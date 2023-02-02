from classes.atm_class import ATM
from classes.user_class import User

user = User('Stephen')
user.welcome()

atm = ATM("us", 123)
atm.check_balance()
atm.withdrawl(12)
atm.check_balance()
atm.deposit(432)
atm.check_balance()
