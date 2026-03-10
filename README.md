# 💳 Credit Risk Prediction System

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Status](https://img.shields.io/badge/Project-Completed-green)

An **end-to-end Machine Learning project** that predicts whether a loan applicant is **Low Risk or High Risk** using financial and demographic information.

The system uses **data preprocessing, feature engineering, ensemble machine learning models, and an interactive Streamlit web application** to provide real-time credit risk predictions.

This project demonstrates the **complete Data Science workflow from raw data to deployment.**

---

# 🚀 Project Highlights

✔ End-to-End Machine Learning Pipeline  
✔ Data Cleaning & Feature Engineering  
✔ Handling Missing Values & Outliers  
✔ Imbalanced Dataset Handling  
✔ Feature Selection & Target Encoding  
✔ Ensemble Models (Bagging & Stacking)  
✔ Deployed using **Streamlit Web Application**  
✔ Real-Time Credit Risk Prediction  

---

# 📊 Business Problem

Financial institutions must evaluate whether a loan applicant is likely to **repay the loan or default**.

Incorrect decisions can cause:

- Financial losses
- High default rates
- Poor credit portfolio quality

This project builds a **predictive system that helps banks identify high-risk applicants before approving loans.**

---

# 🧠 Machine Learning Pipeline

The project follows a **structured ML lifecycle** used in real industry workflows.

## 1️⃣ Data Cleaning
- Removed variables with **>80% missing values**
- Dropped redundant variables
- Removed dynamic indicators

## 2️⃣ Missing Value Treatment
- Imputed missing values for **both categorical and numerical variables**

## 3️⃣ Outlier Detection
- Identified and removed extreme outliers to improve model stability

## 4️⃣ Correlation Analysis
- Removed highly correlated features to prevent multicollinearity

## 5️⃣ Feature Engineering
- Created meaningful variables that improve predictive power

## 6️⃣ Target Encoding
- Applied **target encoding for high-cardinality categorical variables**

## 7️⃣ Feature Scaling
- Normalized numeric variables for improved model convergence

## 8️⃣ Handling Imbalanced Data
- Used techniques to address the **class imbalance problem**

## 9️⃣ Feature Selection
- Selected only the **most important features** for model training

---

# 🤖 Machine Learning Models Used

Multiple models were trained and evaluated to achieve the best performance.

### Algorithms Implemented

- Logistic Regression
- Random Forest
- Gradient Boosting
- Ensemble Learning
- Bagging Models
- Stacking Models

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

The final model was selected based on **overall predictive performance and generalization ability.**

---

# 🖥️ Streamlit Web Application

A **Streamlit-based interactive interface** allows users to input applicant details and receive **instant credit risk predictions.**

### Application Features

✔ Simple User Interface  
✔ Real-Time Prediction  
✔ Financial & Demographic Input Fields  
✔ Instant Loan Risk Classification  

---

# 🏗️ Project Architecture


User Input (Streamlit UI)
│
▼
Data Preprocessing
│
▼
Feature Engineering
│
▼
Trained Machine Learning Model
│
▼
Prediction Output


---

# 📂 Project Structure


Credit-Risk-Prediction/
│
├── app.py
│ Streamlit application for prediction
│
├── Credit Risk Prediction System.ipynb
│ Complete machine learning workflow
│
├── model.pkl
│ Trained machine learning model
│
├── requirements.txt
│ Project dependencies
│
└── README.md
Project documentation


---

# ⚙️ Installation

Clone the repository:


git clone https://github.com/Vandanasharma-1/Credit-Risk-Prediction-System-.git
cd credit-risk-prediction


Install dependencies:


pip install -r requirements.txt


---

# ▶️ Run the Application

Start the Streamlit app:


streamlit run app.py


The application will automatically open in your browser.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Machine Learning Ensemble Techniques

---

# 📈 Business Impact

This system can help financial institutions:

✔ Reduce loan default risk  
✔ Improve credit approval decisions  
✔ Automate risk assessment  
✔ Enable data-driven lending strategies  

---

# 👩‍💻 Author

**Vandana Sharma**

Data Scientist | Machine Learning | AI Enthusiast

Passionate about building **real-world machine learning systems, predictive analytics models, and AI-powered solutions.**

---

⭐ If you found this project useful, consider giving it a **star**!
