# Login and Signup System

This project is a simple console-based account management system.

The system allows users to:

- Create an account with full name, email, date of birth, password, security question, and security answer.
- Login with an existing email and password.
- Reset a forgotten password by answering the saved security question.
- View registered user profiles without exposing password details.

User records are stored in a local SQLite database named `users.db`. The database and `users` table are created automatically when the program starts.

## Project Structure

- `main.py`: Runs the console menu and handles user interaction.
- `auth_service.py`: Contains signup, login, password reset, validation, and password hashing logic.
- `storage.py`: Handles loading and saving user records to the SQLite database.
- `models.py`: Defines the `User` data model.
- `intro.txt`: Contains the original activity instructions.
- `README.md`: Describes the project and explains how to run it.

## Database Design

The SQLite database contains one table named `users`.

Columns:

- `email`: Primary key and unique login identifier.
- `full_name`: User's full name.
- `date_of_birth`: User's date of birth in `YYYY-MM-DD` format.
- `password_hash`: Salted password hash.
- `security_question`: Question used for password recovery.
- `security_answer_hash`: Salted hash of the security answer.

## Functional Breakdown

### Signup

The signup feature collects the user's personal information and account credentials.

Required fields:

- Full name
- Email address
- Date of birth in `YYYY-MM-DD` format
- Password
- Security question
- Security answer

The system validates the name, email, date of birth, and password before saving the account.

### Login

The login feature checks the entered email and password against the saved account data.

Passwords are not stored as plain text. They are hashed using Python's standard `hashlib.pbkdf2_hmac` function with a random salt.

### Forgot Password

The forgot-password feature allows a user to reset their password if they know the answer to their saved security question.

The new password must follow the same password rules as signup:

- At least 8 characters long
- Contains at least one letter
- Contains at least one number

### Profile Management

The profile list displays basic account information:

- Full name
- Email
- Date of birth

Password hashes and security answers are not shown.

## How to Run

From this folder, run:

```bash
python3 main.py
```

## Example Usage

```text
Login and Signup System
1. Sign up
2. Login
3. Forgot password
4. View registered profiles
5. Exit
Choose an option: 1

Create Account
Full name: Alex Smith
Email: alex@example.com
Date of birth (YYYY-MM-DD): 2000-04-15
Password: Password123
Security question: What city were you born in?
Security answer: Auckland
Account created successfully.
```

## Maintainability

The project is separated into small modules so each section has a clear responsibility:

- The menu is handled by `main.py`.
- Business rules are handled by `AuthService`.
- SQLite storage is handled by `UserStorage`.
- User account data is represented by the `User` model.

This makes the project easier to read, test, and extend in the future.
