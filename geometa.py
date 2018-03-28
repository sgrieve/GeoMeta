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
    outfile = rasterio.open("outfile.tiff",'w',driver='GTiff',width=459,height=366,count=1,dtype='float32',crs='+init=epsg:26917',transform=[276853.0, 1.0, 0.0, 3882026.0, 0.0, -1.0],nodata=-9999)
    outfile.write(maskout_data[0][0],1)
    outfile.close()

    #out_data = rasterio.open("outfile.tiff")
    #ctrl_data = rasterio.open("sample_data/subset_data_1/subset_data_1.tif")
    #print((ctrl_data.read(1)==out_data.read(1)).any())


