from smsmobileapi import SMSSender
import os


class NotificationHandler:

    @staticmethod
    def initialize_sms_sender(api_key):
        sms = SMSSender(api_key=api_key)
        return sms

    def __init__(self):
        self.smsmobileapikey = os.getenv("SMSMOBILEAPIKEY")

    def sms_handler(
        self,
        contact,
        otp_code
    ):
        sms = self.initialize_sms_sender(api_key=self.smsmobileapikey)
        return sms.send_message(
            to=f"{contact}", message=f"Good evening. Enter the following otp for verification \n {otp_code}"
        )
