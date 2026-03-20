# 📚 Bookstore Microservices Application

## 🏗️ Architecture Overview

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/45f0a4a7-26b5-41e4-985a-b2e4e35e0b0b" />


This project is a **Microservices-based Bookstore Application** with:

* **Frontend (React)**

  * Admin App
  * Customer App
* **Backend (FastAPI Microservices)**

  * Auth Service
  * Product Service
  * Order Service
  * Tracking Service
* **Database**

  * PostgreSQL (Single Shared DB)

---

# 📦 Repositories

You have **2 repositories**:

### 1️⃣ Backend

```
bookstore-microservices-BE
```

### 2️⃣ Frontend

```
bookstore-microservices-FE
```

---

# 🚀 EC2 SETUP (FIRST TIME)

## ✅ Step 1: Launch EC2 Instance

Use:

* Amazon Linux 2023
* t2.micro / t3.micro (free tier)

---

## ✅ Step 2: Install Required Tools

```bash
sudo dnf update -y

# Install Docker
sudo dnf install docker -y
sudo systemctl start docker
sudo systemctl enable docker

# Give permission
sudo usermod -aG docker ec2-user
newgrp docker

# Install Git
sudo dnf install git -y

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-linux-x86_64" \
-o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

---

# ⚙️ BACKEND SETUP

## ✅ Step 1: Clone Backend Repo

```bash
git clone <your-backend-repo-url>
cd bookstore-microservices-BE
ls
```

---

## ✅ Step 2: Run Docker Compose

```bash
docker-compose up -d --build
```

---

## ✅ Step 3: Verify Running Containers

```bash
docker ps
```

You should see:

```
auth-service        --> 8001
products-service    --> 8002
order-service       --> 8003
tracking-service    --> 8004
postgres            --> 5432
```

---

## 🌐 Backend URLs

| Service          | URL                  |
| ---------------- | -------------------- |
| Auth Service     | http://<EC2-IP>:8001 |
| Product Service  | http://<EC2-IP>:8002 |
| Order Service    | http://<EC2-IP>:8003 |
| Tracking Service | http://<EC2-IP>:8004 |

---

# 🎨 FRONTEND SETUP

## ✅ Step 1: Clone Frontend Repo

```bash
git clone <your-frontend-repo-url>
cd bookstore-microservices-FE
```

---

## ✅ Step 2: Configure Admin App

```bash
cd tracking_admin
ls -la
vi .env
```

Update:

```env
VITE_AUTH_API_URL=http://<EC2-IP>:8001
VITE_PRODUCT_API_URL=http://<EC2-IP>:8002
VITE_ORDER_API_URL=http://<EC2-IP>:8003
VITE_TRACKING_API_URL=http://<EC2-IP>:8004
VITE_USER_API_URL=http://<EC2-IP>:8001
```

Save:

```
:wq!
```

---

## ✅ Step 3: Configure Customer App

```bash
cd ../tracking_customer
ls -la
vi .env
```

Update:

```env
VITE_AUTH_API_URL=http://<EC2-IP>:8001
VITE_PRODUCT_API_URL=http://<EC2-IP>:8002
VITE_ORDER_API_URL=http://<EC2-IP>:8003
VITE_TRACKING_API_URL=http://<EC2-IP>:8004
VITE_USER_API_URL=http://<EC2-IP>:8001
```

Save:

```
:wq!
```

---

## ✅ Step 4: Run Frontend

```bash
cd ..
docker-compose up -d --build
```

---

# 🌐 Frontend URLs

| App          | URL                  |
| ------------ | -------------------- |
| Admin App    | http://<EC2-IP>:5173 |
| Customer App | http://<EC2-IP>:5174 |

---

# 👤 APPLICATION FLOW

## 🔐 Admin Flow

1. Open:

```
http://<EC2-IP>:5173
```

2. Click **Signup**
3. Select **Admin**
4. Enter Secret Code:

```
#12345
```

5. Register & Login

---

## 🛒 Customer Flow

1. Open:

```
http://<EC2-IP>:5174
```

2. Click **User Register**
3. Login
4. Browse products
5. Place orders
6. Track orders

---

# 🐳 Docker Commands (Useful)

### View containers

```bash
docker ps
```

### View logs

```bash
docker logs <container_name>
```

### Stop all

```bash
docker-compose down
```

### Rebuild

```bash
docker-compose up -d --build
```

---

# 🧠 Architecture Notes

* All **4 microservices run independently**
* All connect to **single PostgreSQL database**
* Services communicate via **API calls (not DB joins)**
* Frontend uses **environment variables** to call APIs

---

# ✅ Final Result

✔ Backend running (4 services)
✔ Frontend running (Admin + Customer)
✔ Connected via API Gateway logic
✔ Deployed on EC2 using Docker

---

# 🎯 Next Improvements

* Add API Gateway (Nginx / Kong)
* Use AWS RDS instead of local Postgres
* Use S3 + CloudFront for frontend
* Add CI/CD pipeline (GitHub Actions)

---

🔥 Your project is now **production-ready microservices architecture** 🚀
