# Credit Risk Prediction System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-1572B6?style=for-the-badge&logo=pandas&logoColor=white)

## 📌 Project Overview
In the financial industry, accurately assessing credit risk is vital for maintaining a healthy loan portfolio. This project focuses on building a robust machine learning pipeline to predict the likelihood of loan default. Using a massive dataset of over 100,000 records, the system classifies loans into "Good" or "Bad" categories, enabling data-driven decision-making for lenders.



## 🛠️ Key Technical Challenges & Solutions
- **Handling High-Dimensional Data:** Processed a complex dataset with over 150 initial features, performing rigorous feature selection and engineering to identify the most predictive variables.
- **Class Imbalance Management:** Addressed the significant disparity between "Good" loans (86.6%) and "Bad" loans (13.4%) to ensure the model effectively identifies high-risk applicants.
- **Memory Optimization:** Utilized `psutil` and efficient data handling techniques to manage large-scale data processing within limited RAM environments.

## 📊 The Machine Learning Pipeline

### 1. Advanced Data Engineering
- **Target Engineering:** Defined "Bad" loans by clustering statuses such as 'Charged Off', 'Default', and 'Late' to create a binary classification target.
- **Feature Mapping:** Transformed categorical employment lengths into numerical formats and mapped individual US states into 5 strategic regions (West, SouthWest, SouthEast, MidWest, NorthEast) to capture regional economic trends.
- **Missing Value Strategy:** Implemented sophisticated imputation and cleaning techniques to handle null values without losing critical information.

### 2. Model Benchmarking
I implemented and compared 11+ different modeling approaches, ranging from traditional statistics to advanced ensemble methods.

| Model Implementation | Performance (AUC) |
| :--- | :--- |
| **Stacking Model (XGB Meta)** | **0.866** |
| LightGBM | 0.880 |
| Gradient Boosting | 0.880 |
| Neural Network | 0.879 |
| XGBoost | 0.878 |
| Logistic Regression (Bagging) | 0.853 |



## 🚀 Technical Stack
- **Languages:** Python (Pandas, NumPy)
- **Machine Learning:** Scikit-Learn, XGBoost, LightGBM
- **Ensemble Techniques:** Bagging, Stacking, Boosting
- **Deep Learning:** Artificial Neural Networks (ANN)
- **Monitoring:** psutil (Resource Management)

## 📈 Business Impact & Results
The final **Stacking Model** provides a sophisticated approach to risk management. By leveraging the strengths of multiple base learners, the system offers:
- **Reduced Financial Loss:** Improved detection of potential defaults before loan disbursement.
- **Automated Workflow:** Replaces manual review with a scalable, objective scoring system.
- **Actionable Insights:** Identified key risk factors such as regional economic status and employment stability.

## 📂 Project Structure
```text
├── Credit Risk Prediction System.ipynb  # Main development and analysis notebook
├── data/                               # (Optional) Data source directory
└── README.md                           # Project documentation
