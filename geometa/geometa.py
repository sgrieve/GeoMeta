import json
import os

import rasterio
import rasterio.warp
import rasterio.features
from rasterio import mask


__all__ = ["get_meta", "apply_meta"]


def get_meta(datafile, dataset_doi=None, publication_doi=None,
             outputfile=None):
    """
    Generating geospatial metadata from Digital Elevation Model files.

    Parameters
    ----------
    datafile : str
        Filename for data file. Format should be supported by the
        rasterio packgage.
    dataset_doi : str
        DOI for the original raw data
    publication_doi : str
        Reference publication for this dataset
    outputfile : str
        Name of output file to dump the metadata information


    """
    with rasterio.open(datafile) as data:
        # Read the dataset's valid data mask as a ndarray.
        mask = data.dataset_mask()

        # Extract feature shapes and values from the array.
        for geo_info, val in rasterio.features.shapes(
                mask, transform=data.transform):

            # Transform shapes from the dataset's own coordinate
            # reference system to CRS84 (EPSG:4326).
            geo_info = rasterio.warp.transform_geom(
                data.crs, data.crs, geo_info, precision=6)

    metadata = {
        'georeferencing': {
            'spatial extent': geo_info,
            'EPSG': get_epsg_code(data)},
        'driver': data.driver,
        'width': data.width,
        'height': data.height,
        'count': data.count,
        'dtypes': data.dtypes,
        'crs': data.crs.to_string(),
        'transform': data.transform,
        'bounding_box': data.bounds,
        'source info': {}
    }

    if dataset_doi is not None:
        metadata['source info']['dataset DOI'] = dataset_doi

    if publication_doi is not None:
        metadata['source info']['publication DOI'] = publication_doi

    if outputfile:
        with open(outputfile, 'w') as of:
            json.dump(metadata, of)
    else:
        return json.dumps(metadata, indent=2)


def apply_meta(json_file, data_file, out_file=None):
    """
    Generating Digital Elevation Model file that is a subset of the
    original data, based on the input metadata.

    Parameters
    ----------
    json_file : str
        Filename for metadata file. Should be in json format.
    data_file : str
        Filename for input data file, corresponding to the whole area.
    out_file : str
        Filename for output data file. If not there, a name is created
        from the input file.
    """
    json_meta = json.load(open(json_file))
    s = json_meta["georeferencing"]["spatial extent"]

    with rasterio.open(data_file) as dataset:
        # This will throw for non-overlapping datasets - catch it!
        maskout_data = mask.mask(dataset, [s], crop=True)

    if not out_file:
        out_file = "out_"+os.path.basename(data_file)
    outfile = rasterio.open(
                out_file, 'w', driver=json_meta['driver'],
                width=json_meta['width'], height=json_meta['height'],
                count=json_meta['count'], dtype=json_meta['dtypes'][0],
                crs=json_meta['crs'],
                transform=json_meta['transform'],
                nodata=-9999)
    outfile.write(maskout_data[0][0], 1)
    outfile.close()


class GeometaException(RuntimeError):
    """An error incurred during processing using GeoMeta."""


def get_epsg_code(data):
    """Extract the EPSG code (as an integer) from a RasterIO dataset.

    Currently assumes that there is only a single CRS specified. Will throw
    an exception if the code cannot be extracted.
    """
    if not data.crs.is_epsg_code:
        raise GeometaException(
                "The dataset's CRS does not correspond to an EPSG code.")
    else:
        return int(data.crs.to_string().split(":")[-1])
