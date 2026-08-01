from hashlib import sha256
from ...extensions import ph, fernet


class HashAndEncrypt:

    def __init__(
        self,
        email=None,
        password=None,
        pin=None,
        primary_number=None,
        transactions_number=None,
        national_number=None
    ):
        self.email = email
        self.password = password
        self.pin = pin
        self.primary_number = primary_number
        self.transactions_number = transactions_number

        if self.transactions_number == self.primary_number:
            self.single_contact = True
        else:
            self.single_contact = False

        self.national_number = national_number

    def hash_email(self):
        hashed_email = sha256(self.email.strip().lower().encode()).hexdigest()
        return hashed_email

    # def hash_password(self):
    #     password = self.password
    #     return ph.hash(password)

    # def encrypt_pin(self):
    #     pin = self.pin
    #     recovpin_encryption = fernet.encrypt(pin.encode())
    #     return recovpin_encryption

    # def encrypt_transaction_contact(self) -> tuple:

    #     if self.single_contact == True:
    #         contact = self.primary_number
    #         contact_encryption = fernet.encrypt(contact.encode())
    #         return contact_encryption, None
    #     else:
    #         contact = self.transactions_number
    #         transactions_encryption = fernet.encrypt(contact.encode())

    #         encrypt_primary = self.encrypt_primary_contact(
    #             primary_contact=self.primary_number
    #         )

    #         return transactions_encryption, encrypt_primary

    # def encrypt_primary_contact(self, primary_contact):
    #     return fernet.encrypt(primary_contact.encode())

    # def encrypt_national_number(self):
    #     national_number = self.national_number
    #     return fernet.encrypt(national_number.encode())

    # def generate_client_fingerprint(self):

    #     nationalid_number = self.national_number
    #     transaction_number = self.transactions_number
    #     email = self.email
    #     primary_number = self.primary_number

    #     client_identity = (
    #         f"{nationalid_number}:{transaction_number}:{email}:{primary_number}"
    #     )
    #     client_fingerprint = sha256(client_identity.encode()).hexdigest()
    #     return client_fingerprint

    # def hash_client_otp(self, otp):
    #     hashed_otp = ph.hash(otp)
    #     return hashed_otp

    # def decrypt_recovery_pin(self, pin):
    #     pass

    # def decrypt_phone_numbers(self, phone_number):
    #     pass

    # def decryptid_number(self, idnumber):
    #     pass
