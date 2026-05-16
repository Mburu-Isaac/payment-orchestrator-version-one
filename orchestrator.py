from myorchestrator.email_service import EmailHandler
from myorchestrator.utilities.drafts import Drafts


new_user = {
    "user_id":"",
    "username":"",
    "phone_number":"",
    "email_address":"",
    "password":"",
}

print("User Signup")

new_user["username"] = input("username: ").lower()
new_user["phone_number"] = input("phone number: ")
new_user["email_address"] = input("email address:")
new_user["password"] = input("password: ")


if new_user:
    
    draft = Drafts(
        user=new_user.get("username"),
        otp_type="OTP Verification",
        duration=5
    )
    email = EmailHandler(
        draft=draft,
        receiver_email=new_user.get("email_address")
    )

    print(email.send_otp())








