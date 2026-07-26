from hashlib import sha256
from ...extensions import ph


class HashAndEncrypt:

    def __init__(self):
        pass

    def hash_email(self, email):
        hashed_email = sha256(email.strip().lower().encode()).hexdigest()
        return hashed_email

    def hash_password(self, hashable):
        return ph.hash(hashable)

    def hash_pin(self, pin):
        return self.hash_password(hashable=pin)
