# Flask Backend Project with SQLAlchemy and JWT 🚀

This project implements a Flask backend with SQLAlchemy for managing a MySQL database and JWT authentication.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Environment Variables](#environment-variables)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
     cd <project-directory>
   ```

3. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Unix systems
   ```

   ```bash
   python -m venv venv
   venv\Scripts\activate  # For Windows systems
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application, use the following command:

```bash
python app.py
```

The application will start running on `http://localhost:5000`.

## Endpoints

Below are the available endpoints:

- `{serverip}/api/users`: GET (Get all users), POST (Create a new user)
- `{serverip}/api/users/<user_id>`: GET (Get a specific user), PUT (Update a specific user), DELETE (Delete a specific user)
- `{serverip}/api/users/register`: POST (Register a new user)
- `{serverip}/api/nutritionists`: GET (Get all nutritionists), POST (Create a new nutritionist)
- `{serverip}/api/nutritionists/<nutritionist_id>`: GET (Get a specific nutritionist), PUT (Update a specific nutritionist), DELETE (Delete a specific nutritionist)
- `{serverip}/api/nutritionists/register`: POST (Register a new nutritionist)
- `{serverip}/api/comments`: GET (Get all comments), POST (Create a new comment)
- `{serverip}/api/comments/<comment_id>`: GET (Get a specific comment), PUT (Update a specific comment), DELETE (Delete a specific comment)
- `{serverip}/api/professional_tips`: GET (Get all professional tips), POST (Create a new professional tip)
- `{serverip}/api/professional_tips/<professional_tip_id>`: GET (Get a specific professional tip), PUT (Update a specific professional tip), DELETE (Delete a specific professional tip)
- `{serverip}/api/login`: POST (User login)

## Environment Variables

- `SECRET_KEY`: Secret key for Flask app
- `JWT_SECRET_KEY`: Secret key for JWT token
- `DATABASE_URL`: URL for the database (example for Xampp, `mysql+pymysql://root@localhost/flask-jwt-flutter`)

Make sure to set up these environment variables before running the application.
