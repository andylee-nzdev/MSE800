import base64
import hashlib
import hmac
import os
import re
from datetime import datetime

from models import User


class AuthService:
    def __init__(self, storage):
        self.storage = storage
        self.users = storage.load_users()

    def sign_up(
        self,
        full_name,
        email,
        date_of_birth,
        password,
        security_question,
        security_answer,
    ):
        email = self._normalize_email(email)
        full_name = full_name.strip()
        security_question = security_question.strip()

        self._validate_full_name(full_name)
        self._validate_email(email)
        self._validate_date_of_birth(date_of_birth)
        self._validate_password(password)

        if email in self.users:
            raise ValueError("An account already exists for this email address.")

        if not security_question:
            raise ValueError("Security question cannot be empty.")

        if not security_answer.strip():
            raise ValueError("Security answer cannot be empty.")

        self.users[email] = User(
            full_name=full_name,
            email=email,
            date_of_birth=date_of_birth,
            password_hash=self._hash_secret(password),
            security_question=security_question,
            security_answer_hash=self._hash_secret(security_answer.lower().strip()),
        )
        self.storage.save_users(self.users)

    def login(self, email, password):
        email = self._normalize_email(email)
        user = self.users.get(email)

        if user is None or not self._verify_secret(password, user.password_hash):
            raise ValueError("Invalid email or password.")

        return user

    def get_security_question(self, email):
        email = self._normalize_email(email)
        user = self.users.get(email)

        if user is None:
            raise ValueError("No account exists for this email address.")

        return user.security_question

    def reset_password(self, email, security_answer, new_password):
        email = self._normalize_email(email)
        user = self.users.get(email)

        if user is None:
            raise ValueError("No account exists for this email address.")

        answer_matches = self._verify_secret(
            security_answer.lower().strip(),
            user.security_answer_hash,
        )

        if not answer_matches:
            raise ValueError("Security answer is incorrect.")

        self._validate_password(new_password)
        user.password_hash = self._hash_secret(new_password)
        self.storage.save_users(self.users)

    def list_profiles(self):
        return list(self.users.values())

    def _hash_secret(self, secret):
        salt = os.urandom(16)
        key = hashlib.pbkdf2_hmac(
            "sha256",
            secret.encode("utf-8"),
            salt,
            120_000,
        )
        return (
            base64.b64encode(salt).decode("utf-8")
            + ":"
            + base64.b64encode(key).decode("utf-8")
        )

    def _verify_secret(self, secret, stored_hash):
        salt_text, key_text = stored_hash.split(":", 1)
        salt = base64.b64decode(salt_text)
        expected_key = base64.b64decode(key_text)
        actual_key = hashlib.pbkdf2_hmac(
            "sha256",
            secret.encode("utf-8"),
            salt,
            120_000,
        )
        return hmac.compare_digest(actual_key, expected_key)

    def _normalize_email(self, email):
        return email.strip().lower()

    def _validate_full_name(self, full_name):
        if len(full_name.split()) < 2:
            raise ValueError("Full name should include first and last name.")

    def _validate_email(self, email):
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not re.match(pattern, email):
            raise ValueError("Email address is not valid.")

    def _validate_date_of_birth(self, date_of_birth):
        try:
            datetime.strptime(date_of_birth, "%Y-%m-%d")
        except ValueError as exc:
            raise ValueError("Date of birth must use YYYY-MM-DD format.") from exc

    def _validate_password(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

        if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
            raise ValueError("Password must contain at least one letter and one number.")
