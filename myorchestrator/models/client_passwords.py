from myorchestrator.extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, ForeignKey
from datetime import datetime


class ClientPasswordHistory(db.Model):

    __tablename__ = "client_passwords"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    logged_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())
