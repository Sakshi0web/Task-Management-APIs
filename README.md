Task Management API


Overview

This project provides a Task Management API built using Django and Django Rest Framework. The API allows users to perform CRUD operations on tasks, including:

* Task creation
* Task retrieval (with search and pagination support)
* Task update
* Task deletion
  
The API also supports user authentication, allowing users to register, log in, and manage their tasks individually.

------------------------------ *** -----------------------------------

Endpoints
1. User Registration
   
POST /api/auth/register/

Register a new user.

Request Body:

json

{
  "username": "testuser",
  "password": "password123",
  "email": "testuser@example.com"
}

Response:

json

{
  "message": "User registered successfully."
}

---------------------------- *** ---------------------------------

2. User Login
   
POST /api/auth/login/

Log in and obtain an authentication token.

Request Body:

json

{
  "username": "testuser",
  "password": "password123"
}

Response:

json

{
  "token": "744f763f111113bc894e66b558bc48f1f1c6f4c6"
}

---------------------------- *** ---------------------------------

3. Task Management
   
Create a New Task

POST /api/tasks/

Create a new task for the authenticated user.

Request Body:

json

{
  "title": "Test Task",
  "description": "This is a task for testing.",
  "due_date": "2024-12-01",
  "completed": true
}

Response:

json

{
  "id": 1,
  "user": "testuser",
  "title": "Test Task",
  "description": "This is a task for testing.",
  "due_date": "2024-12-01",
  "completed": true
}

---------------------------- *** ---------------------------------

Retrieve Tasks (Filtered by User)

GET /api/tasks/

Retrieve tasks assigned to the authenticated user. Supports search and ordering by due_date and completed.

Example URL:

bash

/api/tasks/?search=test&ordering=due_date

Response:

json

[
  {
    "id": 1,
    "user": "testuser",
    "title": "Test Task 1",
    "description": "This is a task for testing API.",
    "due_date": "2024-10-23",
    "completed": true
  },
  
  {
    "id": 2,
    "user": "testuser",
    "title": "Test Task 2",
    "description": "Another test task.",
    "due_date": "2024-12-01",
    "completed": false
  }
]

--------------------- *** -------------------------------

Update Task

PUT /api/tasks/{task_id}/

Update an existing task by its ID.

Request Body:

json

{
  "title": "Updated Task",
  "description": "Updated description.",
  "due_date": "2024-12-25",
  "completed": false
}

Response:

json

{
  "id": 1,
  "user": "testuser",
  "title": "Updated Task",
  "description": "Updated description.",
  "due_date": "2024-12-25",
  "completed": false
}

---------------------------- *** ---------------------------------

Delete Task

DELETE /api/tasks/{task_id}/

Delete a task by its ID.

Response:

json

{
  "message": "Task deleted successfully."
}

---------------------------- *** ---------------------------------

Setup and Installation

Prerequisites
* Python 3.x
* Django 3.x+
* Django Rest Framework
* SQLite (default database) or PostgreSQL

---------------------------- *** ---------------------------------

Installation Steps

Clone the repository:

bash

git clone https://github.com/yourusername/task-api.git

cd task-api

Create a virtual environment:

bash

python -m venv venv

source venv/bin/activate  # On Windows, use venv\Scripts\activate

Install dependencies:

bash

pip install -r requirements.txt

Run migrations:

bash

python manage.py migrate

Create a superuser (for admin access):

bash

python manage.py createsuperuser

Start the development server:

bash

python manage.py runserver

The API will now be available at http://127.0.0.1:8000.

---------------------------- *** ---------------------------------

Testing API with Postman

You can use Postman to test the API by following these steps:

1. Register a User:

* Endpoint: POST http://127.0.0.1:8000/api/auth/register/
* Request Body:
  
json

{
  "username": "testuser",
  "password": "password123",
  "email": "testuser@example.com"
}

2. Login to Get Token:

* Endpoint: POST http://127.0.0.1:8000/api/auth/login/
* Request Body:
  
json

{
  "username": "testuser",
  "password": "password123"
}

Response:

json

{
  "token": "your_token_here"
}

3. Create a Task:

* Endpoint: POST http://127.0.0.1:8000/api/tasks/
* Authorization: Bearer Token (your_token_here)
* Request Body:
  
json

{
  "title": "Test Task",
  "description": "This is a task for testing.",
  "due_date": "2024-12-01",
  "completed": false
}

4. Get Tasks:

* Endpoint: GET http://127.0.0.1:8000/api/tasks/
* Authorization: Bearer Token (your_token_here)

---------------------------- *** ---------------------------------

Pagination

The API supports pagination for retrieving tasks. You can use query parameters like page and page_size to control the results returned:

* Example URL for pagination:
  
bash

/api/tasks/?page=2&page_size=10

This will return the second page of tasks, with 10 tasks per page.
