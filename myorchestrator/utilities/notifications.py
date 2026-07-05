from smsmobileapi import SMSSender
import os


class NotificationHandler:

    @staticmethod
    def initialize_sms_sender(api_key):
        sms = SMSSender(api_key=api_key)
        return sms

    def __init__(self):
        self.smsmobileapikey = os.getenv("SMSMOBILEAPIKEY")

    def sms_handler(self):
        sms = self.initialize_sms_sender(api_key=self.smsmobileapikey)
        return sms.send_message(
            to="+254743277087", message="Hello from this other side"
        )
