# django-navbar
Provides a navigation bar for django applications.

## Installation
```python
pip install django_custom_navbar
```
Run after installations or update `manage.py migrate`.

## Settings
```python
INSTALLED_APPS = [
  ...
  "django_navbar",
  ...
]
TEMPLATES = [
    {
        ...
        "OPTIONS": {
            "context_processors": [
                ...
                "django_navbar.context_processors.nav_bar",
                ...
            ],
        },
    },
]
```
