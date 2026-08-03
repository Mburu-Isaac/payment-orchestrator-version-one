from flask import Blueprint
from myorchestrator.utilities.security.reform import HashAndEncrypt
from myorchestrator.models import Client, ClientPasswordHistory, ClientOTP
from myorchestrator.utilities.toolbox import ToolBox
from myorchestrator.email_service import EmailHandler

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

    eh = EmailHandler(receiver_email=valuables.get("email"))

    # -- Registration - Hash and Encrypt collected data -

    tb = ToolBox(dict_or_json=valuables)
    encryptable_valuables = tb.retrieve_structure_values(key="toEncrypt")

    hash_en = HashAndEncrypt(
        email=tb.retrieve_structure_values(key="email"),
        password=tb.retrieve_structure_values(key="password"),
        pin=encryptable_valuables.get("recoveryPin"),
        primary_number=encryptable_valuables.get("primaryNumber"),
        transactions_number=encryptable_valuables.get("transactionNumber"),
        national_number=encryptable_valuables.get("nationalNumber")
    )

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

    # write Client object
    # client = Client(
    #     name=name,
    #     national_id_number=encryptedid_number,
    #     primary_number=encrypted_primary_contact,
    #     transactions_number=enrypted_transactions_contact,
    #     email=hashed_email,
    #     password=hashed_password,
    #     recovery_pin=enrypted_recovery_pin,
    #     client_fingerprint=client_fingerprint,
    # )
    
    # # create parent table
    # create_parent = tb.create(data=[client])

    # if not create_parent:
    #     return 'client record remains null'

    # Registration - Registration OTP
    # 1: Generate OTP
    otp_tuple = tb.generate_systems_otp()
    registration_otp = otp_tuple[0]
    generated_at = otp_tuple[1]
    expires_at = otp_tuple[2]

    # 2: Hash OTP
    hashed_client_otp = hash_en.hash_client_otp(otp=registration_otp)

    # 3: Send OTP to client email
    send_otp = eh.send_otp(
        otp_object={
            "otp":registration_otp,
            "expiresAt":expires_at,
            "clientName":name
        }
    )

    return send_otp

    # # write ClientPasswordHistory object
    # client_password_history = ClientPasswordHistory(
    #     client=client, password=hashed_password
    # )

    # # write ClientOTP object
    # client_registration_otp = ClientOTP(
    #     client=client,
    #     otp=hashed_client_otp,
    #     otp_type="registration",
    #     expires_at=expires_at,
    #     created_at=generated_at,
    # )

    # if create_parent:
    #     create_child = tb.create(
    #         data=[client_password_history, client_registration_otp]
    #     )

    #     return create_child


@bp.route("/login")
def login_client():

    email = "mburuisaac086@gmail.com"

    hash_en = HashAndEncrypt(email=email)
    hashed_email = hash_en.hash_email()

    client_object = tb.conditional_read(
        table_name="clients", field="email", intended_value=hashed_email
    )

    if hashed_email == client_object.email:
        return "welcome back"
