from dataclasses import asdict, dataclass

# models.py
@dataclass
class User:
    full_name: str
    email: str
    date_of_birth: str
    password_hash: str
    security_question: str
    security_answer_hash: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(
            full_name=data["full_name"],
            email=data["email"],
            date_of_birth=data["date_of_birth"],
            password_hash=data["password_hash"],
            security_question=data["security_question"],
            security_answer_hash=data["security_answer_hash"],
        )
