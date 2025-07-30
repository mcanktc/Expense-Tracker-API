# Expense Tracker API

## Overview

This is a secure and extensible Expense Tracker REST API built using Django REST Framework, JWT authentication, and Djoser for user management. The API allows users to register, log in, and manage their expenses under predefined categories.

## Technologies Used

- Django
- Django REST Framework (DRF)
- Djoser (user management)
- JWT (JSON Web Tokens)
- SQLite or MySQL (database support)

## Setup Instructions

1. Clone the repository.
2. Set up your virtual environment and install dependencies.
3. Configure `.env` for your secret key, database, and JWT settings.
4. Run migrations and create a superuser.
5. Start the server and test endpoints via Insomnia or cURL.

## API Endpoints

| Method | Endpoint                       | Description                     | Authentication |
|--------|--------------------------------|---------------------------------|----------------|
| POST   | /auth/users/                   | Register a new user             | No             |
| POST   | /auth/jwt/create/              | Obtain JWT tokens (login)       | No             |
| POST   | /auth/jwt/refresh/             | Refresh access token            | No             |
| GET    | /etapi/expenses/               | List user's expenses            | Yes            |
| POST   | /etapi/expenses/               | Create a new expense            | Yes            |
| PATCH  | /etapi/expenses/<built-in function id>/          | Update an expense               | Yes            |
| DELETE | /etapi/expenses/<built-in function id>/          | Delete an expense               | Yes            |

## Expense Categories

- G: Groceries
- L: Leisure
- E: Electronics
- U: Utilities
- C: Clothing
- H: Health
- O: Others

## Notes

- All endpoints under `/etapi/expenses/` require a valid JWT Bearer Token.
- Only authenticated users can manage their own expenses.

