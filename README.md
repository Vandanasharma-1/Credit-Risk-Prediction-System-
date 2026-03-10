# 🏦 Credit Risk Prediction System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Data Science](https://img.shields.io/badge/Data%20Science-008080?style=for-the-badge&logo=jupyter&logoColor=white)

## 📌 Project Overview
Lending institutions face significant financial risks when borrowers default. This project provides a robust, data-driven solution for predicting credit risk using a comprehensive dataset of **100,000+ loan records**. By leveraging advanced ensemble techniques and an interactive **Streamlit dashboard**, this system classifies loans into "Good" or "Bad" categories to assist in informed lending decisions.

## 🚀 Interactive Web Application
I transformed the analytical model into a functional **Streamlit App** to demonstrate real-world deployment. 
- **User Inputs:** Borrowers can enter annual income, loan amount, and employment stability.
- **Instant Classification:** The app provides a real-time risk assessment using the trained model.
- **Regional Analysis:** Incorporates geographical risk factors based on major economic zones.

## 🛠️ Technical Deep Dive

### 1. Advanced Data Engineering & Cleaning
- **Target Definition:** Created a binary classification target by clustering loan statuses like 'Charged Off', 'Default', and 'Late' as "Bad Loans".
- **Feature Optimization:** Mapped 50+ US states into 5 strategic regions (West, SouthWest, SouthEast, MidWest, NorthEast) to capture regional economic variance.
- **Resource Management:** Integrated `psutil` to monitor system RAM usage, ensuring efficient processing of high-dimensional data on limited hardware.

### 2. Model Benchmarking
I evaluated 11+ different architectures to find the optimal balance between accuracy and reliability.

| Model Architecture | AUC Score |
| :--- | :--- |
| **Light GBM** | **0.880** |
| Gradient Boosting | 0.880 |
| Neural Network | 0.879 |
| XGBoost | 0.878 |
| **Stacking Ensemble (XGB Meta)** | **0.866** |
| Random Forest (Bagging) | 0.871 |

### 3. Ensemble Strategies
- **Bagging:** Implemented Bagging classifiers for Logistic Regression and Decision Trees to reduce variance.
- **Stacking:** Developed a meta-model using XGBoost to aggregate predictions from multiple base learners, enhancing overall predictive stability.

## 💻 Tech Stack
- **Languages:** Python (Pandas, NumPy)
- **Machine Learning:** Scikit-Learn, XGBoost, LightGBM
- **Deep Learning:** Neural Networks (MLP)
- **Interface:** Streamlit
- **Visualization:** Matplotlib, Seaborn

## 📈 Business Impact
- **Risk Mitigation:** Identifying potential "Bad" loans early helps reduce financial losses.
- **Automated Screening:** Provides a scalable alternative to manual credit reviews.
- **Actionable Insights:** Pinpoints critical risk drivers like regional economic trends and employment history.

## 📂 Project Structure
```text
├── Credit Risk Prediction System.ipynb  # Core analysis & model development
├── app.py                              # Streamlit web application script
├── requirements.txt                    # Project dependencies
├── credit_model.pkl                    # Serialized trained model
└── README.md                           # Project documentation

⚙️ Installation & Usage
Clone the repository:

Bash
git clone [https://github.com/your-username/credit-risk-system.git](https://github.com/your-username/credit-risk-system.git)
cd credit-risk-system
Install requirements:

Bash
pip install -r requirements.txt
Launch the App:

Bash
streamlit run app.py
