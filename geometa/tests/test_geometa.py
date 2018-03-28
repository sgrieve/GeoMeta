import rasterio
from .. import get_meta, apply_meta


def test_get_meta():
    get_meta("sample_data/subset_data_1/subset_data_1.tif",
             outputfile="temp_output.json")
    apply_meta("temp_output.json", "sample_data/full_data_1/full_data_1.tif")

    out_data = rasterio.open("out_full_data_1.tif")
    data1 = out_data.read(1)
    dataset2 = rasterio.open("sample_data/subset_data_1/subset_data_1.tif")
    data2 = dataset2.read(1)
    assert (data1 == data2).all()
