# Django Project Setup Guide

This guide provides instructions on how to set up the Django project on your local development environment.

## Pre-requisites

Before you begin, ensure you have the following installed:
- Git
- Python 3.x
- pip (Python package manager)
- Virtualenv (optional but recommended for creating isolated Python environments)

## 1. Clone the Project Repository

First, clone the project repository to your local machine and navigate to the project directory:

bash
git clone <Repository-URL>
cd <Project-Directory>


## 2. Set Up a Virtual Environment for python version 3.10

python3 -m venv .venv
source .venv/bin/activate


## 3. Install Project Dependencies

pip install -r requirements.txt


## 4. Set Up Environment Variables

Create a .env file in the project root directory. Populate it with the necessary environment variables as described in the project documentation or .env.example file, if provided.


## 5. Run Database Migrations

python manage.py migrate

## 6. Load Initial Data (Optional)

python manage.py loaddata data.json

python manage.py loaddata state_data.json

python manage.py loaddata language_data.json

## 7. Create a Superuser (Optional)

python manage.py createsuperuser

## 8. Add .env file
   Create a `.env` file in the root of the project with the following content. The URL (`http://localhost:3000`) can be changed based on your Django project URL:
   
   Copy contents from .env.example file.

## 9. Install Redis

brew install redis

## 10. Run Redis

redis-server

## 11. Run the Development Server

python manage.py runserver

## 12. If need to update translation file we can use:

https://www.ajexperience.com/po-translator/


