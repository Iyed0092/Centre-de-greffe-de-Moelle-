# 🧫 Smart Hygiene — Centre National de Greffe, Tunis  
**Jan – May 2025 | TensorFlow · Random Forest · Flask · React.js**

---

## 💡 Project Overview

**Smart Hygiene** is an intelligent system developed for the **Centre National de Greffe, Tunis**, aimed at **optimizing disinfectant usage** and improving hygiene protocols through **AI-driven predictions**.

The platform integrates **machine learning** and **web development** to deliver a scalable solution that assists medical staff in:  
- Detecting germs present on a given surface  
- Estimating the number of colonies  
- Recommending the most effective disinfectant  
- Predicting the optimal volume of disinfectant to apply  

---

## 🧠 Machine Learning Pipeline

The system is built upon a **multi-model Random Forest pipeline**, combining classification and regression tasks:

| Task | Model | Objective |
|------|--------|------------|
| 🦠 Germ Detection | RandomForestClassifier | Identify the presence and type of germs on surfaces |
| 🧫 Colony Estimation | RandomForestRegressor | Estimate the number of germ colonies detected |
| 🧴 Disinfectant Recommendation | RandomForestClassifier | Suggest the most effective disinfectant |
| 💧 Volume Prediction | RandomForestRegressor | Estimate the recommended volume of disinfectant to use |

The ML models were trained and optimized using **TensorFlow for preprocessing and feature extraction**, followed by **Random Forest models** for robust decision-making.

### 🔬 Results
- **20% reduction in disinfectant usage** through optimization of dosage and selection  
- Improved **prediction accuracy** using a multi-model ensemble  
- Fast and interpretable predictions suitable for real-time deployment  

---

## 🧩 Data Exploration & Clustering Analysis

### 🧪 Cabine Similarity Analysis
The **Centre National de Greffe** operates numerous cabins (e.g., *Cabine 1, Cabine 2, Chambre Lyma, Chambre Trabelsi*).  
We used the **Silhouette Method** to determine the optimal number of clusters for grouping cabins with similar germ patterns and colony counts.  

- **Optimal K = 8**  

<p align="center">
  <img src="https://github.com/Iyed0092/Smart-Hygiene-Centre-National-de-Greffe-Tunis-/raw/main/assets/silhouette-chambres.png" width="600"/>
</p>
<p align="center"><em>Silhouette plot for cabine clustering — identifying similar contamination profiles.</em></p>

### 🪑 Furniture Grouping Analysis
A similar clustering approach was applied to the **furniture items** in each cabin (*chaise, chaise percée, dessus éclairage, interphone, lit, matelas, lavabo*, etc.), grouping pieces with similar contamination patterns.  

- **Optimal K = 4**  

<p align="center">
  <img src="https://github.com/Iyed0092/Smart-Hygiene-Centre-National-de-Greffe-Tunis-/raw/main/assets/silhouette-pt-prelevement.png" width="600"/>
</p>
<p align="center"><em>Silhouette plot for furniture clustering — identifying contamination patterns by object type.</em></p>

These insights helped refine the **training strategy**, enabling the model to consider correlations between *room type* and *surface type* when predicting disinfectant recommendations.

---

## 📊 Model Performance

### 🧴 Disinfectant Recommendation — RandomForestClassifier

The classifier determines the **most suitable disinfectant** based on detected germs and colony counts.

<p align="center">
  <img src="https://github.com/Iyed0092/Smart-Hygiene-Centre-National-de-Greffe-Tunis-/raw/main/assets/classifier%20disinfectants.png" width="600"/>
</p>
<p align="center"><em>Classification report showing F1-scores, precision, and recall for each disinfectant class.</em></p>

---

### 💧 Volume Prediction — RandomForestRegressor

The regressor predicts the **optimal volume of disinfectant** for each surface and germ type.

- **Erreur Quadratique Moyenne (EQM): 0.00043**  

---

## 🌐 Web Platform Features

- **User account management** (Flask + JWT Authentication)  
- **Messaging system** between lab personnel  
- **Chatbot assistant** presenting the centre and its services  
- **Interactive analytics dashboard** (React.js)  
- **RESTful API** for frontend-backend communication  

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React.js, Tailwind CSS |
| **Backend** | Flask, REST API, Spring Boot |
| **Machine Learning** | TensorFlow, Pandas, Scikit-learn, Matplotlib |
| **Database** | PostgreSQL |
| **Visualization** | Matplotlib, Plotly |

---
