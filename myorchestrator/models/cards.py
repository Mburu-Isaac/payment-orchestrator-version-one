from ..extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Foreignkey, DateTime
from datetime import datetime






class Card(db.Model):

    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Foreignkey("users.id"), nullable=False)
    cardholdername: Mapped[str] = mapped_column(String(255), nullable=False, unique=False)
    primary_acc_number: Mapped[str] = mapped_column(String(255), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, unique=False)