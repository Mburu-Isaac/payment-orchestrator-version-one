from smsmobileapi import SMSSender
import os
import requests


class NotificationHandler:

    @staticmethod
    def initialize_sms_sender(api_key):
        sms = SMSSender(api_key=api_key)
        return sms

    @staticmethod
    def source_templates(self):
        pass

    def __init__(self):
        self.smsmobileapikey = os.getenv("SMSMOBILEAPIKEY")

    def sms_handler(self, contact, otp):
        sms = self.initialize_sms_sender(api_key=self.smsmobileapikey)

        sms = sms.send_message(
            to=f"{contact}", message=f"Good evening. enter the following otp for verification. OTP: {otp}"
        )
        return sms
