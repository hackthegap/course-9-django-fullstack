# Full-Stack Django Project

**Created by Fabricio Braga**  
**Last Updated: March 13, 2025**

---

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Accessing the Application](#accessing-the-application)
- [Contributing](#contributing)

---

## Introduction

This is a full-stack Django project that demonstrates how to set up a Django application using Docker. The project includes a basic Django app with models for `User` and `BankAccount`, a PostgreSQL database, and a simple web interface to display user data.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: [Download and install Docker](https://www.docker.com/).
- **Git**: [Download and install Git](https://git-scm.com/).

Verify your Docker installation by running:

```bash
docker --version
```

---

## Installation and Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/hackthegap/course-9-django-fullstack.git
cd course-9-django-fullstack
```

### 2. Create the Django Project and App

Run the following commands to create the Django project and app:

```bash
docker-compose run web django-admin startproject myproject .
docker-compose run web python manage.py startapp myapp
```

### 3. Update `settings.py`

Add `myapp` to the `INSTALLED_APPS` list in `myproject/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'myapp',
]
```

### 4. Define Models

Update `myapp/models.py` to define the `User` and `BankAccount` models:

```python
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Account {self.account_number} ({self.user})"
```

### 5. Register Models in Admin

Update `myapp/admin.py` to register the models in the Django admin interface:

```python
from django.contrib import admin
from .models import User, BankAccount

admin.site.register(User)
admin.site.register(BankAccount)
```

### 6. Configure Docker

#### Create a `Dockerfile`

Create a `Dockerfile` in the root of your project:

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/
```

#### Create a `docker-compose.yml` File

Create a `docker-compose.yml` file in the root of your project:

```yaml
version: '3.8'
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: myproject
      POSTGRES_USER: myprojectuser
      POSTGRES_PASSWORD: myprojectpassword
    volumes:
      - postgres_data:/var/lib/postgresql/data
volumes:
  postgres_data:
```

#### Create `requirements.txt`

Create a `requirements.txt` file in the root of your project:

```plaintext
Django==4.2
psycopg2-binary==2.9.6
```

---

## Running the Application

### 1. Build and Start the Containers

Run the following command to build and start the Docker containers:

```bash
docker-compose up --build
```

### 2. Apply Migrations

Apply the database migrations:

```bash
docker-compose exec web python manage.py migrate
```

### 3. Create a Superuser

Create a superuser to access the Django admin interface:

```bash
docker-compose exec web python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

---

## Accessing the Application

- **Django Admin Interface**: Visit `http://127.0.0.1:8000/admin` to access the Django admin interface.
- **Django App**: Visit `http://127.0.0.1:8000` to access the Django app.

---

## Project Structure

```
course-9-django-fullstack/
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── myapp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
├── templates/
│   └── myapp/
│       └── user_list.html
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md
```

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

---

Happy coding! 🚀