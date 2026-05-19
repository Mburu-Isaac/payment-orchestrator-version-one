from .geolocation import Location
from .tools import generate_otp
from datetime import timedelta
from .tokens import TokenManager
import json
from pathlib import Path 


location = Location(None)
timezoneinfo = location.get_user_timezone()


class Drafts:

    @staticmethod
    def store_otp(otp_data, file_path):
        
        with open(
            file_path,
            mode="w",
            encoding=("utf-8")) as file:

            json.dump(
                otp_data,
                file,
                indent=4,
                ensure_ascii=False
            )

    @staticmethod
    def load_otp(file_path):
        
        try:

            with open(file_path, mode="r", encoding=("utf-8")) as file:
                return json.load(file)

        except json.JSONDecodeError as e:
            print(f"unable to parse data: {e}")
            return {}

        except IOError as e:
            print(f"file I/O exception occured: {e}")
            return {}

    def __init__(
        self,
        user,
        otp_type,
        duration
    ):
        self.user = user
        self._otp_type = otp_type
        self.duration = duration
        self.timezone = timezoneinfo["timezone"]
        self.local_time = timezoneinfo["local_time"]
        self.project_root = Path(__file__).resolve().parent.parent.parent


    def _draft_otp(self):

        otp_data = {
            "otp":"",
            "expires_at":""
        }

        otp = generate_otp()
        expires_at = self.local_time + timedelta(minutes=self.duration)

        otp_data["otp"] = otp
        otp_data["expires_at"] = expires_at.strftime("%Y-%m-%d %H:%M:%S")

        self.store_otp(
            otp_data=otp_data,
            file_path=self.project_root/"vault/otps/otps.json"
        )

        message = f"""
                        Dear Customer,
                        please use the following one-time password to verify your email
                        OTP: {otp}
                        if you did not request the otp, please ignore this email
        """

        return otp, expires_at, message


    def _draft_verification_email(self):
        
        # generate access token
        token_manager = TokenManager(user=self.user) 
        token, expires_at = token_manager.generate_access_token()

        
        # retrieve verification token
        # retrieve token expiry

        # verification_link containing the verification token
        verification_link = f"link token validation?token={token}"
        

        subject = "Email Verification"

        message = f"""
            use the following link to verify your emil:

            {verification_link}

            This link will expire in 15 minutes

            If you did not request the link, please ignore this email
        """

        return verification_link, subject, message
    

    def reset_password(self):
        pass