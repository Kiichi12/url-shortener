from .database import db

class User:
    collection = db.users

    @classmethod
    def create_user(cls, username, email, password):
        user = {
            "username": username,
            "email": email,
            "password": password  # In production, hash the password!
        }
        return cls.collection.insert_one(user)

    @classmethod
    def find_by_email(cls, email):
        return cls.collection.find_one({"email": email})