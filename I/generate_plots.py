import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import OneHotEncoder, StandardScaler
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
            sns.boxplot(x=cat_col, y=num_col, data=df, palette='rocket')

            plt.title(f'Boxplot of {num_col} by {cat_col}', fontsize=14)
            plt.xlabel(cat_col, fontsize=10)
            plt.ylabel(num_col, fontsize=10)

            plt.xticks(rotation=45, fontsize=6)
            plt.yticks(rotation=45, fontsize=6)
            plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
            
            plt.savefig(f'{output_folder}/{num_col}_by_{cat_col}_boxplot.png')
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
                sns.boxplot(x=cat_col1, y=cat_col2, data=df, palette='rocket')

                plt.title(f'Boxplot of {cat_col2} by {cat_col1}', fontsize=14)
                plt.xlabel(cat_col1, fontsize=10)
                plt.ylabel(cat_col2, fontsize=10)

                plt.xticks(rotation=45, fontsize=6)
                plt.yticks(rotation=45, fontsize=6)
                plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)

                plt.savefig(f'{output_folder}/{cat_col2}_by_{cat_col1}_boxplot.png')
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
            sns.violinplot(x=cat_col, y=num_col, data=df, palette='rocket')

            plt.title(f'Violin Plot of {num_col} by {cat_col}', fontsize=14)
            plt.xlabel(cat_col, fontsize=10)
            plt.ylabel(num_col, fontsize=10)

            plt.xticks(rotation=45, fontsize=6)
            plt.yticks(rotation=45, fontsize=6)
            plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)


            plt.savefig(f'{output_folder}/{num_col}_by_{cat_col}_violinplot.png')
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
                sns.violinplot(x=cat_col1, y=cat_col2, data=df, palette='rocket')
                
                plt.title(f'Violin Plot of {cat_col2} by {cat_col1}', fontsize=14)
                plt.xlabel(cat_col1, fontsize=10)
                plt.ylabel(cat_col2, fontsize=10)
               
                plt.xticks(rotation=45, fontsize=6)
                plt.yticks(rotation=45, fontsize=6)
                plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)

                plt.savefig(f'{output_folder}/{cat_col2}_by_{cat_col1}_violinplot.png')
                plt.close()
    
    print(f"All violin plots have been saved to the '{output_folder}' folder.")



def save_histograms(df, output_folder='results/plots/histograms'):
    '''Generates and saves histograms for each ncolumn in the DataFrame.'''

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for col in df.columns:

        sns.histplot(data=df, x=col, hue='Gender', palette='rocket', multiple='dodge')     

        plt.title(f'Histogram of {col}', fontsize=14)
        plt.xlabel(col, fontsize=10)
        plt.ylabel("Count", fontsize=10)

        plt.xticks(rotation=45, size=6)
        plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)


        plt.savefig(f'{output_folder}/{col}_histogram.png')
        plt.close()

    print(f"All histogram plots have been saved to the '{output_folder}' folder.")



def save_heatmap(df, output_folder='results/plots/heatmaps/numerical'):
    '''Generates and saves a heatmap of the correlation matrix for the DataFrame.'''

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    numerical_data = df.select_dtypes(include=['float64', 'int64'])

    corr = numerical_data.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=True, fmt=".2f", cbar_kws={"shrink": .8})

    plt.title('Heatmap of Correlation Matrix', fontsize=16)

    plt.xticks(rotation=45, size=6)
    plt.yticks(size=6)
    plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
    
    plt.savefig(f'{output_folder}/correlation_heatmap.png')
    plt.close()

    print(f'Heatmap saved to the {output_folder} folder.')



def save_regression_plots(df, output_folder='results/plots/regression'):
    '''Creates and saves linear regression plots for every pair of numerical features.'''

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    num_cols = df.select_dtypes(include=['number']).columns

    for col1 in num_cols:
        for col2 in num_cols:
            sns.lmplot(data=df, x=col1, y=col2, aspect=1.2, height=5, scatter_kws={'s': 30}, line_kws={"color": "pink"})

            plt.title(f'Linear Regression: {col1} vs {col2}', fontsize=14)
            plt.xlabel(col1, fontsize=12)
            plt.ylabel(col2, fontsize=12)

            plt.xticks(rotation=45)
            plt.grid(True)
            plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)

            plt.savefig(f'{output_folder}/{col1}_vs_{col2}_linear_regression.png')
            plt.close()

    print(f"Regression plots saved in '{output_folder}'.")



def save_dimension_reduction_plots(df, output_folder='results/plots/dimension_reduction'):
    '''Creates and saves variance plots for PCA and t-SNE dimensionality reduction.'''

    os.makedirs(output_folder, exist_ok=True)

    if df.empty:
        print("DataFrame is empty. No plots will be generated.")
        return

    num_columns = df.select_dtypes(include=['number']).columns
    cat_columns = df.select_dtypes(include=['object']).columns

    if len(cat_columns) > 0:
        one_hot = OneHotEncoder(sparse_output=False)
        one_hot_data = one_hot.fit_transform(df[cat_columns])
        one_hot_df = pd.DataFrame(one_hot_data, columns=one_hot.get_feature_names_out(cat_columns))
        df = df.drop(cat_columns, axis=1, errors='ignore')

    if df.shape[1] == 0:
        print("No numerical columns found after encoding. No plots will be generated.")
        return

    if df.shape[1] > 1:
        scaler = StandardScaler()
        df_scaled = scaler.fit_transform(df)
    else:
        df_scaled = df.to_numpy()

    n_components = min(5, df.shape[1])
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(df_scaled)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=[f'PC{i+1}' for i in range(n_components)],
                y=pca.explained_variance_ratio_,
                palette='viridis')
    plt.title('PCA Explained Variance Ratio', fontsize=16)
    plt.xlabel('Principal Components', fontsize=12)
    plt.ylabel('Explained Variance Ratio', fontsize=12)
    plt.grid(True)
    plt.savefig(f'{output_folder}/pca_variance_ratio.png')
    plt.close()

    if df.shape[1] > 1:
        tsne = TSNE(perplexity=min(30, df.shape[0] - 1), n_iter=1000, random_state=42)
        tsne_data = tsne.fit_transform(df_scaled)
        
        tsne_df = pd.DataFrame(tsne_data, columns=['TSNE1', 'TSNE2'])

        plt.figure(figsize=(10, 6))
        plt.scatter(tsne_df['TSNE1'], tsne_df['TSNE2'], alpha=0.5, edgecolors='k')
        plt.title('t-SNE Visualization', fontsize=16)
        plt.xlabel('t-SNE Component 1', fontsize=12)
        plt.ylabel('t-SNE Component 2', fontsize=12)
        plt.grid(True)
        plt.savefig(f'{output_folder}/tsne_visualization.png')
        plt.close()
    else:
        print("t-SNE requires at least 2 numerical columns. Skipping t-SNE plot.")