import pandas as pd
import os

def read_data(input_file):
    '''Reads the csv input file and returns a pandas dataframe'''

    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading file {input_file}/n{e}")
        exit(1)
    return df



def save_data(results_df, output_file):
    '''Saves given dataframe to a csv file'''
    
    try:
        results_df.to_csv(output_file, index=False)
    except Exception as e:
        print(f"Error writing file {output_file}/n{e}")
        exit(1)

    print(f"Dataframe saved to file {output_file}")