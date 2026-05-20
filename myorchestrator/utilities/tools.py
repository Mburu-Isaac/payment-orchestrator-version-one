import secrets
import os
import json
from pathlib import Path


class Tools:

    def __init__(self):
        self.length = 5
        self.file_path = Path(__file__).resolve().parent.parent.parent/"vault/otps/otps.json"
        self.encoding = "utf-8"

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

    def _delete_used_otp(self):

        os.remove(self.file_path)
        return "otp dispensed - cannot be reused -"