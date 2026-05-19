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
            json.dumps(data, file, indent=4, ensure_ascii=False)

        print(f"data stored at {FILE_PATH}")

    except Exception as e:
        raise f"seriarization failed: {e}"

    except IOError as ioe:
        raise f"file I/O exception occured: {ioe}"



# new_user = {
#     "user_id":"",
#     "username":"",
#     "phone_number":"",
#     "email_address":"",
#     "password":"",
# }

# print("User Signup")

# new_user["username"] = input("username: ").lower()
# new_user["phone_number"] = input("phone number: ")
# new_user["email_address"] = input("email address:")
# new_user["password"] = input("password: ")


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
