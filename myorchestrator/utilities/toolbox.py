import secrets
import os



class ToolBox:

    def __init__(self):
        pass

    def generate_systems_otp(self):
        otp_characters = os.environ.get("CHARACTERS")
        otp = ''.join(secrets.choice(otp_characters) for _ in range(5))
        return otp


tb = ToolBox()
print(tb.generate_systems_otp())