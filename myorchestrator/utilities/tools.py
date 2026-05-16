import secrets
import os

def generate_otp(length=5):
    return ''.join(secrets.choice(os.environ.get("CHARACTERS")) for _ in range(length))

