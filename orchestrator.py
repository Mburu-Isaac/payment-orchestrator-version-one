# from myorchestrator.routes.routes import Routes


# authenticate_user = Routes()


# print("Welcome to my fintech system")
# intent = int(input("Is your intention to log in or sign up? \n enter (1) to sign up; (2) to login: "))

# if intent == 1:
#     print(authenticate_user.user_signup())
# elif intent == 2:
#     print(authenticate_user.login())


# from myorchestrator.utilities.geolocation import Location
# from pprint import pprint


# location = Location(user_ip=None)
# pprint(location.get_user_timezone())

# from myorchestrator.utilities.notifications import NotificationHandler
# from pprint import pprint

# notification = NotificationHandler()
# pprint(notification.sms_handler())

# from myorchestrator.stkpushservice import StkPushService
# import time

# mpesa = StkPushService()


# now = time.time()
# lapse_time = time.time() + 60

# while now < lapse_time:

#     time.sleep(2)
#     access_token = mpesa.initiate_stk_push()

#     print(access_token)

# from cryptography.fernet import Fernet

# fernet_key = Fernet.generate_key()
# print(fernet_key.decode())

from myorchestrator.extensions import db
from myorchestrator import launch_orchestrator
from myorchestrator.routes.auth import register_client


orchestrator = launch_orchestrator()
with orchestrator.app_context():
    # db.create_all()
    print(register_client())


print("data stored successfully")



