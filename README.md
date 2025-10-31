# 🧫 Smart Hygiene — Centre National de Greffe, Tunis  
**Jan – May 2025 | TensorFlow · Random Forest · Flask · React.js**

---

## 💡 Project Overview

**Smart Hygiene** is an intelligent system developed for the **Centre National de Greffe, Tunis**, aimed at **optimizing the use of disinfectants and improving hygiene protocols** through AI-driven predictions.

The platform integrates **machine learning**, **web development** to provide a scalable solution that assists medical staff in:
- Detecting germs present on a given surface,
- Estimating the number of colonies,
- Recommending the most effective disinfectant,
- Predicting the optimal volume of disinfectant to apply.

---

## 🧠 Machine Learning Pipeline

The system is built upon a **multi-model Random Forest pipeline**, combining both classification and regression tasks:

| Task | Model | Objective |
|------|--------|------------|
| 🦠 Germ Detection | RandomForestClassifier | Identify the presence and type of germs on surfaces |
| 🧫 Colony Estimation | RandomForestRegressor | Estimate the number of germ colonies detected |
| 🧴 Disinfectant Recommendation | RandomForestClassifier | Suggest the most effective disinfectant |
| 💧 Volume Prediction | RandomForestRegressor | Estimate the recommended volume of disinfectant to use |

The ML models were trained and optimized using **TensorFlow for data preprocessing and feature extraction**, followed by **Random Forest models** for robust decision-making.

### 🔬 Results
- **20% reduction in disinfectant usage** through optimization of dosage and selection.  
- Improved **prediction accuracy** by combining multi-model ensemble logic.  
- Fast and interpretable predictions suitable for real-time deployment.

---

## 🌐 Web Platform Features

- **User account management** (Flask + JWT Authentication)
- **Messaging system** between lab personnel
- **Chatbot assistant** presenting the centre and its services
- **Interactive analytics dashboard** (React.js)
- **RESTful API** for communication between frontend and backend

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React.js, Tailwind CSS |
| **Backend** | Flask, REST API, Spring boot |
| **Machine Learning** | TensorFlow, Random Forest, Pandas, sci-kit learn|
| **Database** | PostgreSQL |
| **Visualization** | Matplotlib, Plotly |

---

