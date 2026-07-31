import secrets
import os
from datetime import datetime, timezone, timedelta
from myorchestrator.extensions import db



class ToolBox:

    def __init__(self):
        pass

    def generate_systems_otp(self) -> tuple:
        otp_characters = os.environ.get("CHARACTERS")
        otp = ''.join(secrets.choice(otp_characters) for _ in range(5))

        generated_at = datetime.now(timezone.utc)
        expires_at = generated_at + timedelta(minutes=5)
        return otp, generated_at, expires_at

    def create(self, data: list) -> bool:
        
        return len(data)

        # try:
        #     if len(data) == 1:
        #         db.session.add(data[0])
        #     else:
        #         db.session.add_all(data)

        #     db.session.commi()
        #     return True

        # except Exception:
        #     db.session.rollback()
        #     raise
        #     return False





