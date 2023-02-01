from atm_class import ATM
from user_class import User
import json

f = open('users.json')
d = json.load(f)

print(d[0])
user = User(d[0]['user'], d[0]['user'], d[0]['pin'])
print(user.get_user_info())

f.close()

# app_user_one = User("user@email.com", "John", "123456")
# app_user_one.get_user_info()

# a = ATM()
# a.balance(app_user_one.pin)
# a.login(app_user_one.pin)
