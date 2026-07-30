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
        recovpin_encryption = fernet.encrypt(pin.encode())
        return recovpin_encryption

    def encrypt_transaction_contact(self) -> tuple:

        primary_number = self.encryptable.get("primaryNumber")

        if self.single_contact == True:
            contact = primary_number
            contact_encryption = fernet.encrypt(contact.encode())
            return contact_encryption, None
        else:
            contact = self.encryptable.get("transactionNumber")
            transactions_encryption = fernet.encrypt(contact.encode())

            encrypt_primary = self.encrypt_primary_contact(
                primary_contact=primary_number
            )

            return transactions_encryption, encrypt_primary

    def encrypt_primary_contact(self, primary_contact):
        return fernet.encrypt(primary_contact.encode())

    def encrypt_national_number(self):
        national_number = self.encryptable.get("nationalNumber")
        return fernet.encrypt(national_number.encode())

    def generate_client_fingerprint(self):

        nationalid_number = self.encryptable.get("nationalNumber")
        transaction_number = self.encryptable.get("transactionNumber")
        email = self.valuable_data.get("email")
        primary_number = self.encryptable.get("primaryNumber")

        client_identity = f"{nationalid_number}:{transaction_number}:{email}:{primary_number}"
        client_fingerprint = sha256(client_identity.encode()).hexdigest()
        return client_fingerprint

    def hash_client_otp(self, otp):
        hashed_otp = ph.hash(otp)
        return hashed_otp
            
