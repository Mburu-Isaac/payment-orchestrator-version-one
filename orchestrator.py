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

        return {
            "status":"success",
            "feedback":f"data stored at {FILE_PATH}"
        }

    except Exception as e:
        return {
            "status":"failed", 
            "error": f"seriarization failed: {e}"
        }

    except IOError as ioe:
        return {
            "status":"failed",
            "error":f"file I/O exception occured: {ioe}"
        }

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

def user_signup():
    print("welcome to my system. Mi Casa, Su Casa.")
    print("signup")

    new_user = {
        "user_id":1,
        "username":input("username: ").lower(),
        "phone_number":input("phone number:"),
        "email_address":input("email address:"),
        "password":input("password: "),
    }

    process_storage = store_user(new_user)

    if process_storage.get("status") == "success":
        return "welcome home"

    else:
        print(process_storage["error"])
        return "internal error. kindly wait as we resolve your issue"

def login():

    print("hello again.")
    
    email = input("enter your email: ").lower()
    password = input("verify password: ")


    user_details = load_user()
    stored_address = user_details.get("email_address") if user_details else None
    stored_password = user_details.get("password") if user_details else None

    if email == "":
        return "email required"
    
    if email != stored_address:
        return "email does not exist in our files \n - ensure email entered is correct -"


    if email == stored_address:


        if password == "":
            return "you require your password for validation"

        if password != stored_password:
            return "try again"

        if stored_password == password:
            return "good to have you back"

    


print("Welcome to my fintech system")
intent = int(input("Is your intention to log in or sign up? \n enter (1) to sign up; (2) to login: "))

if intent == 1:
    print(user_signup())
elif intent == 2:
    print(login())



































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
