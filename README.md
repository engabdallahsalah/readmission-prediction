
# 🏥 Hospital Readmission Prediction

This project aims to predict whether a patient will be readmitted to the hospital using machine learning techniques on a real-world dataset.

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
├── app.py                    # Streamlit app for demo (optional)
├── data/
│   └── cleaned_data.csv      # Cleaned dataset used for training
├── images/
│   └── roc_curve.png         # Model performance visual
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
git clone https://github.com/YourUsername/readmission-prediction.git
cd readmission-prediction
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the notebook:

```bash
jupyter notebook main_notebook.ipynb
```

4. (Optional) Run the app:

```bash
streamlit run app.py
```

---

## 🚀 Demo

🔗 Add a link here if you deploy it on [Streamlit Cloud](https://streamlit.io/cloud) or a similar platform.

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
