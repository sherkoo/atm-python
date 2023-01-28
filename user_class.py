class User:
    def __init__(self, user_email, name, pin):
        self.user_email = user_email
        self.name = name
        self.pin = pin

    def change_pin(self, new_pin):
        self.pin = new_pin

    def get_user_info(self):
        print(
            f"Welcome {self.name}, What would you like to do today? /n • Check Balance /n • Withdrawl")
