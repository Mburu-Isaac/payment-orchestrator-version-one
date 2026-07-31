from ..extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Boolean
from myorchestrator.extensions import login_manager
from datetime import datetime, timezone


class Client(db.Model):

    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    national_id_number: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=True
    )
    primary_number: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
    transactions_number: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False, unique=False)
    recovery_pin: Mapped[str] = mapped_column(String(255), nullable=False, unique=False)
    client_fingerprint: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=True
    )
    joined_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    verified: Mapped[bool] = mapped_column(
        Boolean, default=False
    )

    client_password_history = db.relationship(
        "ClientPasswordHistory",
        backref="client",
        lazy=True,
        cascade="all, delete-orphan"
    )

    client_otp = db.relationship(
        "ClientOTP",
        backref="client",
        lazy=True,
        cascade="all, delete-orphan"
    )


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Client, int(user_id))
