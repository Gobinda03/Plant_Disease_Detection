# 🌿 AgriDoctor AI

AI-powered Plant Disease Detection and Community Alert System built with Streamlit, TensorFlow, Supabase, and Generative AI.

---

## 📖 Overview

AgriDoctor AI is an intelligent agricultural assistance platform that helps farmers and gardeners identify plant diseases from leaf images, receive treatment recommendations, generate AI-powered reports, and stay informed about disease outbreaks occurring nearby.

The platform combines Computer Vision, Generative AI, Geolocation Services, and Community Intelligence to create a smarter and more proactive plant health monitoring system.

---

## 🚀 Key Features

### 🌱 Plant Disease Detection

* Upload a plant leaf image
* Detect plant diseases using a trained deep learning model
* View prediction confidence scores
* Support for multiple plant disease classes

---

### 📚 Disease Knowledge Base

For every detected disease:

* Disease description
* Symptoms
* Causes
* Organic treatment recommendations

---

### 🤖 AI Generated Reports

Generate detailed disease reports using Generative AI.

Reports include:

* Disease analysis
* Severity assessment
* Treatment recommendations
* Prevention guidelines

All reports are automatically stored for future reference.

---

### 📍 Location-Aware User Profiles

During registration:

* Automatic location detection
* State and district extraction
* Manual location correction option
* Location stored securely in Supabase

Stored profile information:

* Email
* State
* District
* Latitude
* Longitude

---

### 🚨 Community Disease Alerts

AgriDoctor AI continuously analyzes disease reports submitted by users.

When disease cases exceed predefined thresholds in a district:

| Alert Level | Cases |
| ----------- | ----- |
| Warning     | 5+    |
| High Risk   | 15+   |
| Outbreak    | 30+   |

Users receive real-time outbreak notifications for their region.

---

### 📜 Prediction History

Users can view:

* Previously detected diseases
* Confidence scores
* AI generated reports
* Report timestamps

---

### 🔐 Authentication System

Powered by Supabase Authentication.

Features:

* User Registration
* User Login
* Session Management
* Secure Authentication

---

### 📊 Logging System

Every major action is logged:

* Sign Up
* Login
* Disease Detection
* Report Generation
* Profile Creation
* Community Alerts

Useful for debugging and monitoring.

---

## 🏗️ System Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ├── Authentication
 │       │
 │       ▼
 │   Supabase Auth
 │
 ├── Location Detection
 │       │
 │       ▼
 │   User Profiles
 │
 ├── Disease Detection
 │       │
 │       ▼
 │   TensorFlow Model
 │
 ├── Knowledge Base
 │
 ├── AI Report Generator
 │
 └── Community Alert Engine
         │
         ▼
      Supabase Database
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

### Machine Learning

* TensorFlow
* Keras

### AI Reports

* Google Gemini API

### Geolocation

* streamlit-geolocation
* Reverse Geocoding API

### Image Processing

* Pillow
* NumPy

---

## 📂 Project Structure

```text
Plant_Disease_Detection/
│
├── models/
│   └── training_history.json
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_model_evaluation.ipynb
│
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
│   └── reports.py
│
├── webapp/
│   ├── app.py
│   │
│   ├── components/
│   │   ├── auth_guard.py
│   │   ├── header.py
│   │   └── sidebar.py
│   │
│   └── views/
│       ├── auth_page.py
│       ├── dashboard_page.py
│       ├── detection_page.py
│       └── history_page.py
│
├── .env
├── .gitignore
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Gobinda03/Plant_Disease_Detection.git

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

Linux/Mac:

```bash
source plant_disease_project_env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
SUPABASE_URL=YOUR_SUPABASE_URL

SUPABASE_KEY=YOUR_SUPABASE_ANON_KEY

GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## ▶️ Run Application

```bash
streamlit run webapp/app.py
```

---

## 🗄️ Database Tables

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
    confidence numeric,
    report text,
    state text,
    district text,
    latitude double precision,
    longitude double precision,
    created_at timestamptz default now()
);
```

---

## 🚨 Community Alert Logic

Alerts are generated using reports submitted during the last 7 days.

```text
5+ reports     → Warning

15+ reports    → High Risk

30+ reports    → Outbreak
```

Alerts are displayed only for the user's district.

---

## 🔮 Future Enhancements

* Radius-based outbreak detection
* Push notifications
* Email alerts
* Multilingual support
* Farmer discussion forum
* Mobile application
* Crop recommendation engine
* Weather integration
* Disease trend analytics
* Interactive outbreak map

---

## 👨‍💻 Author

Gobinda Hazra

B.Tech Information Technology

Narula Institute of Technology

GitHub:
https://github.com/Gobinda03

---

## 📄 License

This project is intended for educational, research, and portfolio purposes.
