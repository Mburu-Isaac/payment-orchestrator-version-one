import os
import requests
import time






class StkPushService:

    def __init__(
        self,
        # transaction_number,
        # business_short_code,
        # amount,
        # account_ref,
        # transaction_desc
    ):
        self.consumer_key = os.getenv("DARAJACONSUMERKEY")
        self.consumer_secret = os.getenv("DARAJACONSUMERSECRET")
        self.access_token = ""
        self.expires_at = 0
        # self.transaction_number = transaction_number
        # self.business_shortcode = business_short_code
        # self.amount = amount
        # self.account_ref = account_ref
        # self.transaction_desc = transaction_desc

    def retrieve_access_token(self):

        request_response = requests.get(
            url= "https://sandbox.safaricom.co.ke/oauth/v1/generate",
            headers={
                "Authorization": f"Basic {os.getenv("DARAJABASICAUTHKEY")}"
            },
            params={
                "grant_type": "client_credentials"
            },
        )

        if request_response.status_code == 200:
            self.access_token = request_response.json()["access_token"]
            self.expires_at = (time.time() + int(request_response.json()["expires_in"]) - 45)
            return self.access_token
        else:
            return request_response.json()["errorMessage"]



