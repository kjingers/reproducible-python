import importlib
import numpy.testing as npt

country = importlib.import_module('.data.03_country-subset', 'src')

interim_data = "data/interim/2018-05-09-winemag_priceGBP.csv"
processed_data = "data/processed/2018-05-09-winemag_Chile.csv"

def test_get_mean_price():
    mean_price = country.get_mean_price(processed_data)
    assert mean_price == 20.7865
    npt.assert_allclose(country.get_mean_price(processed_data),
                                    20.787, rtol = 0.01)