import rasterio
from rasterio import mask
import json
from shapely.geometry import shape

def apply_meta(json_file, data_file):
    dataset = rasterio.open(data_file)
    json_meta = json.load(open(json_file))
    s = json_meta["georeferencing"]["spatial extent"]
    # This will throw for non-overlapping datasets - catch it!
    maskout_data = mask.mask(dataset,[s],crop=True)
    print(maskout_data[0])

