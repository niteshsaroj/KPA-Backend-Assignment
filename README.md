# KPA Backend Assignment – Nitesh Saroj

## 🔧 Tech Stack
- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL
- Postman (for API testing)

## 🚀 Setup Instructions

### 1. Clone the Repository or Unzip
```bash
git clone https://github.com/niteshsaroj/kpa-backend-assignment.git
cd kpa-backend-assignment
# OR unzip nitesh_kpa_assignment.zip and open the folder
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL Database
- Create a PostgreSQL database (e.g., `kpa_assignment`)
- Update `DATABASES` settings in `settings.py` or use `.env`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kpa_assignment',
        'USER': 'your_pg_user',
        'PASSWORD': 'your_pg_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional for admin access)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

---

## ✅ Implemented APIs

### 1. `POST /api/forms/bogie-checksheet/`
- Accepts nested JSON data
- Saves related models: `BmbcChecksheet`, `BogieChecksheet`, `BogieDetails`
- Returns success message and saved data

### 2. `GET /api/forms/wheel-specifications/`
- Returns list of all wheel specification records

---

## 🔗 API Testing via Postman

- Import the file: `nitesh_kpa_postman_collection.json`
- Includes:
  - `Submit Bogie Checksheet` (POST)
  - `Get Wheel Specifications` (GET)

---

## 📂 Sample PostgreSQL Data (via Admin Panel)

| Wheel Type            | Diameter | Rim Thickness |
|-----------------------|----------|----------------|
| LHB - Mono Block      | 920.0 mm | 30.5 mm         |
| ICF - Cast Steel      | 940.0 mm | 28.0 mm         |
| EMU - Forged          | 915.0 mm | 27.5 mm         |
| Freight - Cast Iron   | 1000.0 mm| 35.0 mm         |

---

## 🖊️ Notes
- PostgreSQL is used as the database.
- Admin panel available at `/admin/`.
- Use superuser to login and add data manually if needed.
- All APIs tested using Postman.

---


