# **Python Task Manager**  

---

## 📋 **Overview**

A project to implement a **task manager system** API using Django, Django Rest Framework, DRF Authentication, and pytest.

---

## 🛠️ **Features**

- **User Authentication**: Secure user creation and authentication using DRF Token.
- **Task Management**:
  - Create, read, update, and delete tasks.
  - Each task is associated with a specific user.
- **User Management**:
  - Create, read, update, and disable your profile.
- **Task Filtering**:
  - Filter tasks by `status`.
  - Order tasks by `title` or `created_at`.
- **Automated Testing**: Comprehensive test suite to ensure reliability.

---

## 🚀 **Running**

### Prerequisites

- Python 3.12+  
- Django 5.1.3  
- pipenv or virtualenv (optional but recommended)  

---

### 🔧 **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/busaikuna/task_manager.git
   cd task_manager
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

---

### ⚙️ **Testing**

The project uses **pytest** for testing, ensuring the app works as expected.

#### Run Tests:

```bash
pytest
```

---

## 📂 **Project Structure**

```plaintext
task_manager/
├── api/
│   ├── migrations/          # Database migrations
│   ├── __init__.py          # Package marker
│   ├── admin.py             # Django admin customization
│   ├── apps.py              # App configuration
│   ├── models.py            # Task model
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # App-specific URLs
│   └── views.py             # API views
├── task_manager/
│   ├── __init__.py          # Package marker
│   ├── asgi.py              # ASGI configuration
│   ├── settings.py          # Project settings
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py              # WSGI configuration
├── tests/
│   ├── __init__.py          # Package marker
│   └── tests.py             # API tests
├── .pytest_cache/           # Pytest cache files
├── db.sqlite3               # SQLite database (development only)
├── pytest.ini               # Pytest configuration
├── manage.py                # Django management script
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation (this file)
```

---

## 📜 **API Endpoints**

### **Users Endpoints**

| Method | Endpoint           | Description                  |
|--------|--------------------|------------------------------|
| POST   | `/api/users/`      | Create a new user            |
| GET    | `/api/users/`      | Retrieve all users           |
| GET    | `/api/users/<id>/` | Retrieve a specific user     |
| PUT    | `/api/users/<id>/` | Update a specific user       |
| DELETE | `/api/users/<id>/` | Delete a specific user       |

---

### **Tasks Endpoints**

| Method | Endpoint           | Description                  |
|--------|--------------------|------------------------------|
| POST   | `/api/tasks/`      | Create a new task            |
| GET    | `/api/tasks/`      | Retrieve all tasks           |
| GET    | `/api/tasks/<id>/` | Retrieve a specific task     |
| PUT    | `/api/tasks/<id>/` | Update a specific task       |
| DELETE | `/api/tasks/<id>/` | Delete a specific task       |

### **User-Specific Task Endpoint**

| Method | Endpoint                  | Description                             |
|--------|---------------------------|-----------------------------------------|
| GET    | `/api/users/<id>/tasks/`  | Retrieve tasks owned by a specific user |

---

## 🧪 **Testing Frameworks and Tools**

- **pytest**: For writing and running tests.  
- **pytest-django**: Django-specific plugin for pytest.  
- **Django Test Client**: For API request simulations.  

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--- 