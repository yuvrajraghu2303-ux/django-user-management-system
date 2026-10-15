# Django User Management System

A Django web application that uses MySQL to manage user records.

## Features

- Display a Hello World response.
- View all users in an HTML table.
- Add new users with name, email, and role.
- View individual user details.
- Validate form inputs and handle users that do not exist.

## Technologies Used

- Python
- Django
- MySQL
- HTML

## Setup and Installation

### 1. Clone the Repository

```bash
git clone -b steptech_assignment https://github.com/yuvrajraghu2303-ux/django-user-management-system.git
cd django-user-management-system/new_project/new_project
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install Django mysqlclient
```

### 4. Configure the Database

Install and start MySQL Server.

Create a MySQL database named `users` and ensure it contains a `users` table with these columns:

- `id`
- `name`
- `email`
- `role`

Configure your database connection in `new_project/settings.py` using your own MySQL credentials. Do not publish passwords or other sensitive credentials.

### 5. Run the Application

From the directory containing `manage.py`, execute:

```bash
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Application URLs

| URL | Description |
|---|---|
| `/hello/` | Display Hello World |
| `/users/` | Display all users |
| `/new_user/` | Add a new user |
| `/users/1/` | View details of user ID 1 |
| `/about/` | Display the About page |
