from .geometa import get_meta, from_metadata

# I am a Researcher who wants to create a GeoMeta file for my dataset
get_meta('sample_data/subset_data_1/subset_data_1.tif', '10.5069/G9HT2M76',
                 'doi.org/10.1002/esp.3884', 'myMeta.json')

# I have been given a GeoMeta file and want to recreate
from_metadata('myMeta.json', 'sample_data/full_data_1/full_data_1.tif')
