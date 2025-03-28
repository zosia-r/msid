from basic_statistics import get_basic_statistics_df
from data_io import read_data, save_data
from rename_columns import rename_columns_based_on_dict
import generate_plots as gp


input_file = 'dataset.csv'


feature_label_dictionary = {
    'Gender': 'Gender',
    'Age': 'Age',
    'Height': 'Height',
    'Weight': 'Weight',
    'family_history_with_overweight': 'Family History of Overweight',
    'FAVC': 'High Caloric Food Frequency',
    'FCVC': 'Vegetables in Meals',
    'NCP': 'Main Meals Daily',
    'CAEC': 'Eat Between Meals',
    'SMOKE': 'Smoking',
    'CH2O': 'Water Intake',
    'SCC': 'Monitor Calories',
    'FAF': 'Physical Activity Frequency',
    'TUE': 'Technology Use Time',
    'CALC': 'Alcohol Consumption',
    'MTRANS': 'Usual Transportation Mode',
    'NObeyesdad': 'Obesity Level'
}




if __name__ == '__main__':
    # 3.0
    df = read_data(input_file)
    df = rename_columns_based_on_dict(df, feature_label_dictionary)

    results_df = get_basic_statistics_df(df)
    save_data(results_df, output_file='results/basic_statistics.csv')

    # 3.5
    gp.save_boxplots_numerical_by_categorial(df,)
    gp.save_boxplots_categorial_by_categorial(df)
    gp.save_violinplots_numerical_by_categorial(df)
    gp.save_violinplots_categorial_by_categorial(df)

    # 4.0
    gp.save_histograms(df)

    # 4.5
    gp.save_heatmap(df)

    # 5.0
    gp.save_regression_plots(df)

   # 5.5
    gp.save_dimension_reduction_plots(df)

