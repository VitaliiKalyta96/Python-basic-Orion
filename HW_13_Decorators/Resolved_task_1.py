# 1. Написати функцію яка в циклі зчитує з консолі введені користувачем дані і записує їх в список.
# Написати декоратор який видасть час виконання роботи функції.
#
from time import time


def time_check(func):
    def wrap(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        print(time() - t1)
        return result

    return wrap


@time_check
def input_data():
    new_list = []
    x = input("Enter number:")
    new_list.append(x)
    print(new_list)


input_data()