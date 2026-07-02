





class Utilities:

    def __init__(self):
        pass

    def canonicalize_phone_number(self, phone_number):
        if phone_number.startswith("0"):
            phone_number = "+254" + phone_number[1:]

        return phone_number