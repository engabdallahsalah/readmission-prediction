![hospital-readmission-machine-learning-predictions](images/hospital-readmission-machine-learning-predictions.jpg)

# 🏥 Diabetes Readmission Prediction

This project predicts early hospital readmission (within 30 days) for diabetic patients using machine learning models. The dataset comes from a large US hospital over a span of 10 years.

## 📌 Problem Statement

Hospital readmissions are costly and can indicate issues in patient care. The goal of this project is to build a machine learning model that can predict if a patient will be readmitted based on clinical and demographic data.

---

## 📁 Project Structure

```
📁 readmission-prediction/
│
├── README.md                  # Project overview and guide
├── requirements.txt          # Python packages used
├── readmission_predictor.pkl # Trained ML model
├── main_notebook.ipynb       # EDA, preprocessing, training, and evaluation
├── app.py                    # Streamlit app for demo 
├── images/
│   └── hospital-readmission-machine-learning-predictions.jpg       
```

---

## 🧪 Models Used

- Random Forest
- Logistic Regression
- Decision Tree
- XGBoost

Class imbalance was addressed using techniques like:
- `class_weight='balanced'`
- Performance evaluated using accuracy, precision, recall, and F1-score

---

## 📊 Key Visualizations

- 📉 ROC Curve
- 🔥 Correlation Heatmap
- 📌 Confusion Matrix
- 📈 Feature Importance

---

## 🛠️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/engabdallahsalah/readmission-prediction.git
cd readmission-prediction
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the notebook:

```bash
jupyter diabetes_readmission_prediction.ipynb
```

4. (Optional) Run the app:

```bash
streamlit run app.py
```

---

## 🚀 Demo

🔗 https://readmission-prediction-bmmy9nlqswga62fdpdoxyz.streamlit.app/

---

## 📬 Contact

For questions or collaboration, feel free to reach out:

- **Name**: Eng/ Abdallah Salah  
- **Email**: [engabdallahsalah99@gmail.com](mailto:engabdallahsalah99@gmail.com)  
- **LinkedIn**: [https://linkedin.com/in/abdallah-salahh](https://linkedin.com/in/abdallah-salahh)

---

## ⭐️ Acknowledgments

- Dataset: [https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008]
- Tools: Scikit-learn, XGBoost, Streamlit, Pandas, Matplotlib, Seaborn
