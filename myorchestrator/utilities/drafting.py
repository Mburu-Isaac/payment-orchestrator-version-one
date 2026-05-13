from myorchestrator.utilities.geolocation import Location
from myorchestrator.utilities.tools import generate_otp
from myorchestrator.utilities.notifications import NotificationHandler
from datetime import timedelta


location = Location(None)
timezoneinfo = location.get_user_timezone()
notification = NotificationHandler()
company_name = "ETERNITY"

class Drafts:

    def __init__(
        self,
        user,
        otp_type,
        email,
        duration
    ):
        self.user = user
        self._otp_type = otp_type
        self.email = email
        self.duration = duration
        self.timezone = timezoneinfo["timezone"]
        self.local_time = timezoneinfo["local_time"]


    def otp_verification(self):
        otp = generate_otp()
        expires_at = self.local_time + timedelta(minutes=self.duration)

        message = f"""
            Dear Customer, 
            please use the following one time password to verify your email address:
            OTP: {otp}
            if you did not request the OTP please ignore this email.
        """

        html_body = f"""
                    <html>
                        <body>
                            <p> Dear Customer, </p>
                            <p> Please use the following one time password to verify your email address: </p>

                            <h2> OTP: {otp} </h2> # add css styling

                            <p>

                                This OTP code will expire at <strong> { expires_at.strftime("%H:%M")} </strong>

                            </p>

                            <p> if you did not request the OTP please ignore this email. </p>

                            <p> 
                                Regards, 
                                <br>
                                {company_name} 
                            </p>
                        </body>
                    </html>
        """

        notification.email_handler(
            to_email=self.email,
            subject="OTP Verification",
            body=message,
            html_structure=html_body,
            company_name=company_name
        )

        return {
            "success":True,
            "otp":otp,
            "message":"OTP sent successfully"
        }


    def verification_email(self):
        pass

    def reset_password(self):
        pass