import json
from pathlib import Path
from myorchestrator.email_service import EmailHandler
from myorchestrator.utilities.drafts import Drafts


class Routes:

    @staticmethod
    def store_user(user_object, file_path):

        try:
            with open(file_path, mode="w", encoding="utf-8") as file:

                json.dump(user_object, file, indent=4, ensure_ascii=False)

            return {"status": "success", "feedback": f"data stored at {file_path}"}

        except Exception as e:
            return {"status": "failed", "error": f"seriarization failed: {e}"}

        except IOError as ioe:
            return {"status": "failed", "error": f"file I/O exception occured: {ioe}"}

    @staticmethod
    def load_user(file_path):

        try:

            with open(file_path, mode="r", encoding=("utf-8")) as file:
                return json.load(file)

        except json.JSONDecodeError as e:
            print(f"unable to parse data: {e}")
            return {}

        except IOError as e:
            print(f"file I/O exception occured: {e}")
            return {}

    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent.parent
        self.project_root = project_root

    def user_signup(self):
        print("welcome to my system. Mi Casa, Su Casa.")
        print("signup")

        new_user = {
            "user_id": 1,
            "username": input("username: ").lower(),
            "phone_number": input("phone number:"),
            "email_address": input("email address:"),
            "password": input("password: "),
        }

        if new_user:

            draft = Drafts(user=new_user, otp_type="OTP Verification", duration=5)
            email = EmailHandler(
                draft=draft, receiver_email=new_user.get("email_address")
            )

            print(email.send_otp())

        process_storage = self.store_user(
            user_object=new_user, file_path=self.project_root / "vault/users/users.json"
        )

        if process_storage.get("status") == "success":
            return "welcome home"

        else:
            print(process_storage["error"])
            return "internal error. kindly wait as we resolve your issue"

    def login(self):

        print("hello again.")

        email = input("enter your email: ").lower()
        password = input("verify password: ")

        user_details = self.load_user(self.project_root / "vault/users/users.json")
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


#     verification_email = draft._draft_verification_email()
#     pprint(verification_email)
