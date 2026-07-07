from myorchestrator.routes.routes import Routes


authenticate_user = Routes()


print("Welcome to my fintech system")
intent = int(input("Is your intention to log in or sign up? \n enter (1) to sign up; (2) to login: "))

if intent == 1:
    print(authenticate_user.user_signup())
elif intent == 2:
    print(authenticate_user.login())
    

# from myorchestrator.utilities.geolocation import Location
# from pprint import pprint


# location = Location(user_ip=None)
# pprint(location.get_user_timezone())


# from myorchestrator.utilities.notifications import NotificationHandler
# from myorchestrator.utilities.tools import Tools
# from pprint import pprint

# tool = Tools()
# contact = "+254743277087"
# otp = tool.generate_otp()

# notification = NotificationHandler()
# pprint(
#     notification.sms_handler(
#         contact=contact,
#         otp=otp
#     )
# )





































