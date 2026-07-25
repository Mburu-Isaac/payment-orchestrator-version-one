from ..extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class User(db.Model):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    national_id_number: Mapped[str] = mapped_column(
        String(8), nullable=False, unique=True
    )
    transactions_number: Mapped[str] = mapped_column(
        String(20), nullable=False, unique=True
    )
    email: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=True
    )
    password: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=False
    )
    recovery_pin: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=False
    )

