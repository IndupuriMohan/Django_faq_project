# FAQ Project with Django API

## Overview
This is a multilingual FAQ web application built using **Django** and **Django REST Framework**. It provides a **RESTful API** that serves Frequently Asked Questions (FAQs) in multiple languages, including **English**, **Hindi**, and **Bengali**. The application includes features like efficient FAQ management, multilingual translation, caching, and a user-friendly Django Admin interface.

---

## Features

- **Multilingual API**: Fetch FAQs in English (default), Hindi, and Bengali.
- **Caching**: Efficient use of caching to store and retrieve FAQ data for better performance.
- **Django Admin**: Manage FAQs easily through Django’s built-in admin interface.
- **Django REST Framework**: Exposed API endpoints to handle FAQ data and translation.
- **Internationalization**: Support for different languages (English, Hindi, Bengali) with automatic translation.

---

## Requirements

To run this project, ensure the following are installed:

- **Python 3.8+**
- **Docker** (recommended for containerized setup)
- **Docker Compose**
- **Git** (for version control)

---

## Installation

### 1. **Clone the Repository**

Clone the repository to your local machine:

```
git clone https://github.com/IndupuriMohan/Django_faq_project.git
cd Django_faq_project
```

### 2. **Set Up Docker (Recommended)**

This project comes with **Docker** configuration. To run the app in a containerized environment:

```
docker-compose up --build
```

This will:
- Build and run the application in a **Docker container**.
- Install all dependencies.
- Start the app and expose it on **port 8000**.

### 3. **Local Setup (Without Docker)**

If you prefer to run the project locally, follow these steps:

#### **Create a Virtual Environment**:

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

#### **Install Dependencies**:

```
pip install -r requirements.txt
```

#### **Apply Database Migrations**:

```
python manage.py migrate
```

#### **Create a Superuser** (optional, for admin access):

```
python manage.py createsuperuser
```

#### **Run the Server**:

```
python manage.py runserver
```

---

## Access the Application

Once the server is running, visit the following URL in your browser:

```
http://127.0.0.1:8000/
```

---

## API Endpoints

The project exposes a **REST API** that can be used to fetch FAQs in different languages.

### **Fetch FAQs in English (default)**

```
curl http://127.0.0.1:8000/api/faqs/
```

### **Fetch FAQs in Hindi**

```
curl http://127.0.0.1:8000/api/faqs/?lang=hi
```

### **Fetch FAQs in Bengali**

```
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```

---

## Folder Structure

```
.
├── faq_project/                # Main project folder
│   ├── settings.py             # Django settings file
│   ├── urls.py                 # Project URL routing
│   ├── wsgi.py                 # WSGI entry point for deployments
├── faq/                        # FAQ app
│   ├── migrations/             # Database migration files
│   ├── models.py               # The FAQ model
│   ├── views.py                # API views for FAQ operations
│   ├── serializers.py          # Serializers to transform model data
│   ├── urls.py                 # URL routing for FAQ app
├── db.sqlite3                  # SQLite database file
├── Dockerfile                  # Docker configuration file
├── docker-compose.yml          # Docker Compose configuration
├── requirements.txt            # List of required Python dependencies
├── .gitignore                  # Git ignore file
├── manage.py                   # Django management script
```

---

## Running Tests

To run tests for the project:

```
docker-compose exec web python manage.py test  # For Docker
# Or if not using Docker, run:
python manage.py test
```

---

## Troubleshooting

If you encounter issues, here are some solutions:

- **Ensure dependencies are installed** by running `pip install -r requirements.txt` or using Docker.
- **Check Docker containers** using `docker ps` to ensure the container is running.
- **Rebuild Docker images** if needed:

```
docker-compose down
docker-compose up --build
```

---


