import pandas as pd


def get_basic_statistics_df(df):
    '''Returns a dataframe with basic statistics for each feature in the input
    dataframe. The statistics include mean, median, min, max, standard deviation,
    5th and 95th percentiles for numerical features, 
    and number of unique classes, number of missing values,
    class proportions for categorical features'''

    numerical_columns = df.select_dtypes(include=["number"]).columns
    categorical_columns = df.select_dtypes(include=["object", "category"]).columns  

    results = []

    for feature in numerical_columns:

        stats = {
            "Feature": feature,
            "Type": "Numerical",
            "Mean": round(df[feature].mean(), 2),
            "Median": round(df[feature].median(), 2),
            "Min": round(df[feature].min(), 2),
            "Max": round(df[feature].max(), 2),
            "Standard deviation": round(df[feature].std(), 2),
            "5th percentile": round(df[feature].quantile(0.05), 2),
            "95th percentile": round(df[feature].quantile(0.95), 2),
            "Unique classes": None,
            "Missing values": df[feature].isnull().sum(),
            "Class proportions": None
        }
        results.append(stats)


    for feature in categorical_columns:

        stats = {
            "Feature": feature,
            "Type": "categorical",
            "Mean": None,
            "Median": None,
            "Min": None,
            "Max": None,
            "Standard deviation": None,
            "5th percentile": None,
            "95th percentile": None,
            "Unique classes": df[feature].nunique(),
            "Missing values": df[feature].isnull().sum(),
            "Class proportions": str(df[feature].value_counts(normalize=True).round(2).astype(str).to_dict())
        }
        results.append(stats)


    results_df = pd.DataFrame(results)
    return results_df
