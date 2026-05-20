from .geolocation import Location
from .tools import Tools
from datetime import timedelta
from .tokens import TokenManager
import json
from pathlib import Path 


location = Location(None)
timezoneinfo = location.get_user_timezone()

tool = Tools()


class Drafts:


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

        otp = tool.generate_otp()
        expires_at = self.local_time + timedelta(minutes=self.duration)

        otp_data["otp"] = otp
        otp_data["expires_at"] = expires_at.strftime("%Y-%m-%d %H:%M:%S")

        tool.store_otp(
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