from flask import Blueprint
from myorchestrator.utilities.security.reform import HashAndEncrypt

bp = Blueprint("auth", __name__)


def query_contact(primary_contact):
    query = int(
        input(
            "\n transaction number: Same as primary number? \n 1. Yes \n 2. No \n Response: "
        )
    )

    if query == 1:
        return primary_contact

    elif query == 2:
        transaction_number = input("transaction number: ")
        return transaction_number


@bp.route("/signup")
def register_client():

    name = input("your name: ").title()
    national_number = input("national ID number: ")

    primary_number = input("primary phone number: ")
    transaction_number = query_contact(primary_number)

    email = input("your email address: ")
    password = input("create password: ")
    recovery_pin = input("four digit pin for password recovery: ")

    valuables = {
        "email": email,
        "password": password,
        "toEncrypt": {
            "nationalNumber": national_number,
            "primaryNumber": primary_number,
            "transactionNumber": transaction_number,
            "recoveryPin": recovery_pin,
        },
    }

    hash_en = HashAndEncrypt(valuables=valuables)

    return hash_en.hash_email()


@bp.route("/login")
def login_client():
    pass


print(register_client())
