import secrets
import os
from datetime import datetime, timezone, timedelta



class ToolBox:

    def __init__(self):
        pass

    def generate_systems_otp(self) -> tuple:
        otp_characters = os.environ.get("CHARACTERS")
        otp = ''.join(secrets.choice(otp_characters) for _ in range(5))

        generated_at = datetime.now(timezone.utc)
        expires_at = generated_at + timedelta(minutes=5)
        return otp, generated_at, expires_at





