# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean = np.mean(sale_price)
    median = np.median(sale_price)
    mode = sale_price.mode()[0]

    plt.figure(figsize=(10, 6))
    plt.hist(sale_price, bins=40)
    plt.plot([mode]*300, range(300), label='mode')
    plt.plot([median]*300, range(300), label='median')
    plt.plot([mean]*300, range(300), label='mean')
    plt.ylim(0, 250)
    plt.legend()
    plt.show()
