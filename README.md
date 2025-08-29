# Travel Booking Application

## Overview

The **Travel Booking Application** is a web app built with **Python (Django)**. It allows users to register, log in, and manage their profiles, browse travel options (Flights, Trains, Buses), book tickets, and view or cancel bookings. The project uses **Django templates** for frontend, **SQLite (default)** for data storage, and supports extension with MySQL.

---

## Features

* **User Authentication:** Register, login, logout, and manage user profiles.
* **Travel Options Management:** Browse available travel options with details like type, source, destination, date, time, price, and seats.
* **Booking System:** Book tickets, confirm reservations, and manage seats.
* **Manage Bookings:** View current/past bookings, cancel or update reservations.
* **Admin Panel:** Manage users, travel options, and bookings via Django Admin.
* **Responsive UI:** Clean, mobile-friendly interface built using Django templates and Bootstrap.

---

## Technologies Used

* **Backend:** Django (Python)
* **Frontend:** Django Templates, Bootstrap, CSS
* **Database:** SQLite (default) / MySQL (optional)
* **Other Tools:** Django Admin, Django Authentication System

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/travel_booking_app.git
cd travel_booking_app
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

Run migrations to create database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

> This project uses `db.sqlite3` as the built-in database.

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

Use these demo credentials:

* **Username:** admin
* **Email:** [admin@gmail.com](mailto:admin@gmail.com)
* **Password:** admin@12

### 6. Run Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Usage

* Register or log in using your credentials.
* Redirects to the **Home Page** where you can:

  * View available travel options (Flight, Train, Bus)
  * Book tickets and manage bookings
  * Cancel or update bookings
* Access the **Admin Panel** at `/admin`.

---

## API Endpoints

> These endpoints assume you expose RESTful APIs in your `urls.py` using Django views or Django REST Framework (DRF).

### 1. User Authentication

* **POST** `/api/register/` → Register a new user
* **POST** `/api/login/` → Login user
* **POST** `/api/logout/` → Logout user
* **PUT** `/api/profile/` → Update user profile

### 2. Travel Options

* **GET** `/api/travel-options/` → List all travel options
* **GET** `/api/travel-options/<id>/` → Get details of a travel option
* **POST** `/api/travel-options/` → Add a new travel option (Admin only)
* **PUT** `/api/travel-options/<id>/` → Update a travel option (Admin only)
* **DELETE** `/api/travel-options/<id>/` → Delete a travel option (Admin only)

### 3. Bookings

* **POST** `/api/bookings/` → Create a new booking
* **GET** `/api/bookings/` → View all bookings of logged-in user
* **GET** `/api/bookings/<id>/` → View details of a booking
* **PUT** `/api/bookings/<id>/cancel/` → Cancel a booking
* **DELETE** `/api/bookings/<id>/` → Delete a booking (Admin only)

---

## Running Tests

Unit tests are located in:

```
travel_booking_app/booking_app/tests.py
```

Run tests:

```bash
python manage.py test
```

---

## Directory Structure

```
travel_booking_app/
│
├── db.sqlite3              # Default SQLite database
├── manage.py               # Django project manager
├── requirements.txt        # Dependencies
│
├── booking_app/            # Core application
│   ├── models.py           # Travel & Booking models
│   ├── views.py            # Request handlers
│   ├── urls.py             # App-level routes
│   ├── forms.py            # User input forms
│   ├── admin.py            # Admin panel config
│   ├── tests.py            # Unit tests
│   └── templates/          # HTML templates
│
└── travel_booking_app/     # Project settings
    ├── settings.py         # Django settings
    ├── urls.py             # Project routes
    ├── wsgi.py             # WSGI configuration
    └── asgi.py             # ASGI configuration
```

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to branch (`git push origin feature/new-feature`)
5. Open a pull request

---

## License

This project is licensed under the **MIT License**.

---

## Acknowledgments

Special thanks to the following technologies and resources:

* **Django** – Backend framework
* **SQLite/MySQL** – Database management
* **Bootstrap** – Frontend styling and responsive design
