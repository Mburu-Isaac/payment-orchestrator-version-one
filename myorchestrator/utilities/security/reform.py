from hashlib import sha256
from ...extensions import ph


class HashAndEncrypt:

    def __init__(self, valuables):
        self.valuable_data = valuables

    def hash_email(self):
        email = self.valuable_data.get("email")
        hashed_email = sha256(email.strip().lower().encode()).hexdigest()
        return hashed_email

    def hash_password(self):
        password = self.valuable_data.get("password")
        return ph.hash(password)

    # def encrypt_pin(self, pin):
    #     return self.hash_password(hashable=pin)
