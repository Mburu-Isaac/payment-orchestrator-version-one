from myorchestrator.routes.routes import Routes


authenticate_user = Routes()


print("Welcome to my fintech system")
intent = int(input("Is your intention to log in or sign up? \n enter (1) to sign up; (2) to login: "))

if intent == 1:
    print(authenticate_user.user_signup())
elif intent == 2:
    print(authenticate_user.login())
    



































