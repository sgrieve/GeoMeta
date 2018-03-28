import json

import rasterio
import rasterio.warp
import rasterio.features


def get_meta(datafile, source_info=None, outputfile=None):

    with rasterio.open(datafile) as data:
        # Read the dataset's valid data mask as a ndarray.
        mask = data.dataset_mask()

        # Extract feature shapes and values from the array.
        for geo_info, val in rasterio.features.shapes(
                mask, transform=data.transform):

            # Transform shapes from the dataset's own coordinate
            # reference system to CRS84 (EPSG:4326).
            geo_info = rasterio.warp.transform_geom(
                data.crs, 'EPSG:26917', geo_info, precision=6)

    metadata = {
        'georeferencing': {
            'spatial extent': geo_info,
            'EPSG': 26917}
        'driver': data.driver,
        'width': data.width,
        'height': data.height,
        'count': data.count,
        'dtypes': data.dtypes,
        'crs': data.crs.to_string(),
        'transform': data.transform,
        'nodata': data.nodata,
        'bounding_box': data.bounds
    }

    if source_info is not None:
        metadata['source info'] = source_info

    if outputfile:
        with open(outputfile, 'w') as of:
            json.dump(metadata, of)
    else:
        return json.dumps(metadata, indent=2)


def from_metadata(datafile, metadata):
    pass
