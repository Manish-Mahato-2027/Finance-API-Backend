# Finance *Backend*

A Django REST API for personal finance management — authentication, transaction tracking, and analytics in one place.

![Django](https://img.shields.io/badge/Django-3.2-green) ![JWT Auth](https://img.shields.io/badge/JWT_Auth-blue) ![SQLite / PG](https://img.shields.io/badge/SQLite%20%2F%20PG-orange) ![DRF Enabled](https://img.shields.io/badge/DRF-Enabled-brightgreen)

---

## Stats

| ENDPOINTS | AUTH | ROLES |
|-----------|------|-------|
| **13** | **JWT** | **3** |
| Backend 3 modules | Simple JWT / none | Admin · Analyst · Viewer |

---

## Features

- 👤 **User Management** — Custom user model with role-based access control and role mappings: Admin, Analyst, Viewer
- 🔐 **JWT Authentication** — Secure token auth with DRF Simple JWT
- 💸 **Transaction CRUD** — Full lifecycle management for income & expenses
- 🔍 **Filtering & Search** — Filter by date, amount, category, type
- 📊 **Dashboard Analytics** — Dynamic statistics with monthly reports
- 📄 **Pagination & CORS** — Paginated responses with cross-origin support

---

## Project Structure

```
finance_backend/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── users/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── finance/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── filters.py
│   │   └── urls.py
│   └── dashboard/
│       ├── views.py
│       └── urls.py
├── pagination.py
├── requirements.txt
├── manage.py
└── .env
```

---

## Installation

### 1. Clone & create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
DATABASE_URL_pg=postgres://user:pass/dbname
```

### 4. Run migrations & create superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start the development server

```bash
python manage.py runserver
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/auth/register/` | Register a new user |
| `POST` | `/api/auth/login/` | Obtain JWT access token |

### Users & Admin

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/auth/users/` | List all users |
| `GET` | `/api/auth/users/{id}/` | Retrieve a specific user |
| `PUT` | `/api/auth/users/{id}/` | Update user details |
| `DEL` | `/api/auth/users/{id}/` | Delete a user |

### Transactions

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/finance/transactions/` | Get the authenticated user's transactions |
| `POST` | `/api/finance/transactions/` | Create a new transaction |
| `GET` | `/api/finance/transactions/{id}/` | Retrieve a specific transaction |
| `PUT` | `/api/finance/transactions/{id}/` | Update a transaction |
| `DEL` | `/api/finance/transactions/{id}/` | Delete a transaction |

### Dashboard

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/dashboard/summary/` | Overview of monthly summary stats |
| `GET` | `/api/dashboard/monthly_reports/` | Full calculation by month |

---

## Filtering Transactions

| Parameter | Type | Description |
|-----------|------|-------------|
| `type` | `str` | Filter by type (e.g., `income`, `expense`) |
| `category` | `str` | Filter transactions by category |
| `date_after` | `date` | Filter date → `yyyy-mm-dd` |
| `date_before` | `date` | Filter date → `yyyy-mm-dd` |
| `amount_min` | `decimal` | Minimum transaction amount |
| `amount_max` | `decimal` | Maximum transaction amount |

**Example:**

```
/api/finance/transactions/?finance_type=expense&category=food&date_after=2024-01-01&amount_max=500
```

---

## Authentication

Include the JWT access token in every request header:

```http
Authorization: Bearer <your_jwt_token>
```

> Tokens are obtained from `/api/auth/login/`. Refresh tokens can be used to generate new access tokens without re-authenticating.

---

## Technologies

![Django 3.2](https://img.shields.io/badge/Django-3.2-092E20?logo=django)
![Django REST Framework](https://img.shields.io/badge/DRF-3.x-ff1709)
![JWT Token Auth](https://img.shields.io/badge/JWT-SimpleJWT-black)
![Django Filter](https://img.shields.io/badge/django--filter-enabled-blue)
![django-environ](https://img.shields.io/badge/django--environ-config-lightgrey)
![SQLite](https://img.shields.io/badge/SQLite-default-003B57)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-optional-336791?logo=postgresql)

---

## License

MIT License. Feel free to use and adapt for your own projects.