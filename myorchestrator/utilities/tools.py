import secrets
import os


def generate_otp(length=6):
    return ''.join(secrets.choice(os.environ.get("CHARACTERS")) for _ in range(length))

def slugify_object():
    pass

def standardize_contact():
    pass

def validate_subscription():
    pass