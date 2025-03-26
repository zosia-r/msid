import pandas as pd

input_file = 'dataset.csv'
output_file = 'basic_statistics.csv'

try:
    df = pd.read_csv(input_file)
except Exception as e:
    print(f"Error reading file {input_file}/n{e}")
    exit(1)



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


try:
    results_df.to_csv(output_file, index=False)
except Exception as e:
    print(f"Error writing file {output_file}/n{e}")
    exit(1)

print(f"Statistics saved to file {output_file}")
