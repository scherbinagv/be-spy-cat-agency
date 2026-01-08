# 🐍 Spy Cats Agency – Backend

Backend for Spy Cats Agency built with Django REST Framework.

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL / SQLite
- TheCatAPI

---

## 📌 Features

- CRUD for spy cats
- Breed validation via TheCatAPI
- Mission & target management
- Business rules validation

---

## ▶️ Setup & Run

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


## Postman

Postman collection with all API endpoints is available here:

postman/spy-cat-agency.postman_collection.json
