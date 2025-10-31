# 🧫 Smart Hygiene — Centre National de Greffe, Tunis  
**Jan – May 2025 | TensorFlow · Random Forest · Flask · React.js 

---

## 💡 Project Overview

**Smart Hygiene** is an intelligent system developed for the **Centre National de Greffe, Tunis**, aimed at **optimizing disinfectant usage** and improving hygiene protocols through **AI-driven predictions**.

The platform integrates **machine learning**, **web development** to deliver a scalable solution that assists medical staff in:
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

## 🧩 Data Exploration & Clustering Analysis

Before building predictive models, we performed **unsupervised clustering** to better understand the structure of our hygiene data.

### 🧪 Cabine Similarity Analysis
The **Centre National de Greffe** operates numerous rooms and cabins (e.g., *Cabine 1, Cabine 2, Chambre Lyma, Chambre Trabelsi,* etc.).  
We used the **Silhouette Method** to determine the optimal number of clusters and to **group cabins with similar germ patterns and colony counts**.

<img src="https://raw.githubusercontent.com/yourusername/smart-hygiene/main/plots/silhouette_cabines.png" width="500"/>
<p align="center"><em>Silhouette plot for cabine clustering — identifying similar contamination profiles.</em></p>

### 🪑 Furniture Grouping Analysis
A similar clustering approach was applied to the **furniture items** present in each cabin —  
for instance, *chaise, chaise percée, dessus éclairage, interphone, lit, matelas, lavabo,* etc.  
This helped group **furniture pieces that tend to harbor similar types of germs**.

<img src="https://raw.githubusercontent.com/yourusername/smart-hygiene/main/plots/silhouette_furniture.png" width="500"/>
<p align="center"><em>Silhouette plot for furniture clustering — identifying contamination patterns by object type.</em></p>

These insights helped refine the **training strategy**, enabling the model to consider contextual correlations between *room type* and *surface type* when predicting disinfectant recommendations.

---

## 📊 Model Performance

### 🧴 Disinfectant Recommendation — RandomForestClassifier

The Random Forest classifier was used to determine the **most suitable disinfectant** based on detected germ species and colony counts.

<img src="https://github.com/Iyed0092/Smart-Hygiene-Centre-National-de-Greffe-Tunis-/raw/main/assets/classifier%20disinfectants.png" width="500"/>
<p align="center"><em>Classification report showing F1-scores, precision, and recall for each disinfectant class.</em></p>


---

### 💧 Volume Prediction — RandomForestRegressor

The final regressor predicts the **optimal volume of disinfectant** to be used for each surface and germ type.

- Obtained an **Erreur Quadratique Moyenne (EQM)** of **0.00043**,  
  indicating highly precise predictions of the required disinfectant volume.  
- The low error confirms the model’s suitability for real-world dosage optimization.

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
| **Machine Learning** | TensorFlow, Pandas, Matplotlib, Sci-kit learn, |
| **Database** | PostgreSQL |
| **Visualization** | Matplotlib, Plotly |

---

