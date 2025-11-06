# 🎓 Online Course Shop

A Django-based web application for managing and browsing online courses.  
Users can explore available categories and courses.  
The admin panel allows managing (adding, editing, deleting) both courses and categories.  
A RESTful API is also available for external integrations.

---

## 🚀 Features

- Browse categories and courses  
- Admin panel to **add**, **edit**, and **delete** courses and categories  
- RESTful API built with **Django Tastypie**  
- Simple and clear project structure  
- Ready for future extension (e.g., cart and checkout functionality)

---

## ⚙️ Installation & Setup

Follow the steps below to run the project locally.

### 1. Clone the repository
```bash
git clone https://github.com/vkrylova/Courses.git
cd Courses
```
### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply migrations
```bash
python manage.py migrate
```
### 5. Run the development server
```bash
python manage.py runserver
```

---

## 🧩 Project Structure
<details>
  
```bash
project_root/
│
├── base/                           # Core app: settings and configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── shop/                           # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── api/                            # Tastypie API application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── authentication.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── resources.py
│
├── templates/                      # Global templates shared across apps
│   ├── base.html
│   └── shop/
│       ├── courses.html
│       └── single_course.html
│
├── manage.py
└── requirements.txt
```
</details>

---

## 🧠Tech Stack:
- Python 3.12
- Django 4
- Django Tastypie
- SQLite / PostgreSQL
- HTML5, CSS3
  
---

## 📸 Screenshots
<details>
<img width="1663" height="603" alt="shop" src="https://github.com/user-attachments/assets/7bc94b90-dff0-4011-8d0d-97a9aad1f001" />
<img width="1647" height="396" alt="image" src="https://github.com/user-attachments/assets/e0fc9e0a-4e53-4b7e-aebd-114327971336" />
<img width="1772" height="632" alt="image" src="https://github.com/user-attachments/assets/ad605f64-8c45-490c-bd91-21886640344d" />
<img width="442" height="233" alt="image" src="https://github.com/user-attachments/assets/102054ca-bc46-43a0-b7ca-dff79011e2f9" />
</details>



