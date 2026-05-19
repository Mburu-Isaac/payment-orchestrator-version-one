from myorchestrator.email_service import EmailHandler
from myorchestrator.utilities.drafts import Drafts
from myorchestrator.routes.routes import Routes


authenticate_user = Routes()


print("Welcome to my fintech system")
intent = int(input("Is your intention to log in or sign up? \n enter (1) to sign up; (2) to login: "))

if intent == 1:
    print(authenticate_user.user_signup())
elif intent == 2:
    print(authenticate_user.login())
    



































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
