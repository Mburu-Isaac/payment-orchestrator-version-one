from .geolocation import Location
from .tools import generate_otp
from datetime import timedelta
from .tokens import TokenManager


location = Location(None)
timezoneinfo = location.get_user_timezone()


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


    def _draft_otp(self):
        otp = generate_otp()
        expires_at = self.local_time + timedelta(minutes=self.duration)

        message = f"""
                        Dear Customer,
                        please use the following one-time password to verify your email
                        OTP: {otp}
                        if you did not request the otp, please ignore this email
        """

        return otp, expires_at, message


    def _draft_verification_email(self):
        
        # generate access token
        token_manager = TokenManager(user="user") 
        token = token_manager.generate_access_token()

        
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