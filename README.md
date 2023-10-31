# booksapi-

# BookAPI Project

This project is a simple REST API for managing a list of books using Django, along with JWT (JSON Web Token) authentication for securing the API endpoints.

## Prerequisites

Before getting started, make sure you have the following prerequisites installed:

- Python (3.x)
  
- Django
  
- Django REST framework
  
- djangorestframework-simplejwt (for JWT authentication)

2.You can install the necessary packages using `pip`:

3.pip install django djangorestframework djangorestframework-simplejwt

4. Project Setup

Clone the repository:

git clone https://github.com/your-username/bookapi.git

5. cd bookapi

6. Create a virtual environment (optional but recommended):

python -m venv venv

source venv/bin/activate  # On Windows, use: venv\Scripts\activate

7 .Migrate the database and create a superuser:

python manage.py migrate

python manage.py createsuperuser

8. JWT Authentication

To secure the API endpoints, this project uses JWT (JSON Web Token) authentication.


9. API Endpoints
POST /api/token/: Obtain a JWT token by providing your username and password.

GET /api/books/: List all books.

GET /api/books/<id>/: Retrieve a specific book by ID.

POST /api/books/: Create a new book.

PUT /api/books/<id>/: Update an existing book.

DELETE /api/books/<id>/: Delete a book.


Thank you for using the BookAPI project!



asgiref==3.2.7
Django==3.0.5
django-widget-tweaks==1.4.8
pytz==2020.1
sqlparse==0.3.1

