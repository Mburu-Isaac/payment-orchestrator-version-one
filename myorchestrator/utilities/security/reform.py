from hashlib import sha256
from ...extensions import ph


class HashAndEncrypt:

    def __init__(self, valuables):
        self.valuable_data = valuables

    def hash_email(self):
        email = self.valuable_data["email"]
        hashed_email = sha256(email.strip().lower().encode()).hexdigest()
        return hashed_email

    # def hash_password(self, hashable):
    #     return ph.hash(hashable)

    # def encrypt_pin(self, pin):
    #     return self.hash_password(hashable=pin)
