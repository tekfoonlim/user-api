# User Management API

A RESTful API built using FastAPI to manage users. This project demonstrates clean architecture, proper API design, validation, and error handling.

---

# 🚀 Features

* Create, read, update, and delete users
* Search users by name or email
* Sort users by name or email
* Input validation using Pydantic
* JSON-based data persistence
* Clean architecture (routes → service → repository)

---

# 🛠️ Tech Stack

* Python
* FastAPI
* Uvicorn

---

# 📦 Setup Instructions
# 1. Clone the repository

```bash
git clone <your-repo-link>
cd user-api
```

---

# 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---
# 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 4. Run the application

```bash
uvicorn app.main:app --reload
```

---

# 5. Access API

* Swagger UI:
  http://localhost:8000/docs

* Base URL:
  http://localhost:8000

---

# 📌 API Endpoints

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| GET    | /users      | List users     |
| GET    | /users/{id} | Get user by ID |
| POST   | /users      | Create user    |
| PUT    | /users/{id} | Update user    |
| DELETE | /users/{id} | Delete user    |

---

# 🔍 Query Parameters

* `search` → filter users by name or email
* `sort` → sort by `name` or `email`
* `order` → `asc` or `desc`

Example:

```
/users?search=john&sort=name&order=asc
```

---

# 📄 Sample Request

# Create User

```json
{
  "name": "Joseph",
  "email": "joe@example.com"
}
```

---

# 📁 Data Storage

* Data is stored in:

```
data/users.json
```
## ⚠️ Assumptions / Notes

* This project uses file-based storage (JSON) instead of a database
* UUID is used for unique user identification
* PUT endpoint supports partial updates (acts like PATCH)
* Extra fields in request body are not allowed (strict validation)
* Error handling is implemented for invalid inputs and missing users

---
