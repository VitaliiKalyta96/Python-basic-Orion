# 1. Написати функцію яка в циклі зчитує з консолі введені користувачем дані і записує їх в список.
# Написати декоратор який видасть час виконання роботи функції.
#
from time import sleep, time


def user(*args):
    def count(func):
        def wrap(list_):
            new_list = []
            y = input("Enter number:")
            for x in list_:
                if isinstance(x, args):
                    new_list.append(y)
            result = func(new_list)
            return result
        return wrap
    return count


def time_check(func):
    def wrap(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        print(time() - t1)
        return result
    return wrap


@user(int, float)
@time_check
def input_data(list_):
    sleep(1)
    return list_

print(input_data([1]))