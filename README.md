# 🛒 Tracking Application – Microservices Architecture

This project is a microservices-based e-commerce tracking system built using FastAPI, PostgreSQL, and Docker.

---

# 🏗 Architecture Overview

This application is split into 4 independent services:

1. Auth Service
2. Product Service
3. Order Service
4. Tracking Service

Each service:
- Has its own models
- Has its own database folder
- Has its own .env
- Has its own requirements.txt
- Runs independently

---

# 📂 Project Structure

tracking/
│
├── auth-service/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── utils/
│   ├── main.py
│   ├── .env
│   └── requirements.txt
│
├── product-service/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── main.py
│   ├── .env
│   └── requirements.txt
│
├── order-service/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── main.py
│   ├── .env
│   └── requirements.txt
│
├── tracking-service/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── main.py
│   ├── .env
│   └── requirements.txt
│
└── README.md
