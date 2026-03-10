# 🏦 Credit Risk Prediction System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Data Science](https://img.shields.io/badge/Data%20Science-008080?style=for-the-badge&logo=jupyter&logoColor=white)

An end-to-end Machine Learning project that predicts whether a loan applicant is high risk or low risk based on financial and demographic information.

The project combines data preprocessing, feature engineering, model training, and deployment using Streamlit to create an interactive prediction interface. 
This system helps financial institutions reduce loan default risk and make data-driven credit decisions.



## 🚀 Project Overview
Credit risk assessment is a crucial task for banks and financial institutions. Incorrect risk evaluation can lead to financial losses due to loan defaults. 
This project builds a robust machine learning pipeline to analyze historical loan data and predict the probability of loan repayment.

**The system includes:**
* Advanced data cleaning and preprocessing
* Handling imbalanced datasets
* Feature engineering and encoding techniques
* Multiple machine learning models
* Model bagging and stacking
* Interactive Streamlit web application for predictions

## 📊 Key Features
✔ End-to-End ML Pipeline
✔ Automated Data Cleaning & Missing Value Handling
✔ Outlier Detection and Removal
✔ Feature Engineering & Target Encoding
✔ Handling Highly Imbalanced Data
✔ Feature Selection for Model Optimization
✔ Ensemble Models (Bagging & Stacking)
✔ Interactive Streamlit Prediction Interface

## 🧠 Machine Learning Workflow
The project follows a complete ML lifecycle:

1.  **Data Cleaning**
    * Removed variables with >80% missing values
    * Eliminated redundant and useless variables
    * Removed dynamic indicators
2.  **Missing Value Imputation**
    * Applied appropriate techniques to handle missing values in both numerical and categorical variables.
3.  **Outlier Detection**
    * Identified and removed extreme values to improve model performance.
4.  **Correlation Analysis**
    * Analyzed relationships between variables to remove highly correlated features.
5.  **Feature Engineering**
    * Created meaningful features to improve model learning.
6.  **Target Encoding**
    * Applied target encoding for multi-categorical variables to convert them into useful numerical representations.
7.  **Feature Scaling**
    * Applied normalization to numeric variables for better model convergence.
8.  **Handling Imbalanced Dataset**
    * Implemented techniques to balance the dataset since loan defaults are rare events.
9.  **Feature Selection**
    * Selected the most relevant features to improve model performance and reduce overfitting.



[Image of a machine learning workflow diagram]


## 🤖 Model Development
Multiple machine learning models were trained and evaluated to achieve the best performance.

### Models Used
* Logistic Regression
* Random Forest
* Gradient Boosting
* **Ensemble Methods:**
    * Bagging
    * Stacking Models

### Evaluation Metrics
These models were evaluated using:
* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

## 📈 Model Evaluation
The final model was evaluated on the test dataset to ensure strong generalization. 

**Key goals of the model:**
* Accurately identify high-risk loan applicants
* Minimize false negatives (predicting risky loans as safe)



## 🖥️ Streamlit Web Application
The project includes an interactive Streamlit application (`app.py`) where users can input applicant details and instantly receive a credit risk prediction.

**App Features:**
* User-friendly interface
* Real-time predictions
* Input financial and personal attributes
* Instant loan risk classification



## 📂 Project Structure
```text
Credit-Risk-Prediction/
│
├── app.py                             # Streamlit application
├── requirements.txt                   # Project dependencies
├── Credit Risk Prediction System.ipynb  # Complete ML workflow
├── model.pkl                          # Trained machine learning model
└── README.md                          # Project documentation
⚙️ Installation
Clone the repository:

Bash
git clone [https://github.com/yourusername/credit-risk-prediction.git](https://github.com/yourusername/credit-risk-prediction.git)
cd credit-risk-prediction
Install dependencies:

Bash
pip install -r requirements.txt
▶️ Run the Application
Launch the Streamlit app:

Bash
streamlit run app.py
The application will open in your browser.

📊 Technologies Used
Language: Python

Data Analysis: Pandas, NumPy

Machine Learning: Scikit-learn

Visualization: Matplotlib / Seaborn

Deployment: Streamlit

Techniques: Machine Learning Ensemble Methods

💡 Business Impact
This system can help financial institutions:

Reduce loan default risk

Improve credit approval decisions

Automate risk assessment

Support data-driven lending strategies

👩‍💻 Author
Vandana Sharma Data Scientist | Machine Learning | AI Enthusiast

Passionate about building end-to-end ML systems, predictive analytics, and AI-powered applications that solve real-world problems.

⭐ If you found this project useful, consider giving it a star!
