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
    # print(column)
# print(dir(User.__table__))


print("------")

"""
Main file
"""

from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)

print("------")
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

find_user = my_db.find_user_by(email="test@test.com")
print(find_user.id)

try:
    find_user = my_db.find_user_by(email="test2@test.com")
    print(find_user)
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")
    
print("------")

"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

email = 'test@test.com'
hashed_password = "hashedPwd"

user = my_db.add_user(email, hashed_password)
print(user.id)

try:
    my_db.update_user(user.id, hashed_password='FakePwd')
    print("Password updated")
except ValueError:
    print("Error")

print("------")

"""
Main file
"""
from auth import _hash_password

print(_hash_password("Hello Holberton"))

print("------")

"""
Main file
"""
from auth import Auth

email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err)) 

print("------")

"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.valid_login(email, password))

print(auth.valid_login(email, "WrongPwd"))

print(auth.valid_login("unknown@email", password))


print("------")

import auth

uid = auth._generate_uuid()
print(uid)


# print("------")
# """
# Main file
# """
# from auth import Auth

# email = 'bob@bob.com'
# password = 'MyPwdOfBob'
# auth = Auth()

# auth.register_user(email, password)

# print(auth.create_session(email))
# print(auth.create_session("unknown@email.com"))


print("------")
"""
Main file
"""
from auth import Auth

email = 'newbob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

user = auth.register_user(email, password)

print(auth.create_session(email))
# column_values = {column.name: getattr(user, column.name) for column in user.__table__.columns}
# print(column_values)
print(auth.destroy_session(user.id))
# column_values = {column.name: getattr(user, column.name) for column in user.__table__.columns}
# print(column_values)
print("------")
