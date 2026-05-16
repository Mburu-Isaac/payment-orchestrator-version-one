import os
from datetime import datetime, timedelta
import jwt

class TokenManager:

    def __init__(self, user):
        self.private_key = "private_key"
        self.algorithm = os.environ.get("JWT_ALGORITHM")
        self.public_key = "public_key"
        self.user = user

    def generate_access_token(self):

        issued_at = datetime.now()
        expires_at = issued_at + timedelta(minutes=15)

        payload = {
            "sub": str(self.user.get("user_id")),
            "iat": issued_at,
            "exp": expires_at,
            "type": "access",
        }

        token = jwt.encode(
            payload=payload, 
            key=self.private_key, 
            algorithm=self.algorithm
        )

        return token, expires_at
