import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

def save_boxplots_numerical_by_categorial(df, output_folder='results/plots/boxplots'):
    '''This function creates boxplots of numerical columns by categorical columns 
    in the input DataFrame and saves them to the output folder.'''

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    
    for num_col in numerical_columns:
        for cat_col in categorical_columns:
            sns.boxplot(x=cat_col, y=num_col, data=df, palette='rocket', hue='Gender')
            plt.title(f'Boxplot of {num_col} by {cat_col}', fontsize=14)
            plt.xlabel(cat_col, fontsize=10)
            plt.ylabel(num_col, fontsize=10)
            plt.xticks(rotation=45, fontsize=6)
            plt.yticks(rotation=45, fontsize=6)
            plot_filename = f'{output_folder}/{num_col}_by_{cat_col}_boxplot.png'
            plt.savefig(plot_filename)
            plt.close()
    
    print(f"All boxplots have been saved to the '{output_folder}' folder.")



def save_boxplots_categorial_by_categorial(df, output_folder='results/plots/boxplots'):
    '''This function creates boxplots of categorical columns by categorical columns 
    in the input DataFrame and saves them to the output folder.'''

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    
    for cat_col1 in categorical_columns:
        for cat_col2 in categorical_columns:
            if cat_col1 != cat_col2:
                sns.boxplot(x=cat_col1, y=cat_col2, data=df, palette='rocket', hue='Gender')
                plt.title(f'Boxplot of {cat_col2} by {cat_col1}', fontsize=14)
                plt.xlabel(cat_col1, fontsize=10)
                plt.ylabel(cat_col2, fontsize=10)
                plt.xticks(rotation=45, fontsize=6)
                plt.yticks(rotation=45, fontsize=6)
                plot_filename = f'{output_folder}/{cat_col2}_by_{cat_col1}_boxplot.png'
                plt.savefig(plot_filename)
                plt.close()
    
    print(f"All boxplots have been saved to the '{output_folder}' folder.")



def save_violinplots_numerical_by_categorial(df, output_folder='results/plots/violinplots'):
    '''This function creates violin plots of numerical columns by categorical columns 
    in the input DataFrame and saves them to the output folder.'''

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    
    for num_col in numerical_columns:
        for cat_col in categorical_columns:
            sns.violinplot(x=cat_col, y=num_col, data=df, palette='rocket', hue='Gender')
            plt.title(f'Violin Plot of {num_col} by {cat_col}', fontsize=14)
            plt.xlabel(cat_col, fontsize=10)
            plt.ylabel(num_col, fontsize=10)
            plt.xticks(rotation=45, fontsize=6)
            plt.yticks(rotation=45, fontsize=6)
            plot_filename = f'{output_folder}/{num_col}_by_{cat_col}_violinplot.png'
            plt.savefig(plot_filename)
            plt.close()
    
    print(f"All violin plots have been saved to the '{output_folder}' folder.")


def save_violinplots_categorial_by_categorial(df, output_folder='results/plots/violinplots'):
    '''This function creates violin plots of categorical columns by categorical columns 
    in the input DataFrame and saves them to the output folder.'''

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    
    for cat_col1 in categorical_columns:
        for cat_col2 in categorical_columns:
            if cat_col1 != cat_col2:
                sns.violinplot(x=cat_col1, y=cat_col2, data=df, palette='rocket', hue='Gender')
                plt.title(f'Violin Plot of {cat_col2} by {cat_col1}', fontsize=14)
                plt.xlabel(cat_col1, fontsize=10)
                plt.ylabel(cat_col2, fontsize=10)
                plt.xticks(rotation=45, fontsize=6)
                plt.yticks(rotation=45, fontsize=6)
                plot_filename = f'{output_folder}/{cat_col2}_by_{cat_col1}_violinplot.png'
                plt.savefig(plot_filename)
                plt.close()
    
    print(f"All violin plots have been saved to the '{output_folder}' folder.")



def save_histograms(df, output_folder='results/plots/histograms'):
    '''Generates and saves histograms for each numerical column in the DataFrame.'''

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    numerical_columns = df.select_dtypes(include=['number']).columns

    for col in numerical_columns:

        sns.histplot(data=df, x=col, hue='Gender', palette='rocket', multiple='dodge')     

        plt.title(f'Histogram of {col}', fontsize=14)
        plt.xlabel(col, fontsize=10)
        plt.ylabel("Count", fontsize=10)

        plt.xticks(rotation=45)

        plt.savefig(f'{output_folder}/{col}_histogram.png')
        plt.close()

    print(f"All histogram plots with error bars have been saved to the '{output_folder}' folder.")



def save_heatmap_of_correlation_matrix(df, output_folder='results/plots/heatmaps'):
    '''Generates and saves a heatmap of the correlation matrix for the DataFrame.'''

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    numerical_data = df.select_dtypes(include=['number'])

    corr = numerical_data.corr()

    # Create a mask to display only the lower triangle of the heatmap
    mask = np.triu(np.ones_like(corr, dtype=bool))

    sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=True, fmt=".2f", cbar_kws={"shrink": .8})

    plt.title('Heatmap of Correlation Matrix', fontsize=16)

    plt.xticks(rotation=45, size=6)
    plt.yticks(size=6)
    plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
    
    plt.savefig(f'{output_folder}/correlation_heatmap.png')
    plt.show()
    plt.close()

    print(f"Correlation heatmap has been saved to the '{output_folder}' folder.")