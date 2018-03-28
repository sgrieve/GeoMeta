# GeoMeta
Making locations citable.

## Project overview

Building tools to allow the sharing of geospatial metadata and the automatic reconstruction of datasets from raw data and metadata.

## The problem

In geoscience research, spatial data stored as two dimensional arrays, known as digital elevation models (DEMs). Researchers work on spatial subsets of this data, but only cite the original full dataset. This makes it challenging to reproduce geospatial research and results in a lack of transparency in research.

## Install guide

```
pip install -r requirements.txt
```

notes here on gdal/rasterio alpha versions...

## Usage examples

Using the tool within an existing python workflow is simple.

I am a Researcher who wants to create a GeoMeta file for my dataset `myDataSubset.tif`, where the doi of the original data is `10.5069/G9HT2M76` and the doi of my paper is `doi.org/10.1002/esp.3884`. This will write an output GeoMeta file called `myMeta.json`:

```
import geometa
geometa.get_meta('myDataSubset.tif', '10.5069/G9HT2M76',
                 'doi.org/10.1002/esp.3884', 'myMeta.json')
```

I have been given a GeoMeta file `myMeta.json` and want to recreate a dataset. First, download the raw data linked in the DOI field of the `myMeta.json` file. Then download the file, following the instructions given by the data provider `fullData.tif`. This code will generate an output file which matches the original researcher's data file:

```
import geometa
geometa.from_metadata('myMeta.json', 'fullData.tif', 'output.tif')
```

This software supports a wide range of geospatial data formats, the full list of these files can be [found here](http://www.gdal.org/formats_list.html). Please open an issue if a filetype on this list does not work for you.

## Contribution guidelines

Contributions welcome, please open an issue in the issue tracker, or submit a pull request with new features.

You can contact the authors via geometa@swdg.io or on twitter @GIStuart

## Citation


## License

This code is MIT licensed.

## Future steps

The next step for this project is to build out the code and tests to handle more edge cases, where bad data is provided, to attempt to steer the user to correct their data.

The eventual goal for the project is to host the tool online as a service, where researchers can create GeoMeta files without needing to install anything locally on their machines.
