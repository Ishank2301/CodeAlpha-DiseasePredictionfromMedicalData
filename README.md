# Heart Disease Prediction Using Machine Learning

## Overview

This project aims to predict the likelihood of heart disease in patients using machine learning techniques and clinical health indicators.

The project follows a complete machine learning workflow including:

* Data Exploration and Visualization
* Data Preprocessing
* Feature Analysis
* Model Training and Evaluation
* Model Comparison
* Model Deployment Preparation

---

## Dataset Information

The dataset contains clinical information collected from patients and includes:

| Feature  | Description                       |
| -------- | --------------------------------- |
| age      | Age of patient                    |
| sex      | Gender (0 = Female, 1 = Male)     |
| cp       | Chest pain type                   |
| trestbps | Resting blood pressure            |
| chol     | Serum cholesterol                 |
| fbs      | Fasting blood sugar               |
| restecg  | Resting ECG results               |
| thalach  | Maximum heart rate achieved       |
| exang    | Exercise induced angina           |
| oldpeak  | ST depression induced by exercise |
| slope    | Slope of peak exercise ST segment |
| ca       | Number of major vessels           |
| thal     | Thalassemia                       |
| target   | Presence of heart disease         |

### Dataset Statistics

* Total Records: 1,025
* Features: 13
* Target Variable: Heart Disease Presence
* Missing Values: 0
* Duplicate Records Identified: 723

---

## Exploratory Data Analysis

The following analyses were performed:

* Target Class Distribution
* Age Distribution Analysis
* Age vs Heart Disease
* Gender vs Heart Disease
* Chest Pain Type Analysis
* Cholesterol Distribution
* Maximum Heart Rate Analysis
* Pairwise Feature Relationships
* Correlation Heatmap

These visualizations helped identify relationships between clinical features and heart disease outcomes.

---

## Machine Learning Models Evaluated

The following classification algorithms were trained and compared:

1. Logistic Regression
2. Support Vector Machine (SVM)
3. Random Forest Classifier
4. XGBoost Classifier

---

## Model Performance

| Model               |   Accuracy | Precision | Recall | F1 Score |
| ------------------- | ---------: | --------: | -----: | -------: |
| Logistic Regression | **80.33%** |    80.00% | 84.85% |   82.35% |
| SVM                 |     77.05% |    77.14% | 81.82% |   79.41% |
| Random Forest       |     75.41% |    76.47% | 78.79% |   77.61% |
| XGBoost             |     72.13% |    73.53% | 75.76% |   74.63% |

### Best Performing Model

**Logistic Regression**

Accuracy: **80.33%**

The Logistic Regression model achieved the highest overall performance on the test set and was selected as the final deployment model.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Joblib

---

## Project Structure

```text
Heart-Disease-Prediction/
│
├── models/
│   └── best_model.pkl
│
├── notebooks/
│   └── Heart_Disease_Prediction.ipynb
│
├── src/
│   ├── preprocess.py
│   └── predict.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Future Improvements

* Hyperparameter Optimization
* Feature Selection
* Cross Validation
* Streamlit Deployment
* Explainable AI using SHAP
* Ensemble Learning Approaches

---

## Results

The project successfully demonstrates the use of machine learning techniques for predicting heart disease risk using clinical attributes. Logistic Regression emerged as the most effective model among the evaluated algorithms, achieving an accuracy of 80.33%.
