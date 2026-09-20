# Library Management System

A Django-based library management application for managing books, users, withdrawals, and returns.

## Overview

This project allows:
- Admins to add books and monitor active withdrawals
- Users to register and log in
- Users to borrow available books
- Admins to process book returns and update inventory automatically
- Book cover images and document uploads to be stored in media folders

It is built with Django and uses MySQL for persistence.

## Features

- Book catalog listing with stock availability
- User registration and authentication
- Admin authentication
- Book issue workflow with a return deadline
- Return processing and inventory restoration
- Live admin dashboard for active withdrawals
- File and image upload support for books
- Basic Django message-based feedback for user/admin actions

## Project Structure

```text
library-management-system/
├── Project21/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── media/
│   ├── documents/
│   └── images/
├── static/
│   └── css/
├── templates/
│   ├── admin_dashboard.html
│   ├── booktemp.html
│   ├── index.html
│   ├── login.html
│   └── register.html
├── manage.py
├── requirements.txt
└── README.md
```

## Tech Stack

- Django 6.0.6
- Python 3
- MySQL
- Pillow
- HTML and CSS templates

## Prerequisites

Before running the application, make sure you have:

- Python installed
- MySQL server running
- A MySQL database named `BookManagementdb`
- `pip` available for installing dependencies

## Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/beheragit/library-management-system.git
cd library-management-system
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure your database settings

Update the database settings in `Project21/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'BookManagementdb',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Start the server

```bash
python manage.py runserver
```

Open the app in your browser at:

```text
http://127.0.0.1:8000/
```

## Main Features by Role

### User
- Register an account at `/register/`
- Log in at `/user-login/`
- View available books on the home page
- Withdraw a book if copies are available

### Admin
- Log in at `/admin-login/`
- Add books via the admin interface
- View active withdrawal records
- Mark books as returned and restore inventory

## Application Routes

- `/` — Home page and catalog
- `/register/` — User registration
- `/user-login/` — User login
- `/admin-login/` — Admin login
- `/createbook/` — Add a new book (admin only)
- `/admin-dashboard/` — Admin dashboard for active issues
- `/withdraw/<book_id>/` — Withdraw a book
- `/return/<issue_id>/` — Process a return
- `/logout/` — Log out

## Models

The project includes these models:

- `Book` — stores book details like title, author, cover image, attached document, and available copies
- `AdminModel` — admin authentication model
- `UserModel` — student/user information and login credentials
- `IssuedBook` — tracks who borrowed a book, when it was issued, its return date, and whether it has been returned

## Important Notes

- Uploaded media files are stored in the `media/` directory.
- CSS and static assets are stored under `static/`.
- Templates are located under `templates/`.
- The project uses custom authentication models instead of Django’s default user system.
- Admin credentials are not auto-created, so the admin user must be added manually or via the database.

## Troubleshooting

If you encounter issues:

- Verify MySQL is running
- Confirm the database `BookManagementdb` exists
- Check that the credentials in `Project21/settings.py` are correct
- Run:

```bash
python manage.py check
```

## License

This project does not currently include a license file. Please confirm usage rights before redistributing or publishing it.

## Repository Maintainer

- `beheragit`
