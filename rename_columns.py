
def rename_columns_based_on_dict(df, column_dict):
    '''Function that renames columns in the DataFrame based on the provided dictionary.'''

    df_renamed = df.rename(columns=column_dict)
    
    return df_renamed
