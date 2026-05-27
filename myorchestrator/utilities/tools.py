import secrets
import os
import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from .geolocation import Location
import urllib.parse
from .tokens import TokenManager


location = Location(None)

class Tools:

    def __init__(self):
        self.length = 5
        self.file_path = Path(__file__).resolve().parent.parent.parent/"vault/otps/otps.json"
        self.encoding = "utf-8"
        self.timezoneinfo = location.get_user_timezone()

    def generate_otp(self):
        return ''.join(secrets.choice(os.environ.get("CHARACTERS")) for _ in range(self.length))


    def store_otp(self, otp_data, file_path):
        
        with open(file_path, mode="w",encoding=(self.encoding)) as file:

            json.dump(
                otp_data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def _load_stored_otp(self):
            
        try:

            with open(self.file_path, mode="r", encoding=(self.encoding)) as file:
                return json.load(file)

        except json.JSONDecodeError as e:
            print(f"unable to parse data: {e}")
            return {}

        except IOError as e:
            print(f"file I/O exception occured: {e}")
            return {}

    def _verify_otp(
        self,
        _attempt,
    ):

        stored_otp = self._load_stored_otp()

        otp_expiry = datetime.strptime(stored_otp.get("expires_at"), "%Y-%m-%d %H:%M:%S")

        current_regional_time_string = datetime.now(
            tz=ZoneInfo(self.timezoneinfo["timezone"])
        ).strftime("%Y-%m-%d %H:%M:%S")


        current_regional_time = datetime.strptime(
            current_regional_time_string,
            "%Y-%m-%d %H:%M:%S"
        )

        

        if otp_expiry < current_regional_time :
            return {
                "success":False,
                "message": "OTP expired - request new OTP -"
            }
           
        if _attempt == stored_otp.get("otp"):
            dispensed = self._delete_used_otp()
            return {
                "success":True,
                "message":dispensed
            }

    def _delete_used_otp(self):

        with open(self.file_path, mode="r", encoding=(self.encoding)):
            pass
        
        return "otp dispensed - cannot be reused -"

    def intercept_ngrok_link(self, ngrok_url):

        token_manager = TokenManager()
        
        parsed_url = urllib.parse.urlparse(ngrok_url)
        query_parameters = urllib.parse.parse_qs(parsed_url.query)

        token_parameter = query_parameters.get("token", [])
        verification_token = token_parameter[0]

        verify_email_token = token_manager.validate_access_token(
            token=verification_token
        )

        return verify_email_token



