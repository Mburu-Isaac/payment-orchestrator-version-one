import os
import requests
import time
import datetime
import base64






class StkPushService:

    def __init__(
        self,
        business_short_code,
        amount,
        transaction_number,
        account_ref,
        transaction_desc
    ):
        self.consumer_key = os.getenv("DARAJACONSUMERKEY")
        self.consumer_secret = os.getenv("DARAJACONSUMERSECRET")
        self.access_token = ""
        self.expires_at = 0
        self.business_shortcode = business_short_code
        self.transaction_type = "transaction_type"
        self.amount = amount
        self.transaction_number = transaction_number
        self.account_ref = account_ref
        self.transaction_desc = transaction_desc

    def retrieve_access_token(self):

        try:

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
        
        except KeyError:
            return "No json was returned"


    def token_cache(self):
        
        if time.time() < self.expires_at:
            return self.access_token
        
        else:
            return self.retrieve_access_token()
            

    def initiate_stk_push(self):

        return self.token_cache()

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        encode_bytes = base64.b64encode(
            f'{self.business_short_code}'
        )

        password = encode_bytes.decode("utf-8")

        stkpush_response = requests.post(
            
            url="",
            headers={
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json"
            },
            json={
                "BusinessShortCode": self.business_shortcode,
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": self.transaction_type,
                "Amount": self.amount,
                "PartyA": self.transaction_number,
                "PartyB": self.business_shortcode,
                "PhoneNumber": self.mpesa_contact,
                "CallBackURL":"",
                "AccountRefernce": self.account_ref,
                "TransactionDesc": self.transaction_desc
            }
        )
        
        



