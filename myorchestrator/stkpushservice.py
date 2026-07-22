import os
import requests






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
        # self.transaction_number = transaction_number
        # self.business_shortcode = business_short_code
        # self.amount = amount
        # self.account_ref = account_ref
        # self.transaction_desc = transaction_desc
        # self.access_token = ""
        # self.expires_at = 0

    def retrieve_access_token(self):

        token_request_response = requests.get(
            url= "https://sandbox.safaricom.co.ke/oauth/v1/generate",
            headers={
                "Authorization": f"Basic {os.getenv("DARAJABASICAUTHKEY")}"
            },
            params={
                "grant_type": "client_credentials"
            },
        )

        if token_request_response.status_code == 200:
            self.access_token = token_request_response.json()["access_token"]
            return self.access_token
        
        else:
            return token_request_response.json()["errorMessage"]



