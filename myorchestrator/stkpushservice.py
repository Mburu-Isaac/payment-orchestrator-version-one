import os






class StkPushService:

    def __init__(
        self,
        transaction_number,
        business_short_code,
        amount,
        account_ref,
        transaction_desc
    ):
        self.consumer_key = os.getenv("DARAJACONSUMERKEY")
        self.consumer_secret = os.getenv("DARAJACONSUMERSECRET")
        self.transaction_number = transaction_number
        self.business_shortcode = business_short_code
        self.amount = amount
        self.account_ref = account_ref
        self.transaction_desc = transaction_desc

    def retrieve_access_token(self):
        pass