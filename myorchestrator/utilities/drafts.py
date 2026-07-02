from .tools import Tools
from datetime import timedelta
from .tokens import TokenManager
from pathlib import Path 
from pprint import pprint


tool = Tools()


class Drafts:

    @staticmethod
    def create_token_object(user):
        token = TokenManager(user=user)
        return token


    def __init__(
        self,
        user,
        otp_type,
        duration
    ):
        self.user = user
        self._otp_type = otp_type
        self.duration = duration
        pprint(tool.timezoneinfo)
        self.timezone = tool.timezoneinfo["timezone"]
        self.local_time = tool.timezoneinfo["local_time"]
        self.project_root = Path(__file__).resolve().parent.parent.parent
        self.token_manager = self.create_token_object(user=self.user)



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

        subject = "OTP Verification"

        message = f"""
                        Dear Customer,
                        please use the following one-time password to verify your email
                        OTP: {otp}
                        if you did not request the otp, please ignore this email
        """

        return otp, expires_at, message, subject


    def _draft_verification_email(self):
        
        # generate access token
        # retrieve verification token and expiry 
        token, expires_at = self.token_manager.generate_access_token()

        # verification_link containing the verification token
        verification_link = f"https://a1cb-217-199-148-238.ngrok-free.app?token={token}"
        

        subject = "Email Verification"

        message = f"""
            use the following link to verify your email:

            {verification_link}

            This link will expire in 15 minutes

            If you did not request the link, please ignore this email
        """

        return verification_link, subject, message, expires_at
    

    def reset_password(self):
        pass