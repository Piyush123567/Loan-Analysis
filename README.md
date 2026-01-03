# Loan-Analysis

## 🚀 Project Overview
Banks often receive thousands of loan applications, and manually assessing each can be inefficient.  
This project automates the loan approval decision process using machine learning classification models and provides a live web interface for real-time prediction.

---

## 🌐 Live Application
👉 **Live Demo:**  
https://loan-analysis-mqfdquv9ssh3umzew7nlpg.streamlit.app



---

## 🧩 Problem Statement
The goal of this project is to build a machine learning model that predicts whether a loan will be approved for an applicant based on features such as income, credit history, education, marital status, and property area.

---

## 🔍 Methodology

### 1. Data Cleaning
- Handled missing values using mean and mode imputation.

### 2. Feature Engineering
- Log transformation applied to skewed numerical features.
- Categorical variables encoded using pipelines and transformers.

### 3. Exploratory Data Analysis (EDA)
- Analyzed loan approval distribution.
- Studied the impact of income, credit history, and property area.

### 4. Model Building
Trained and compared multiple models:
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

### 5. Handling Imbalanced Data
- Used **RandomOverSampler** to balance loan approval classes.

### 6. Model Evaluation
- Primary metric: **F1-score** (to handle class imbalance)
- Also evaluated using:
  - Accuracy
  - Confusion Matrix
  - Classification Report

### 7. Model Deployment
- Best-performing model (**Random Forest**) saved using `joblib`.
- Deployed as a **Streamlit web application**.
- Hosted on **Streamlit Community Cloud**.

---

## 📌 Key Insights
- **Credit History** is the strongest predictor of loan approval.
- **Random Forest** achieved the best F1-score after hyperparameter tuning.
- Handling class imbalance significantly improved minority-class prediction.
- Log transformation improved model stability.

---

## 🛠️ Tools & Libraries Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Imbalanced-learn
- XGBoost
- Streamlit

---

## 📂 Repository Structure

