# 1. Написати програму яка буде зберігати username і email в файл json.
# При наявності користувачів перед тим як додати юзера програма повинна перевірити
# чи не існує на данний момент користувача з таким username і email,
# якщо існує вивести помилку.

import json


class BadValue(Exception):
    pass


class ExistValue(Exception):
    pass


def input_names(u, m):
    result = {"username": u, "email": m}
    return result


list_values_users = []

while True:
    try:
        record_inform = input("Enter value username:\t")
        record_inform_2 = input("Enter value email:\t")
        if record_inform[0] == 'value' or record_inform_2[1] == 'value':
            break
        for x in list_values_users:
            if x['username'] != record_inform[0] or x["email"] != record_inform_2[1]:
                list_values_users.append(input_names(record_inform[0], record_inform_2[1]))
            else:
                raise BadValue
    except ExistValue:
        print("To exist same values.")

users = json.dumps(list_values_users)

with open("HW_15.json", "w") as file:
    file.write(users)

with open("HW_15.json", "r") as file:
    json_obj = file.readlines()

# py HW_15_Argument_parser_serialization.py