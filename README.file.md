# 🚀 Dockerized Flask App

A simple Python Flask web application containerized using Docker.

## 📌 Project Overview
This project demonstrates how to containerize a basic Flask web app using Docker.  
The app prints **"Hello from Docker!"** when accessed through a browser.

## 🧩 Project Structure
```
app.py              → Flask application  
requirements.txt    → Dependencies list  
Dockerfile          → Docker build configuration  
```

## ⚙️ How to Run
### Step 1: Build Docker Image
```bash
docker build -t flask-docker-app .
```
### Step 2: Run Container
```bash
docker run -d -p 5001:5001 flask-docker-app
```
### Step 3: Open in Browser
Go to 👉 **http://localhost:5001**  
You should see:  
> **Hello from Docker!**

## 🛠️ Common Issues & Fixes
- **Port already in use:** Stop other containers or change port number.
- **Invalid reference format:** Remove extra spaces when building image name.
- **Dependency errors:** Ensure `requirements.txt` contains `flask`.

## 🚀 Future Enhancements
- Add multiple routes and HTML templates.  
- Integrate a small database (SQLite/MySQL).  
- Use Docker Compose for multi-container setup.  
- Deploy on AWS or Heroku.


