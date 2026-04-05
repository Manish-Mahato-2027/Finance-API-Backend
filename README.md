# Finance Backend

> A Django REST API for personal finance management — authentication, transaction tracking, and analytics in one place.

![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.15-ff1709)
![JWT](https://img.shields.io/badge/JWT-SimpleJWT-black)
![License](https://img.shields.io/badge/license-MIT-green)
![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?logo=render)

## 🚀 Live Demo

**Base URL:** [https://finance-api-backend-jp1l.onrender.com](https://finance-api-backend-jp1l.onrender.com)

> API is live and deployed on Render. Use the endpoints below with a REST client like Postman or HTTPie.

---

## Stats

| Endpoints | Auth   | Roles                     |
|-----------|--------|---------------------------|
| **13**    | **JWT** | **Admin · Analyst · Viewer** |

---

## Features

- 👤 **User Management** — Custom user model with role-based access control (Admin, Analyst, Viewer)
- 🔐 **JWT Authentication** — Secure token auth with DRF Simple JWT and refresh token support
- 💸 **Transaction CRUD** — Full lifecycle management for income & expense records
- 🔍 **Filtering & Search** — Filter by date, amount, category, and type
- 📊 **Dashboard Analytics** — Dynamic statistics with monthly report breakdowns
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
├── core/
│   └── pagination.py
├── requirements.txt
├── manage.py
└── .env
```

---

## Installation

### 1. Clone & create virtual environment

```bash
git clone https://github.com/your-username/finance-backend.git
cd finance-backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
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
DB_NAME=your-db-name
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### 4. Run migrations & create superuser

```bash
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
| `POST` | `/api/auth/login/` | Obtain JWT access & refresh tokens |

### Users & Admin

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/auth/users/` | List all users |
| `GET` | `/api/auth/users/{id}/` | Retrieve a specific user |
| `PUT` | `/api/auth/users/{id}/` | Update user details |
| `DELETE` | `/api/auth/users/{id}/` | Delete a user |

### Transactions

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/finance/transactions/` | List authenticated user's transactions |
| `POST` | `/api/finance/transactions/` | Create a new transaction |
| `GET` | `/api/finance/transactions/{id}/` | Retrieve a specific transaction |
| `PUT` | `/api/finance/transactions/{id}/` | Update a transaction |
| `DELETE` | `/api/finance/transactions/{id}/` | Delete a transaction |

### Dashboard

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/dashboard/summary/` | Overview of monthly summary stats |
| `GET` | `/api/dashboard/monthly_reports/` | Full breakdown by month |

---

## Filtering Transactions

| Parameter | Type | Description |
|-----------|------|-------------|
| `type` | `str` | Filter by type — `income` or `expense` |
| `category` | `str` | Filter by category name |
| `date_after` | `date` | From date — `yyyy-mm-dd` |
| `date_before` | `date` | To date — `yyyy-mm-dd` |
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

Tokens are obtained from `/api/auth/login/`. Use the refresh token to generate a new access token without re-authenticating:

```http
POST /api/auth/token/refresh/
Content-Type: application/json

{
  "refresh": "<your_refresh_token>"
}
```

---

## Tech Stack

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 5.2 | Web framework |
| djangorestframework | 3.15 | REST API |
| djangorestframework-simplejwt | 5.3 | JWT authentication |
| django-cors-headers | 4.4 | CORS support |
| django-filter | 24.2 | Query filtering |
| drf-yasg | 1.21 | Swagger/OpenAPI docs |
| python-decouple | 3.8 | Environment config |
| gunicorn | 25.3 | Production WSGI server |
| whitenoise | 6.12 | Static file serving |
| psycopg2 | 2.9 | PostgreSQL adapter |

---

## Deployment

This project is deployed on **Render**.

**Live URL:** https://finance-api-backend-jp1l.onrender.com

To deploy your own instance:

1. Push your code to GitHub
2. Create a new **Web Service** on [Render](https://render.com)
3. Set the build command: `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`
4. Set the start command: `gunicorn config.wsgi:application`
5. Add the following environment variables in Render dashboard:

```env
SECRET_KEY=your-secret-key
DEBUG=False
DJANGO_SETTINGS_MODULE=config.settings
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
DB_HOST=...
DB_PORT=5432
```

---

## License

MIT License. Free to use and adapt for your own projects.
