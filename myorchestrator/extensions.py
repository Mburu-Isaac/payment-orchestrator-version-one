from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from argon2 import PasswordHasher
import os

# Database initializer
db = SQLAlchemy()

# Login Manager
login_manager = LoginManager()

# Password Hasher
ph = PasswordHasher(
    time_cost=int(os.getenv("TIMECOST")),
    memory_cost=int(os.getenv("MEMORYCOST")),
    parallelism=int(os.getenv("PARALLELISM")),
    hash_len=int(os.getenv("HASHLEN")),
    salt_len=int(os.getenv("SALTLEN"))
)
