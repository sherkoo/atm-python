from user_class import User

u1 = User("user@email.com", "John", "4566")


class ATM:

    def login(self, password):
        user_input = input("Enter your password? ____ ")
        if (user_input == password):
            print("logged in!")
            print(f"Welcome {u1.name}!")

        else:
            print('wrong password')

    def balance(self, balance):
        print(f"Your balance is {balance}")
