# 📝 Simple Note App (Streamlit + PostgreSQL + Docker + Kubernetes)

A minimal note-taking web application built with **Streamlit**, backed by **PostgreSQL**, containerized with **Docker**, and deployed on **Kubernetes via Minikube**.

---

## ✨ Features

- Add & delete simple notes via web UI
- Data persisted using PostgreSQL
- Visualize and manage database using DBeaver
- Fully containerized for reproducibility
- Kubernetes manifests ready for deployment on Minikube

---

## 📁 Project Structure

```
simple-note-app/
├── app/                     # Streamlit application
│   ├── main.py              # Main Streamlit app
│   └── db.py                # PostgreSQL connection logic
├── k8s/                     # Kubernetes manifests
│   ├── app-deployment.yaml
│   ├── app-service.yaml
│   ├── db-deployment.yaml
│   └── db-service.yaml
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## 🔧 Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/YannawutRoumsuk/simple-note-app.git
cd simple-note-app
```

### 2. Create `.env` (Optional)
If needed, create `.env` file to store environment variables.

### 3. Install dependencies (for local testing)

```bash
pip install -r requirements.txt
```

---

## 🐳 Run with Docker Compose (Local Dev)

```bash
docker-compose up --build
```

Access the app at: [http://localhost:8501](http://localhost:8501)

---

## 🐳 Build & Push Docker Image to Docker Hub

```bash
# Build
docker build -t yannawutz/note-app:latest .

# Push
docker push yannawutz/note-app:latest
```

> Replace `yannawutz` with your Docker Hub username.

---

## ☸️ Deploy to Minikube (Kubernetes)

### 1. Start Minikube with Docker driver

```bash
minikube start --driver=docker
```

### 2. Apply all Kubernetes manifests

```bash
kubectl apply -f k8s/
```

### 3. Access the app

```bash
minikube service note-app-service
```

---

## 🧠 Database Access with DBeaver

Use these credentials to connect to PostgreSQL from DBeaver:

- **Host**: `localhost`
- **Port**: `5432`
- **Database**: `notesdb`
- **User**: `postgres`
- **Password**: `postgres`

---

## ⚙️ Environment Variables

The application reads the DB host from an environment variable `DB_HOST`. You can configure it per environment:

- For Kubernetes: `DB_HOST=postgres`
- For Docker Compose: `DB_HOST=db` or leave it blank (default fallback)

---

## 📸 Screenshots

![alt text](image.png)

---

## 👨‍💻 Author

[Yannawut Roumsuk](https://github.com/YannawutRoumsuk)

---

## 📜 License

MIT License - free for personal and commercial use.

---

## ⭐️ Show Some Love

If you found this useful, please star the repository 🙌