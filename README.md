# Django Blog Project

A backend blog application built with Django and Django REST Framework. This project provides a set of RESTful API endpoints for managing blog posts, as well as a landing page to display featured posts.

## Tech Stack

- **Framework**: Django 6.0
- **API**: Django REST Framework (DRF)
- **Database**: SQLite (Development) / PostgreSQL (Production ready via `dj-database-url`)
- **Static Files Management**: WhiteNoise
- **CORS**: django-cors-headers

## Features

- **Blog Posts Management**: Create, Read, Update, and Delete (CRUD) operations for blog posts.
- **Bulk Delete**: Ability to delete all posts at once.
- **Home View**: A server-rendered HTML page showing the latest featured posts and total post counts.
- **Production Ready**: Comes with a `build.sh` script and `Procfile` for easy deployment (e.g., Render, Heroku).

## Project Structure

```
d:/blog-django/
├── .venv/                   # Virtual environment
└── blog/
    ├── api/                 # Django app containing models, views, and serializers
    ├── mysite/              # Core Django project settings
    ├── manage.py            # Django command-line utility
    ├── requirements.txt     # Python dependencies
    ├── build.sh             # Deployment build script
    ├── Procfile             # Process file for deployment
    └── .env                 # Environment variables (ignored in version control)
```

## Setup Instructions

### 1. Clone the repository and navigate to the project directory

Ensure you are in the `blog/` folder where `manage.py` is located.

```bash
cd blog
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.

## Deployment

The project is pre-configured for deployment on platforms like Render or Heroku. 

1. Ensure the `DATABASE_URL` environment variable is set to your production database URL (e.g., PostgreSQL).
2. The `build.sh` script is provided to automate the build process:
   - Installs requirements
   - Collects static files using WhiteNoise
   - Runs database migrations

## API Endpoints Overview

- **`GET /`** - Renders the home page displaying featured posts.
- **`GET /api/posts/`** - Retrieves a list of all posts.
- **`POST /api/posts/`** - Creates a new post.
- **`DELETE /api/posts/`** - Deletes all posts.
- **`GET /api/posts/<id>/`** - Retrieves a specific post by ID.
- **`PUT/PATCH /api/posts/<id>/`** - Updates a specific post.
- **`DELETE /api/posts/<id>/`** - Deletes a specific post.

*(Note: Endpoint paths might vary based on your `urls.py` configuration.)*
