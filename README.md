# 🌿 AgriDoctor AI

AI-Powered Plant Disease Detection and Community Disease Intelligence Platform

---

## 📌 Overview

AgriDoctor AI is an intelligent plant disease detection platform that helps farmers identify crop diseases using deep learning and receive AI-generated treatment recommendations.

The system combines Computer Vision, Artificial Intelligence, Location Intelligence, and Community Disease Monitoring to create an early-warning ecosystem for agricultural disease outbreaks.

---

## 🚜 Problem Statement

Crop diseases cause significant agricultural losses worldwide. Farmers often struggle to:

* Identify diseases accurately
* Take preventive action quickly
* Access expert agricultural guidance
* Know about disease outbreaks in nearby areas

AgriDoctor AI addresses these challenges through automated disease detection and community-based disease intelligence.

---

## ✨ Features

### 🔍 Plant Disease Detection

* Upload a leaf image
* Deep Learning model predicts disease
* Confidence score displayed
* Supports multiple crop diseases

---

### 📚 Disease Knowledge Base

Provides:

* Disease description
* Symptoms
* Causes
* Organic treatment recommendations

---

### 🤖 AI Generated Reports

Automatically generates:

* Disease analysis
* Severity assessment
* Recommended actions
* Prevention strategies

---

### 👤 User Authentication

Powered by Supabase Authentication.

Features:

* User Registration
* Secure Login
* User Session Management
* Logout Functionality

---

### 📍 Location-Aware Profiles

During registration:

* User location is detected automatically
* State and district are stored
* Location data is linked to disease reports

---

### 📜 Prediction History

Users can:

* View previous disease reports
* Access AI-generated recommendations
* Track past predictions

---

### 📊 Community Dashboard

Visualizes:

* Most common diseases
* Disease frequency
* Community-level disease trends

---

### 🚨 Community Disease Alerts

The system monitors disease reports from nearby users.

When a disease exceeds a threshold count:

* Community alert is generated
* Nearby farmers are notified
* Early preventive action becomes possible

---

## 🏗️ System Architecture

```text
Leaf Image
    │
    ▼
Deep Learning Model
    │
    ▼
Disease Prediction
    │
    ├── Knowledge Base
    │
    ├── AI Report Generator
    │
    ├── Save Report (Supabase)
    │
    └── Community Alert Engine
            │
            ▼
    Location-Based Alerts
```

---

## 🛠️ Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* Supabase PostgreSQL

### Authentication

* Supabase Auth

### AI/ML

* TensorFlow
* Keras
* CNN Model

### Data Processing

* NumPy
* Pandas

### Visualization

* Plotly

### Image Processing

* Pillow (PIL)

### Geolocation

* Streamlit Geolocation
* Reverse Geocoding APIs

---

## 📂 Project Structure

```text
PLANT_DISEASE_DETECTION PROJECT/

├── .devcontainer/

├── dataset/
│   ├── test/
│   ├── train/
│   ├── valid/
│   └── disease_knowledge.json

├── docs/
│   └── classification_report.csv

├── models/
│   ├── trained_plant_disease_model.keras
│   └── training_history.json

├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_model_evaluation.ipynb

├── plant_disease_project_env/

├── src/
│   ├── alerts.py
│   ├── auth.py
│   ├── dashboard.py
│   ├── database.py
│   ├── geocoding.py
│   ├── history.py
│   ├── knowledge_base.py
│   ├── llm_report.py
│   ├── location.py
│   ├── logger.py
│   ├── predict.py
│   ├── profile.py
│   ├── reports.py
│   └── __init__.py

├── tests/

├── webapp/
│   ├── __pycache__/
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── alerts.py
│   │   ├── header.py
│   │   └── sidebar.py
│   │
│   ├── views/
│   │   ├── __init__.py
│   │   ├── auth_page.py
│   │   ├── dashboard_page.py
│   │   ├── detection_page.py
│   │   └── history_page.py
│   │
│   ├── __init__.py
│   └── app.py

├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── runtime.txt
```

---

## 🗄️ Database Schema

### user_profiles

```sql
create table user_profiles (
    id uuid primary key references auth.users(id) on delete cascade,
    email text,
    state text,
    district text,
    latitude double precision,
    longitude double precision,
    created_at timestamptz default now()
);
```

---

### disease_reports

```sql
create table disease_reports (
    id bigint generated always as identity primary key,
    user_id uuid references auth.users(id),
    disease_name text,
    confidence float,
    report text,
    state text,
    district text,
    latitude double precision,
    longitude double precision,
    created_at timestamptz default now()
);
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Gobinda03/Plant_Disease_Detection
cd Plant_Disease_Detection
```

### Create Virtual Environment

```bash
python -m venv plant_disease_project_env
```

### Activate Environment

Windows:

```bash
plant_disease_project_env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
GROK_API_KEY=your_grok_api_key
```

---

## ▶️ Run Application

```bash
streamlit run webapp/app.py
```

---

## 📈 Current Progress


* Plant Disease Detection
* Disease Information System
* AI Report Generation
* Supabase Integration
* Prediction History
* Dashboard Analytics
* Community Alert Framework
* User Authentication
* User Profiles
* Auto Location Detection
* Location-Aware Disease Reports

---

## 🚀 Future Enhancements

### 🔥 Planned Features

#### Multilingual Support

Support for:

* English
* Hindi
* Bengali
* Tamil
* Telugu

---

#### Advanced Disease Alerts

* District-wise alerts
* State-wise disease heatmaps
* Real-time outbreak monitoring

---

#### Model Improvements

* Higher accuracy CNN
* Transfer Learning
* EfficientNet
* MobileNetV3

---

#### Mobile Application

* Flutter Frontend
* Android Deployment
* Offline Predictions

---

#### Farmer Community Network

* Disease reporting
* Discussion forums
* Agricultural expert support

---

## 📊 Expected Impact

AgriDoctor AI aims to:

* Reduce crop losses
* Improve disease awareness
* Enable early disease intervention
* Provide accessible AI-powered agricultural assistance

---

## 👨‍💻 Developer

**Gobinda Hazra**

Software Engineering Student

Passionate about AI, Machine Learning, Agriculture Technology, and Full-Stack Development.

---

## 📄 License

This project is developed for educational and research purposes.
