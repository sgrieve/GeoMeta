from geometa import get_meta
import rasterio

def test_get_meta():
    json_meta = get_meta("sample_data/subset_data_1/subset_data_1.tif")
    dataset1 = apply_meta(json_meta,"sample_data/full_data_1/full_data_1.tif")
    data1 = dataset1.read(1)
    dataset2 = rasterio.open("sample_data/subset_data_1/subset_data_1.tif")
    data2 = dataset2.read(1)
    assert data1 == data2
