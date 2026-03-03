<<<<<<< HEAD

=======
Hotel Management System (Django)
  Project Overview

The Hotel Management System is a web-based application built using Python and Django.
It allows customers to book hotel rooms online and make payments securely.
Admin users can manage rooms, bookings, and payments.

This project demonstrates real-world backend development concepts such as authentication, booking validation, payment handling, and deployment.

 Features
 User Features

User Registration & Login

Role-based authentication (Customer / Admin)

View available rooms

Book rooms

Prevent overlapping bookings

Online payment system

View booking history

Admin Features:

Add/Edit/Delete Rooms

View all bookings

Confirm or cancel bookings

Manage payments

Technologies Used:

Python 3

Django

PostgreSQL

HTML

Bootstrap

Git & GitHub

 Database Models:
Accounts Model:
role based  authentication (admin,customer)
 Room Model:

room_number

room_type (Single, Double, Deluxe, Suite)

price

description

image

is_available

 Booking Model:

user (ForeignKey)

room (ForeignKey)

check_in

check_out

total_price

status (Pending, Confirmed, Cancelled)

  Payment Model:

booking (OneToOneField)

amount

payment_method

payment_status

transaction_id

 Booking Validation

 

The system prevents:

Booking the same room for overlapping dates

Booking without login

Duplicate payment for same booking

Payment Integration

Currently supports:

Cash on Arrival

Razorpay (can be integrated)

Stripe (can be integrated)

Each booking has one payment record using OneToOne relationship.


Project Structure:

hotel_management/
│
├── accounts/
├── rooms/
├── bookings/
├── payments/
├── templates/
├── static/
└── manage.py


Clone repository:
git clone git@github.com:hemangiram/hotel_management.git
cd hotel_management


Create virtual environment:
python -m venv venv
source venv/bin/activate


Install dependencies:
pip install -r requirements.txt


Apply migrations:
python manage.py makemigrations
python manage.py migrate


Run server:
python manage.py runserver
>>>>>>> ae9ca7e8cdbfaa25497f93e29fec4f7907960469
