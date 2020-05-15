from passlib.hash import sha256_crypt
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, email, first_name):
        self.email = email
        self.first_name = first_name

    def get_id(self):
        return self.email

    @staticmethod
    def validate_login(password, hash):
        return sha256_crypt.verify(password, hash)
