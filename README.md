# EDA & Evaluation and Optimization of Machine Learning Models

This repository contains a multi-stage academic project focused on **building, evaluating, and optimizing machine learning models** from high-level libraries to low-level implementations. The project explores how model performance changes depending on the **implementation approach, regularization techniques and hyperparameter settings**. The work is divided into three parts, each implemented in separate folders with **Python code and Jupyter notebooks**. A full analysis and discussion of the results is provided in the accompanying report.

---

## Project Goals

The main objective of the project was to investigate practical aspects of machine learning model development:

- implementing models using **different frameworks**
- comparing **library implementations vs. custom implementations**
- analyzing **training dynamics and convergence**
- studying **overfitting and underfitting**
- evaluating the impact of:
  - feature selection
  - regularization
  - dataset balancing
  - hyperparameter tuning
  - ensemble methods

The project focuses on both **classification and regression tasks**.

---

## Dataset

This project uses the **Estimation of Obesity Levels Based on Eating Habits and Physical Condition** dataset. 
https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition

**Dataset overview**

- 2,111 samples
- 16 input features + 1 target variable
- Features describe demographics, eating habits, and physical activity
- Main task: classification of obesity levels

The target variable `NObeyesdad` represents 7 obesity categories, ranging from *Insufficient Weight* to *Obesity Type III*.
---

## Technologies Used

- Python
- NumPy
- PyTorch
- Scikit-learn
- Jupyter Notebook
- Matplotlib

---

## Tasks

### 1. Exploratory Data Analysis (EDA)

The first part of the project focuses on **exploratory data analysis** of the obesity dataset.

The analysis includes:

- inspecting the structure of the dataset
- analyzing distributions of selected variables
- exploring relationships between features and the target variable
- basic data visualization

The goal of this stage was to better understand the dataset before building machine learning models.

---

### 2. Evaluation of Machine Learning Models

The second part of the project evaluates several machine learning models for predicting obesity level.
Models were implemented using different libraries to compare their performance.

| Model | Implementation | Test Accuracy |
|------|------|------|
| Logistic Regression | Scikit-learn | 90.5% |
| Support Vector Classification | Scikit-learn | 92.2% |
| Decision Tree Classifier | Scikit-learn | 92.6% |
| Logistic Regression | NumPy | 78.5% |
| Logistic Regression | PyTorch (CPU) | 87.2% |
| Logistic Regression | PyTorch (GPU) | 87.9% |

Additionally, a **linear regression task** was performed to predict body weight.

| Model | Implementation | Test MSE |
|------|------|------|
| Linear Regression | NumPy (closed form) | 24.829 |
| Linear Regression | Scikit-learn | 24.829 |

---

### 3. Model Optimization

The final part of the project focuses on **improving and analyzing model performance**.

Experiments include:

- **cross-validation**
- **convergence analysis**
- **feature reduction experiments**
- **L1 and L2 regularization**
- dataset balancing
- hyperparameter optimization
- ensemble methods
- ablation study

The experiments were used to analyze model stability, generalization ability, and the impact of different optimization techniques.

---

## Report

A detailed description of the experiments and results is available in:

```
FINALREPORT.pdf
```
