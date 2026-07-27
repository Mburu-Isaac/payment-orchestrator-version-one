from flask import Blueprint
from myorchestrator.utilities.security.reform import HashAndEncrypt

bp = Blueprint("auth", __name__)


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

    # name = input("your name: ").title()
    # national_number = input("national ID number: ")

    # primary_number = input("primary phone number: ")
    # transaction_number = query_contact(primary_number)

    # email = input("your email address: ")
    # password = input("create password: ")
    # recovery_pin = input("four digit pin for password recovery: ")

    valuables = {
        "email": "mburuisaac086@gmail.com", #email,
        "password": "@1234.", #password,
        "toEncrypt": {
            "nationalNumber": "12345678", #national_number,
            "primaryNumber": "0112816337", #primary_number,
            "transactionNumber": "0743277087", #transaction_number,
            "recoveryPin": "2009" #recovery_pin,
        },
    }

    hash_en = HashAndEncrypt(valuables=valuables)

    # hash_en.hash_email()
    # hash_en.hash_password()
    return hash_en.encrypt_pin()


@bp.route("/login")
def login_client():
    pass


print(register_client())
