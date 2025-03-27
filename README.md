
# Estimation of Obesity Levels Based On Eating Habits and Physical Condition

[Dataset description]
(https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition)


## Requirements -> `environment.yml`


## Running the project
```python
python data_analysis_main.py
```


## Project structure
 ### `data_analysis_main.py`
 Main script that orchestrates the obesity data analysis pipeline. Loads data from CSV, renames columns using a predefined mapping, and processes it through various analysis stages including basic statistics calculation and visualization generation (boxplots, violinplots, histograms, heatmaps, and regression plots).

 ### `data_io.py`
 Utility file that provides core data input/output functionality. Contains functions for reading CSV files into pandas DataFrames and saving DataFrames back to CSV files, both with error handling.

 ### `rename_columns.py`
 Utility module containing a function that renames DataFrame columns based on a provided dictionary mapping, making data more interpretable with descriptive column names.

 ### `basic_statistics.py`
 Module that generates comprehensive statistical summaries of datasets. Contains a function that calculates descriptive statistics (mean, median, min/max, standard deviation, percentiles) for numerical features and category counts/proportions for categorical features, returning results as a structured DataFrame.

 ### `generate_plots.py`
 Visualization module with extensive plotting functionality for data exploration. Implements functions for creating and saving multiple visualization types: boxplots, violin plots, histograms, correlation heatmaps, and regression plots. Each function includes customization options for appearance and automatically organizes output into appropriate folders.

_Zofia Różańska
280526_