from .geolocation import Location
from .tools import generate_otp
from .notifications import NotificationHandler
from datetime import timedelta


location = Location(None)
timezoneinfo = location.get_user_timezone()
notification = NotificationHandler()


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


    def _generate_otp(self):
        otp = generate_otp()
        expires_at = self.local_time + timedelta(minutes=self.duration)

        message = f"""
                        Dear Customer,
                        please use the following one-time password to verify your email
                        OTP: {otp}
                        if you did not request the otp, please ignore this email
        """

        return otp, expires_at, message


    def verification_email(self):
        pass

    def reset_password(self):
        pass