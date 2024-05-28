#!/usr/bin/env python3
"""
Main file
"""
from user import User
import pprint

print(User.__tablename__)
# # print(dir(User))
# user1 = User(email='abc@gmail.com')
# # print(f'user1 dir - {dir(user1)}')
# pprint.pprint(dir(user1))
# # print(user1.email)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))

print("------")


print("------")

"""
Main file
"""

from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test2@test.com", "SuperHashedPwd2")
print(user_1.id)
print(user_1.email)
print(user_1.hashed_password)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)
print(user_2.email)
print(user_2.hashed_password)