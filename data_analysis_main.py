from basic_statistics import get_basic_statistics_df
from data_io import read_data, save_data

import pandas as pd


input_file = 'dataset.csv'
output_file = 'basic_statistics.csv'





if __name__ == '__main__':
    df = read_data(input_file)
    results_df = get_basic_statistics_df(df)
    save_data(results_df, output_file)