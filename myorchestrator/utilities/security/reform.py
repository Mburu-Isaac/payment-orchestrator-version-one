from hashlib import sha256
from ...extensions import ph, fernet


class HashAndEncrypt:

    def __init__(self, valuables):
        self.valuable_data = valuables
        self.encryptable = self.valuable_data.get("toEncrypt")
        
        if self.encryptable.get("transactionNumber") == self.encryptable.get("primaryNumber"):
            self.single_contact = True
        else:
            self.single_contact = False


    def hash_email(self):
        email = self.valuable_data.get("email")
        hashed_email = sha256(email.strip().lower().encode()).hexdigest()
        return hashed_email

    def hash_password(self):
        password = self.valuable_data.get("password")
        return ph.hash(password)

    def encrypt_pin(self):
        pin = self.encryptable.get("recoveryPin")
        encryption = fernet.encrypt(pin.encode())
        return encryption
