from auth_service import AuthService
from storage import UserStorage


def main():
    # Initialize the authentication service with user storage
    auth_service = AuthService(UserStorage())

    while True:
        print("\nLogin and Signup System")
        print("1. Sign up")
        print("2. Login")
        print("3. Forgot password")
        print("4. View registered profiles")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            sign_up(auth_service)
        elif choice == "2":
            login(auth_service)
        elif choice == "3":
            forgot_password(auth_service)
        elif choice == "4":
            view_profiles(auth_service)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1 to 5.")


# The following functions handle user interactions for signing up, logging in, resetting passwords, and viewing profiles.
def sign_up(auth_service):
    print("\nCreate Account")
    full_name = input("Full name: ")
    email = input("Email: ")
    date_of_birth = input("Date of birth (YYYY-MM-DD): ")
    password = input("Password: ")
    security_question = input("Security question: ")
    security_answer = input("Security answer: ")

    try:
        auth_service.sign_up(
            full_name,
            email,
            date_of_birth,
            password,
            security_question,
            security_answer,
        )
        print("Account created successfully.")
    except ValueError as error:
        print(f"Sign up failed: {error}")


def login(auth_service):
    print("\nLogin")
    email = input("Email: ")
    password = input("Password: ")

    try:
        user = auth_service.login(email, password)
        print(f"Welcome back, {user.full_name}.")
        print(f"Date of birth on profile: {user.date_of_birth}")
    except ValueError as error:
        print(f"Login failed: {error}")


def forgot_password(auth_service):
    print("\nForgot Password")
    email = input("Email: ")

    try:
        question = auth_service.get_security_question(email)
        print(f"Security question: {question}")
        answer = input("Security answer: ")
        new_password = input("New password: ")
        auth_service.reset_password(email, answer, new_password)
        print("Password reset successfully.")
    except ValueError as error:
        print(f"Password reset failed: {error}")


def view_profiles(auth_service):
    print("\nRegistered Profiles")
    profiles = auth_service.list_profiles()

    if not profiles:
        print("No registered users found.")
        return

    for index, user in enumerate(profiles, start=1):
        print(f"{index}. {user.full_name} | {user.email} | DOB: {user.date_of_birth}")


if __name__ == "__main__":
    main()
