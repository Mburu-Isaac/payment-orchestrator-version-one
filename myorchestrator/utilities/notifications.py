from smsmobileapi import SMSSender
import os
import requests


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

    def whatsapp_handler(
        self,
        contact,
        otp_code
    ):
        payload = {
            "recepients":f"{contact}",
            "message":f"Good evening. Enter the following otp for verification \n {otp_code}",
            "apikey": self.smsmobileapikey
        }
        
        response = requests.post(
            url="https://api.smsmobileapi.com/sendsms/waonly=yes",
            data=payload,
        )

        return response.text
