from myorchestrator.extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, DateTime
from datetime import datetime, timezone



class ClientOTP(db.Model):
    
    __tablename__ = "otps"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    otp: Mapped[str] = mapped_column(String(255), nullable=False)
    otp_type: Mapped[str] = mapped_column(String(30), nullable=False, default="login")
    expires_at: Mapped [DateTime] = mapped_column(DateTime(timezone=True))
    created_at: Mapped [DateTime] = mapped_column(DateTime(timezone=True))