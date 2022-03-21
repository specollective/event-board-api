# Event Board

Boilerplate Django application for a community event board.

# Dependencies

- asgiref
- dj-database-url
- Django
- django-environ
- djangorestframework1
- gunicorn0
- psycopg2-binary
- sqlparse

# Getting started

Clone repository the git repository.
```
git clone git@github.com:specollective/event-board-api.git
cd event-board-api
```

# Development Environment (localhost)

1. Set up environment variables
```
cp .env.development .env
```

2. Set up python environment
```
python3 -m venv python-env
```

3. Active python environment
```
source python-env/bin/activate
```

4. Install dependencies
```
pip install -r requirements.txt
```

5. Migrate database
```
python manage.py migrate
```

6. Run tests
```
python manage.py test
```

7. Create a admin user
```
python manage.py createsuperuser --email example@example.com --username admin
```

8. Run server
```
python manage.py runserver
```

9. Visit http://localhost:8000/api/v1 to view Django REST framework graphical interface for the API.
