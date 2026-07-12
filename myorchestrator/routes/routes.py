import json
from pathlib import Path
from myorchestrator.email_service import EmailHandler
from myorchestrator.utilities.drafts import Drafts
from myorchestrator.utilities.tools import Tools
import time
from pprint import pprint
from myorchestrator.utilities.utilities import Utilities
from myorchestrator.utilities.notifications import NotificationHandler

tool = Tools()
utility = Utilities()
notification = NotificationHandler()


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

    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent.parent
        self.project_root = project_root

    @staticmethod
    def get_user():

        username = input("username: ").lower()
        phone_number = input("phone number:")
        email_address = input("email address:")
        password = input("password: ")

        phone_number = utility.canonicalize_phone_number(phone_number)
        otp_code = tool.generate_otp()

        verification_direction = int(
            input(
                "choose the direction you wish to take for verification: \n 1. sms \n 2. Whatsapp \n 3. email \n response: "
            )
        )

        if verification_direction == 1:

            sms = notification.sms_handler(contact=phone_number, otp_code=otp_code)
            sms

        elif verification_direction == 2:
            whatsapp = notification.whatsapp_handler(
                contact=phone_number, otp_code=otp_code
            )
            whatsapp

        return {
            "user_id": 1,
            "username": username,
            "phone_number": phone_number,
            "email_address": email_address,
            "password": password,
        }

    @staticmethod
    def get_otp_attempt():
        return input("enter the 5-digit code from your email: ")

    def user_signup(self):
        print("welcome to my system. Mi Casa, Su Casa.")
        print("signup")

        new_user = self.get_user()
        pprint(new_user)

        # if new_user:

        #     draft = Drafts(user=new_user, otp_type="OTP Verification", duration=5)

        #     time.sleep(1)
        #     print("\n Loading ...\n")

        #     email = EmailHandler(
        #         draft=draft, receiver_email=new_user.get("email_address")
        #     )

        #     forward_otp = email.send_otp()

        #     if forward_otp.get("success"):
        #         print(f"{forward_otp.get("message")}\n- check mail -\n")

        #         time.sleep(2)
        #         user_otp_attempt = self.get_otp_attempt()

        #         otp_verification = tool._verify_otp(
        #             _attempt=user_otp_attempt,
        #         )

        #         if otp_verification["success"]:

        #             verification_email = email.send_verification_email()
        #             pprint(verification_email)

        #             process_storage = self.store_user(
        #                 user_object=new_user, file_path=self.project_root / "vault/users/users.json"
        #             )

        #             if process_storage.get("status") == "success":
        #                 return "welcome home"

        #             else:
        #                 print(process_storage["error"])
        #                 return "internal error. kindly wait as we resolve your issue"

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
