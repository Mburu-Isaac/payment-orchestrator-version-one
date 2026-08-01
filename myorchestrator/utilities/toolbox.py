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

        try:
            if len(data) == 1:
                db.session.add(data[0])
                db.session.flush()
            else:
                db.session.add_all(data)

            db.session.commit()
            return True

        except Exception:
            db.session.rollback()
            raise

    def conditional_read(
        self,
        model_name,
        intended_value,
        multiple_value_return=False
    ):
        
    
        if not multiple_value_return:
            
            return_object = db.session.execute(
                db.select(model_name).where(
                    model_name.field == intended_value
                )
            ).scalar()

            return return_object

        else:

            return_object = db.session.execute(
                db.select(model_name).where(
                    model_name.field == intended_value
                )
            ).scalar()

            return return_object





