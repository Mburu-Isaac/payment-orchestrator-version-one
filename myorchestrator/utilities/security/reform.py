from hashlib import sha256


class HashAndEncrypt:

    def __init__(self):
        pass

    def hash_email(self, email):
        hashed_email = sha256(email.strip().lower().encode()).hexdigest()
        return hashed_email