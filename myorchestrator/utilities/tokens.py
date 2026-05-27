import os
from datetime import datetime, timedelta
import jwt
from pathlib import Path
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

class TokenManager:

    @staticmethod
    def load_private_key():
        
        _resolved_private_key_path = Path(os.environ.get("PRIVATE_KEY")).resolve()

        with open(_resolved_private_key_path, "rb") as private_file:
            return load_pem_private_key(
                private_file.read(),
                password=os.environ.get("JWT_KEY_PASSPHRASE").encode()
            )

    @staticmethod
    def load_public_key():

        _resolved_public_key_path = Path(os.environ.get("PUBLIC_KEY")).resolve()

        with open(_resolved_public_key_path, "rb") as public_file:
            return load_pem_public_key(
                public_file.read()
            )

    def __init__(self, user):
        self.private_key = self.load_private_key()
        self.algorithm = os.environ.get("JWT_ALGORITHM")
        self.public_key = self.load_public_key()
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
            payload=payload, key=self.private_key, algorithm=self.algorithm
        )

        return token, expires_at

    def validate_access_token(self, token: str) -> dict:
        
        try:
            payload = jwt.decode(
                token,
                public_key=self.public_key,
                algorithms=[self.algorithm]
            )
            return payload

        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token")
