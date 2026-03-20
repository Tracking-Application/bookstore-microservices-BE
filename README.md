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

# 🧠 Microservice Rule

### Use this way to run

cd auth-service
``uvicorn main:app --port 8001``
cd product-service
``uvicorn main:app --port 8002``

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
# CI/CD: GitHub Actions -> EC2 Auto Deploy

This repository now includes a production deploy workflow:

- Workflow: `.github/workflows/deploy-ec2.yml`
- EC2 deploy script: `scripts/ec2-deploy.sh`

## What happens on push to `main`

1. GitHub Actions validates `docker-compose.yml`.
2. If valid, Actions connects to EC2 over SSH.
3. EC2 runs:
   - `git fetch / git pull` on `main`
   - `docker compose up -d --build --remove-orphans`

## Required GitHub Secrets

Add these in your repo: `Settings -> Secrets and variables -> Actions -> New repository secret`

- `EC2_HOST`: Public IP or DNS of your EC2
- `EC2_USER`: SSH user (usually `ubuntu` for Ubuntu AMI)
- `EC2_SSH_KEY`: Private key content (full PEM text)
- `EC2_PORT`: Usually `22`
- `EC2_APP_DIR`: Absolute path on EC2 (example: `/home/ubuntu/bookstore-microservices-BE`)
- `EC2_USE_SUDO_DOCKER`: `true` if your user needs sudo for docker, else `false`

## One-time EC2 setup

Run once on EC2:

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin git
sudo systemctl enable --now docker

# optional: run docker without sudo
sudo usermod -aG docker $USER
# log out and log back in after group change
```

Then clone repo once:

```bash
git clone <your-repo-url> /home/ubuntu/bookstore-microservices-BE
cd /home/ubuntu/bookstore-microservices-BE
```

Ensure your `docker-compose.yml` and env values are production-ready.

## Manual deploy trigger

You can also run deployment from GitHub Actions tab using `workflow_dispatch`.
