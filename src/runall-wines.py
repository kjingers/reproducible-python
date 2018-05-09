import importlib
import src

# Import modules
subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')


raw_data = "data/raw/winemag-data-130k-v2.csv"
interim_data = "data/interim/2018-05-09-winemag_priceGBP.csv"
country = "Chile"



# Run all processing scripts
subset.process_data_GBP('data/raw/winemag-data-130k-v2.csv')
plotwines.create_plots('data/interim/2018-05-09-winemag_priceGBP.csv')
country_sub.get_country('data/interim/2018-05-09-winemag_priceGBP.csv', "Chile")

if __name__ == '__main__':
    subset.process_data_GBP(raw_data)
    plotwines.create_plots(interim_data)
    country_sub.get_country(interim_data, country)