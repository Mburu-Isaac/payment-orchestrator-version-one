from flask import Blueprint
from myorchestrator.utilities.security.reform import HashAndEncrypt
from myorchestrator.models import Client, ClientPasswordHistory, ClientOTP
from myorchestrator.utilities.toolbox import ToolBox

bp = Blueprint("auth", __name__)
tb = ToolBox()


def query_contact(primary_contact):
    query = int(
        input(
            "transaction number: Same as primary number? \n 1. Yes \n 2. No \n Response: "
        )
    )

    if query == 1:
        print("Say less")
        return primary_contact

    elif query == 2:
        transaction_number = input("transaction number: ")
        return transaction_number


@bp.route("/signup")
def register_client():

    # -- Registration: collect client data -

    # name = input("your name: ").title()
    # national_number = input("national ID number: ")

    # primary_number = input("primary phone number: ")
    # transaction_number = query_contact(primary_number)

    # email = input("your email address: ")
    # password = input("create password: ")
    # recovery_pin = input("four digit pin for password recovery: ")

    name = "mburu Isaac"
    valuables = {
        "email": "mburuisaac086@gmail.com",  # email,
        "password": "@1234.",  # password,
        "toEncrypt": {
            "nationalNumber": "12345678",  # national_number,
            "primaryNumber": "0112816337",  # primary_number,
            "transactionNumber": "0743277087",  # transaction_number,
            "recoveryPin": "2009",  # recovery_pin,
        },
    }

    # -- Registration - Hash and Encrypt collected data -

    hash_en = HashAndEncrypt(valuables=valuables)

    hashed_email = hash_en.hash_email()
    hashed_password = hash_en.hash_password()
    enrypted_recovery_pin = hash_en.encrypt_pin()
    encryptedid_number = hash_en.encrypt_national_number()

    enrypted_transactions_contact = hash_en.encrypt_transaction_contact()[0]
    encrypted_primary_contact = hash_en.encrypt_transaction_contact()[1]

    # -- Hash and Encrypt collected data: generate client fingerprint -

    client_fingerprint = hash_en.generate_client_fingerprint()

    # -- Hash and Encrypt collected data: set transaction's contact to store -
    if encrypted_primary_contact is None:
        encrypted_primary_contact = enrypted_transactions_contact

    # Registration - write database objects
    client_object = {
        "name": name,
        "national_id_number": encryptedid_number,
        "primary_number": encrypted_primary_contact,
        "transaction_number": enrypted_transactions_contact,
        "email": hashed_email,
        "password": hashed_password,
        "recovery_pin": enrypted_recovery_pin,
        "client_fingerprint": client_fingerprint,
    }

    client_password_history_object = {
        "client": client_object,
        "password": hashed_password,
    }

    otp_tuple = tb.generate_systems_otp()
    registration_otp = otp_tuple[0]
    generated_at = otp_tuple[1]
    expires_at = otp_tuple[2]

    hashed_client_otp = hash_en.hash_client_otp(otp=registration_otp)

    client_registration_otp_object = {
        "otp": hashed_client_otp,
        "otp_type": "registration",
        "expires_at": expires_at,
        "created_at": generated_at,
    }

    return client_object, client_password_history_object, client_registration_otp_object

    # Write Database Objects: write Client object

    # client = Client(
    #     name=name,
    #     national_id_number=encryptedid_number,
    #     primary_number=encrypted_primary_contact,
    #     transactions_number=enrypted_transactions_contact,
    #     email=hashed_email,
    #     password=hashed_password,
    #     recovery_pin=enrypted_recovery_pin,
    #     client_fingerprint=client_fingerprint
    # )

    # Write Database Objects: write ClientPasswordHistory object

    # client_password_history = ClientPasswordHistory(
    #     client=client,
    #     password=hashed_password
    # )

    # Write Database Objects: write ClientOTP object

    # client_registration_otp = ClientOTP(
    #     otp=hashed_client_otp,
    #     otp_type="registration",
    #     expires_at=expires_at,
    #     created_at=generated_at
    # )

    # return


@bp.route("/login")
def login_client():
    return tb.generate_systems_otp()


from pprint import pprint

pprint(register_client())
