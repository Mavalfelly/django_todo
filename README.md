### Django Todo API

* * * * *

**Overview**

This Django project provides an API for managing user authentication and a to-do list application. It includes user registration, login/logout functionality, and endpoints for creating and managing to-do lists and tasks.

* * * * *

**Features**

-   **User Authentication**: Signup, login, and logout functionality.
-   **Dashboard**: View user-specific data after logging in.
-   **To-Do Lists**: Create, view, and manage to-do lists.
-   **Task Management**: Toggle task completion status.

* * * * *

**Requirements**

-   Python 3.8+
-   Django 4.0+
-   A database supported by Django (e.g., SQLite, PostgreSQL, MySQL)

* * * * *

**Installation**

1.  **Clone the Repository**:

    bash

    Copy code

    `git clone <repository-url>
    cd <repository-folder>`

2.  **Set Up a Virtual Environment**:

    bash

    Copy code

    `python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate`

3.  **Install Dependencies**:

    Copy code

    `pip install -r requirements.txt`

4.  **Run Migrations**:

    Copy code

    `python manage.py migrate`

5.  **Start the Server**:

    Copy code

    `python manage.py runserver`

6.  **Access the Application**: Open `http://127.0.0.1:8000/` in your browser.

* * * * *

**Endpoints**

### Master List and Todo Endpoints

#### Master Lists

-   **GET** `/masterlists/`\
    Retrieve a list of all master lists.

-   **POST** `/masterlists/`\
    Create a new master list.

-   **GET** `/masterlists/{id}/`\
    Retrieve details of a specific master list.

-   **PUT** `/masterlists/{id}/`\
    Update a specific master list.

-   **DELETE** `/masterlists/{id}/`\
    Delete a specific master list.

#### Todos (Nested under Master Lists)

-   **GET** `/masterlists/{master_list_id}/todos/`\
    Retrieve a list of todos for a specific master list.

-   **POST** `/masterlists/{master_list_id}/todos/`\
    Create a new todo within a specific master list.

-   **GET** `/masterlists/{master_list_id}/todos/{id}/`\
    Retrieve details of a specific todo within a master list.

-   **PUT** `/masterlists/{master_list_id}/todos/{id}/`\
    Update a specific todo within a master list.

-   **DELETE** `/masterlists/{master_list_id}/todos/{id}/`\
    Delete a specific todo within a master list.

* * * * *

### Authentication Endpoints

#### User Registration

-   **POST** `/register/`\
    Register a new user.

#### Token Management

-   **POST** `/token/`\
    Obtain a pair of access and refresh tokens.

-   **POST** `/token/refresh/`\
    Refresh the access token using the refresh token.
