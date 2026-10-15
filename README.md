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
```

Navigate to the directory containing `manage.py`:

```bash
cd django-user-management-system/new_project/new_project
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install Django mysqlclient
```

### 4. Configure the MySQL Database

Install and start MySQL Server.

Create a database named `users` and a table named `users` with the following columns:

- `id`
- `name`
- `email`
- `role`

If the database and table do not already exist, you can create them using:

```sql
CREATE DATABASE IF NOT EXISTS users;

USE users;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    role VARCHAR(50) NOT NULL
);
```
### Database Schema

The `users` table contains the following columns:

| Column | Data Type | Description |
|---|---|---|
| `id` | INT, AUTO_INCREMENT | Unique identifier for each user |
| `name` | VARCHAR(100) | User's name |
| `email` | VARCHAR(150) | User's email address |
| `role` | VARCHAR(50) | User's role |

### Populate the Database with Sample Data

Insert sample users using the following SQL statement:

```sql
INSERT INTO users (name, email, role)
VALUES
    ('Rahul Sharma', 'rahul.sharma@example.com', 'Developer'),
    ('Priya Verma', 'priya.verma@example.com', 'Designer'),
    ('Aman Singh', 'aman.singh@example.com', 'Tester');
```

Run this SQL statement once to add the sample records.

To verify that the records were inserted successfully, run:

```sql
SELECT * FROM users;
```

Configure the MySQL database connection in `new_project/settings.py` using your own database credentials.

**Security:** Do not publish database passwords or other sensitive credentials.

### 5. Run the Application

From the directory containing `manage.py`, execute:

```bash
python manage.py migrate
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

## Application URLs

| URL | Description |
|---|---|
| `/hello/` | Display Hello World |
| `/users/` | Display all users |
| `/new_user/` | Add a new user |
| `/users/1/` | View details of user ID 1 |
| `/about/` | Display the About page |
