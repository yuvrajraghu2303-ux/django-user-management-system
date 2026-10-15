# Django User Management System

A Django web application that uses MySQL to manage user records.

## Features

- Display a Hello World response.
- View all users in an HTML table.
- Add new users with name, email, and role.
- View individual user details.
- Validate form inputs.
- Handle requests for users that do not exist.

## Technologies Used

- Python
- Django
- MySQL
- HTML

## Setup and Installation

### 1. Clone the Repository

Clone the assignment branch from GitHub:

```bash
git clone -b steptech_assignment https://github.com/yuvrajraghu2303-ux/django-user-management-system.git
```

Navigate to the directory containing `manage.py`:

```bash
cd django-user-management-system/new_project/new_project
```

### 2. System Requirements

The application requires:

- Python 3.12 or later
- MySQL Server
- pip
- Python virtual environment support

### 3. Install Additional System Dependencies

On Ubuntu, install the system packages required to build the MySQL Python connector:

```bash
sudo apt update
sudo apt install python3-venv python3-dev default-libmysqlclient-dev build-essential pkg-config
```

These packages provide the development headers and build tools that may be required to install `mysqlclient`.

If these packages are already installed, you do not need to install them again.

### 4. Create and Activate a Virtual Environment

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 5. Install Python Dependencies

Install Django and the MySQL database connector:

```bash
pip install "Django==6.1.2" mysqlclient
```

Make sure the virtual environment is activated before installing the dependencies.

## Database Setup

### 1. Configure the MySQL Database

Install and start MySQL Server.

Create a database named `users` and a table named `users`.

If the database and table do not already exist, execute the following SQL statements:

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

### 2. Database Schema

The `users` table contains the following columns:

| Column | Data Type | Description |
|---|---|---|
| `id` | INT, AUTO_INCREMENT | Unique identifier for each user and primary key |
| `name` | VARCHAR(100) | Name of the user |
| `email` | VARCHAR(150) | Email address of the user |
| `role` | VARCHAR(50) | Role assigned to the user |

The Django `User` model maps to the existing `users` table.

Because the model uses `managed = False`, Django does not create or manage this table through migrations. Create the table manually using the SQL statement above.

### 3. Populate the Database with Sample Data

Select the `users` database and insert sample records:

```sql
USE users;

INSERT INTO users (name, email, role)
VALUES
    ('Rahul Sharma', 'rahul.sharma@example.com', 'Developer'),
    ('Priya Verma', 'priya.verma@example.com', 'Designer'),
    ('Aman Singh', 'aman.singh@example.com', 'Tester');
```

Run this `INSERT` statement once to add the sample records. Running it repeatedly will create additional records.

### 4. Verify the Sample Data

To check that the records were inserted successfully, execute:

```sql
SELECT * FROM users;
```

The query displays the user IDs, names, email addresses, and roles stored in the database.

### 5. Configure the Django Database Connection

Open `new_project/settings.py` and configure the MySQL connection using your own database credentials.

Ensure that:

- The database name is `users`.
- The MySQL username and password are correct.
- The MySQL account has permission to access the database and table.
- MySQL Server is running.

**Security:** Do not publish database passwords or other sensitive credentials in your repository.

## Running the Application

From the directory containing `manage.py`, run:

```bash
python manage.py migrate
python manage.py runserver
```

The `migrate` command applies the migrations for Django-managed tables. It does not create the `users` table because the `User` model uses `managed = False`.

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

## Additional Notes

- Ensure MySQL Server is running before starting the Django application.
- Configure the database connection before running the application.
- Keep database credentials private.
- Activate the Python virtual environment whenever you work on the project.
