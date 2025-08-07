# Loan-Analysis
## 🚀 Project Overview
Banks often receive thousands of loan applications, and manually assessing each can be inefficient. This project uses historical loan data to automate and optimize the decision-making process using classification models.


## 🧩 Problem Statement
The goal of this project is to build a machine learning model that predicts whether a loan will be approved for an applicant based on various features like income, credit history, education, and property area.



## 🔍 Methodology
1. **Data Cleaning**  
   - Handled missing values using mean/mode imputation.
2. **Feature Engineering**  
   - Categorical encoding using `LabelEncoder` and `get_dummies`.
3. **Exploratory Data Analysis (EDA)**  
   - Visualized loan status distribution, income levels, and credit history.
4. **Model Building**  
   - Trained multiple models: `Logistic Regression`, `Decision Tree`, `Random Forest`, and `K-Nearest Neighbors`.
5. **Evaluation**  
   - Evaluated using `accuracy_score`, `confusion_matrix`, and `classification_report`.

## 📌 Key Insights
- **Credit History** was the strongest predictor of loan approval.
- **Random Forest** and **Logistic Regression** performed the best among tested models.
- Preprocessing and balanced categorical encoding significantly improved model performance.

## 🛠️ Tools & Libraries Used
- Python, Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn
