# Fetal-Health-XGBoost-Classifier
An online application built on Flask that classifies foetal health from CTG data as normal, suspicious, or pathological using the XGBoost algorithm.  It facilitates the early diagnosis of pregnancy problems with 96% accuracy.  Through an intuitive interface, users may register, log in, and receive forecasts.
# FetalHealth-XGBoost-Classifier

## 📌 Project Overview

Pregnancy complications pose significant risks to maternal and fetal health, requiring early and accurate diagnosis. This project presents a Machine Learning-based approach using **XGBoost**, a powerful gradient boosting algorithm, to classify fetal health based on **cardiotocography (CTG)** data.

With an achieved accuracy of **96%**, the model demonstrates significant potential in supporting medical professionals with timely and precise fetal health assessments.

---

## 💡 Features

- Classifies fetal health as **Normal**, **Suspect**, or **Pathological**
- Uses **XGBoost** for high performance and accuracy
- Built with **Flask** for a lightweight web interface
- Allows users to **register** and **log in** securely
- Simple and interactive prediction form

---

## 🚀 Technologies Used

- Python (3.8 or 3.9)
- Flask 3.0.3
- pandas 2.0.3
- xgboost 2.1.3
- HTML/CSS (for frontend)

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/FetalHealth-XGBoost-Classifier.git
cd FetalHealth-XGBoost-Classifier


### 2. Create a Virtual Environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
### 3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
### 4. Run the Flask App
bash
Copy
Edit
python app.py
Then open your browser and navigate to:

cpp
Copy
Edit
http://127.0.0.1:5000/
🔐 Login Info
You can register a new account yourself via the web interface.

Example:

Username: admin

Password: admin

📊 Dataset
This project uses a publicly available CTG dataset containing fetal heart rate and uterine contraction measurements for health classification. The dataset includes features extracted from cardiotocograms.

📈 Model Accuracy
Model Used: XGBoost (eXtreme Gradient Boosting)

Accuracy Achieved: 96%

✨ Future Enhancements
Add charts to visualize fetal health predictions

Integrate additional clinical parameters

Deploy to cloud (e.g., Heroku, Render)
