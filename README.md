Here is a complete, beginner-friendly DevOps project. This project demonstrates how to take a simple Python application, package it into a Docker container, and run it consistently across any environment.

---

### 1. Project Folder Structure

Before writing the code, let's look at how the files should be organized on your computer.

```text
flask-docker-app/
│
├── app.py                # The main Python Flask application
├── requirements.txt      # List of Python dependencies
├── Dockerfile            # Instructions to build the Docker image
├── .dockerignore         # Files to exclude from Docker (optional but recommended)
└── README.md             # Project documentation
```

---

### 2. Source Code

Create a folder named `flask-docker-app` and create the following files inside it.

#### File: `requirements.txt`
This file tells Python which libraries are needed.
```text
Flask==3.0.0
Werkzeug==3.0.1
```

#### File: `app.py`
This is the application logic. It includes logging, multiple routes, and a health check.

```python
# app.py
from flask import Flask, jsonify
import logging
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure Logging
# In production/Docker, logs should go to stdout so Docker can capture them.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 1. Home Page Route
@app.route('/')
def home():
    logger.info("Home page accessed.")
    return """
    <h1>Welcome to the Dockerized Flask App!</h1>
    <p>This is a simple beginner DevOps project.</p>
    <a href="/about">Go to About Page</a> | <a href="/health">Check Health</a>
    """

# 2. About Page Route
@app.route('/about')
def about():
    logger.info("About page accessed.")
    return """
    <h1>About This Project</h1>
    <p>This project demonstrates how to containerize a Python application.</p>
    <a href="/">Go back Home</a>
    """

# 3. Health Check API
# This is crucial for DevOps tools (like Kubernetes or Load Balancers) 
# to know if the app is still running correctly.
@app.route('/health')
def health():
    logger.info("Health check performed.")
    return jsonify({"status": "healthy", "message": "System is operational"}), 200

# Run the application
# host='0.0.0.0' is important! It makes the app accessible outside the container (not just localhost).
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

#### File: `Dockerfile`
This file contains the "recipe" to build the Docker image.

```dockerfile
# Use an official lightweight Python image
# "slim" variants are smaller and more secure for production
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (Caching layer)
# This is a best practice. If requirements.txt doesn't change, 
# Docker uses the cached layer, making builds faster.
COPY requirements.txt .

# Install dependencies
# --no-cache-dir keeps the image size small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create a non-root user to run the app
# This is a security best practice (Production Ready)
RUN useradd -m myuser
USER myuser

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
# "python" is the command, "app.py" is the argument
CMD ["python", "app.py"]
```

#### File: `.dockerignore`
This prevents unnecessary files from being copied into the Docker image, keeping it small and secure.

```text
.git
__pycache__
*.pyc
.env
Dockerfile
README.md
```

---

### 3. README.md

Here is the professional documentation for the project.

```markdown
# Dockerized Python Flask Web Application

A simple, production-ready beginner project demonstrating how to containerize a Python Flask web application using Docker.

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![Docker](https://img.shields.io/badge/Docker-Latest-blue.svg)

## 📋 Project Description

This project creates a web server with three main endpoints:
1. **Home Page**: A welcome screen.
2. **About Page**: Information about the project.
3. **Health Check**: A JSON endpoint used for monitoring the application's status.

The goal of this project is to teach the fundamentals of building Docker images and running containers.

## ✨ Features

- ✅ **Lightweight Image**: Uses `python:3.11-slim` for efficiency.
- ✅ **Security**: Runs as a non-root user.
- ✅ **Logging**: Configured to output logs to standard out (stdout) for container monitoring.
- ✅ **Health Check**: Dedicated `/health` endpoint.
- ✅ **Environment Flexibility**: Uses `0.0.0.0` host to allow external access.

## 🛠 Technologies Used

- **Language**: Python 3.11
- **Framework**: Flask
- **Containerization**: Docker
- **OS**: Linux (Alpine/Debian based)

## 🚀 Installation & Usage

### Prerequisites
- Docker installed on your machine.

### Steps

1. **Clone or Create the project folder.**

2. **Build the Docker Image:**
   Open your terminal in the project folder and run:
   ```bash
   docker build -t flask-app .
   ```

3. **Run the Docker Container:**
   ```bash
   docker run -d -p 5000:5000 --name my-flask-app flask-app
   ```

4. **Access the Application:**
   Open your browser and visit:
   - Home Page: `http://localhost:5000`
   - About Page: `http://localhost:5000/about`
   - Health API: `http://localhost:5000/health`

## 🐳 Docker Commands Reference

- **Build Image**: `docker build -t flask-app .`
- **Run Container**: `docker run -d -p 5000:5000 --name my-flask-app flask-app`
- **View Logs**: `docker logs my-flask-app`
- **Stop Container**: `docker stop my-flask-app`
- **Remove Container**: `docker rm my-flask-app`

## 📸 Screenshots

*Note: In a real repository, you would place actual images here.*

**1. Home Page**
> [Description: A browser window showing the Welcome message with links to About and Health check.]

**2. Health Check Output**
> [Description: JSON output displaying `{"status": "healthy", "message": "System is operational"}`.]

**3. Docker Terminal**
> [Description: Terminal showing the output of `docker logs` displaying timestamped access logs.]
```

---

### 4. Commands to Build and Run

Here are the exact commands you need to type in your terminal (inside the project folder):

**1. Build the Image:**
This command builds the image based on the Dockerfile. `-t flask-app` gives it a name.
```bash
docker build -t flask-app .
```

**2. Run the Container:**
This command runs the container in the background (`-d`) and maps port 5000 on your computer to port 5000 inside the container (`-p 5000:5000`).
```bash
docker run -d -p 5000:5000 --name my-flask-app flask-app
```

**3. Verify Logs:**
To see the application logs (proving the logging feature works):
```bash
docker logs my-flask-app
```

---

### 5. Explanation for Beginners

To help you understand what is happening under the hood, here is a simple explanation of the key components.

#### What is Flask?
Flask is a "micro-framework" for Python. It allows us to write code that listens for web requests (like when you type a URL in a browser) and sends back a response (HTML or JSON). In `app.py`, `@app.route('/')` tells Flask: "When someone visits the homepage, run this function."

#### What is a Dockerfile?
Think of a Dockerfile as a **recipe**.
1.  **`FROM python:3.11-slim`**: We start with a base. We are taking a lightweight Linux operating system that already has Python 3.11 installed. We don't have to install Python manually.
2.  **`WORKDIR /app`**: This tells Docker: "Once you are inside the container, go to the `/app` folder. Do all work there."
3.  **`COPY ...`**: This moves files from your computer into the container.
4.  **`RUN pip install ...`**: This is a command executed inside the container to install the libraries listed in `requirements.txt`.
5.  **`CMD ["python", "app.py"]`**: This is the command that starts the application. Once the container starts up, it runs this command immediately.

#### Why do we use `host='0.0.0.0'`?
By default, Python web apps only listen to `localhost` (inside the container). However, a Docker container is isolated. If you only listen to localhost inside the container, *you* (on your computer) cannot reach it.
By setting `host='0.0.0.0'`, we tell the app: "Listen on *every* available network interface inside this container." This allows Docker to route traffic from your computer's port 5000 to the app's port 5000.

#### Why use a non-root user?
In the Dockerfile, we created a user named `myuser`.
By default, Docker runs as `root` (the administrator). If a hacker breaks into your app, they have full control over the container. By switching to a non-root user, we limit the damage they can do. This is a standard "Production Ready" security practice.