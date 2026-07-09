# 🌿 KrishiNetra

**An Intelligent Crop Health Monitoring and Region-Based Disease Alert System for Smart Agriculture**

KrishiNetra is a deep learning-based web application that helps farmers, gardeners, and researchers identify plant diseases from leaf images. The platform combines Computer Vision, Artificial Intelligence, and a curated agricultural knowledge base to provide accurate disease diagnosis, treatment recommendations, and AI-generated reports.

The project is developed as both a research contribution and a portfolio project, focusing on practical deployment and real-world usability.

---

## ✨ Features

### 🌿 Leaf Validation

Before disease detection, every uploaded image is verified using a dedicated **Leaf Validator Model**.

This prevents:
- Random objects
- Furniture
- Human faces

from being classified as plant diseases.

Only valid plant leaf images are passed to the disease classifier.

---

### 🔍 Plant Disease Detection

- MobileNetV2-based CNN model
- Detects diseases from plant leaf images
- Supports **38 plant disease classes**
- Displays prediction confidence score

---

### 📚 Disease Knowledge Base

Each detected disease includes:

- Description
- Symptoms
- Possible causes
- Prevention methods
- Organic treatment recommendations

---

### 🤖 AI Disease Report

Generate a detailed report using **GROQ**.

Reports include:

- Disease explanation
- Severity analysis
- Organic treatment
- Prevention advice

Reports are automatically saved.

---

--- 
### 🚨 Community Disease Alerts 

## KrishiNetra continuously analyzes disease reports submitted by users. 

When disease cases exceed predefined thresholds in a district: 
| Alert Level   | Cases | 
| ------------- | ----- | 
| Warning       | 5+    | 
| High Risk     | 15+   | 
| Outbreak      | 30+   | 

Users receive real-time outbreak notifications for their region. 
---

### 📊 Prediction History

Users can review:

- Previous predictions
- Confidence scores
- Generated reports
- Detection timestamps

---

### 🔐 Authentication

Powered by **Supabase Authentication**

- User Registration
- Login
- Secure Sessions

---

### 📍 User Profile

Automatically stores:

- Email
- State
- District
- Latitude
- Longitude

using Supabase.

---

## 🛠 Technology Stack

**Frontend**
- Streamlit

**Backend**
- Python

**Machine Learning**
- TensorFlow
- Keras
- MobileNetV2

**Database**
- Supabase PostgreSQL

**Authentication**
- Supabase Auth

**Generative AI**
- Google GROQ API

**Image Processing**
- Pillow
- NumPy


## ⚙️ Installation 

### Clone Repository
bash
git clone https://github.com/Gobinda03/Plant_Disease_Detection.git

cd Plant_Disease_Detection
### Create Virtual Environment
bash
python -m venv plant_disease_project_env
### Activate Environment Windows:
bash
plant_disease_project_env\Scripts\activate
Linux/Mac:
bash
source plant_disease_project_env/bin/activate
### Install Dependencies
bash
pip install -r requirements.txt
---

## 🔑 Environment Variables

Create a .env file:
```env
SUPABASE_URL=YOUR_SUPABASE_URL

SUPABASE_KEY=YOUR_SUPABASE_ANON_KEY

GROQ_API_KEY=YOUR_GROQ_API_KEY
```

## 📖 Research Contribution

KrishiNetra introduces a practical disease diagnosis pipeline consisting of:

1. Leaf Validation Model
2. Plant Disease Classification
3. Agricultural Knowledge Base
4. AI-powered Disease Report Generation

The additional Leaf Validation stage significantly reduces false predictions on non-leaf images, making the system more reliable for real-world deployment.

--- 
## 👨‍💻 Author 
Gobinda Hazra B.Tech Information Technology Narula Institute of Technology 

GitHub: https://github.com/Gobinda03 
--- 

## 📄 License 
This project is intended for educational, research, and portfolio purposes. modify this correctl