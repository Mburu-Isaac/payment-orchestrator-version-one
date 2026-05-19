from myorchestrator.email_service import EmailHandler
from myorchestrator.utilities.drafts import Drafts
from pprint import pprint
import json
from pathlib import Path

project_root = Path(__file__).resolve().parent
FILE_PATH = project_root / "vault/users.json"


def store_user(data):

    try:
        with open(FILE_PATH, mode="w", encoding="utf-8") as file:          
            
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"data stored at {FILE_PATH}")

    except Exception as e:
        print(f"seriarization failed: {e}")

    except IOError as ioe:
        print(f"file I/O exception occured: {ioe}")

def load_user():

    try:
        
        with open(FILE_PATH, mode="r", encoding=("utf-8")) as file:
            return json.load(file)

    except json.JSONDecodeError as e:
        print(f"unable to parse data: {e}")
        return {}

    except IOError as e:
        print(f"file I/O exception occured: {e}")
        return {}


new_user = {
    "user_id":1,
    "username":input("username: ").lower(),
    "phone_number":input("phone number:"),
    "email_address":input("email address:"),
    "password":input("password: "),
}

store_user(new_user)



# if new_user:

#     draft = Drafts(
#         user=new_user,
#         otp_type="OTP Verification",
#         duration=5
#     )
#     email = EmailHandler(
#         draft=draft,
#         receiver_email=new_user.get("email_address")
#     )

#     print(email.send_otp())

#     verification_email = draft._draft_verification_email()
#     pprint(verification_email)
