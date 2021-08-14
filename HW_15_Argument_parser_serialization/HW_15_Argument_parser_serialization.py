# 1. Написати програму яка буде зберігати username і email в файл json.
# При наявності користувачів перед тим як додати юзера програма повинна перевірити
# чи не існує на данний момент користувача з таким username і email,
# якщо існує вивести помилку.

import argparse
import json


class ExistUsernameValue(Exception):
    pass


class ExistEmailValue(Exception):
    pass


parser = argparse.ArgumentParser()
parser.add_argument("--username", help="Enter username: ")
parser.add_argument("--email", help="Enter email: ")

arguments = parser.parse_args()
user_dict = {}

if arguments.username:
    user_dict["username"] = arguments.username

if arguments.email:
    user_dict["email"] = arguments.email

with open("users.json", 'r') as file:
    user_data = json.loads(file.readline())

try:
    for user in user_data:
        if user["username"] == user_dict["username"]:
            raise ExistUsernameValue
        elif user["email"] == user_dict["email"]:
            raise ExistEmailValue

    user_data.append(user_dict)

except ExistUsernameValue:
    print("Username already exist! To change him.")

except ExistEmailValue:
    print("Email already exist! To change him.")

with open("users.json", 'w') as file:
    file.write(json.dumps(user_data))

"""Instruction."""
# To record username and email do with help console and in file json must have "[]" for correct record.

# py HW_15_Argument_parser_serialization.py --username Vitalii --email vitalii@gmail
# py HW_15_Argument_parser_serialization.py --username Vitalik --email vitalik@gmail