# 1. Дану задачу робити через декоратор як функції!
# Написати декоратор який зробить з будь-якої функції строго типізовану. Тобо це декоратор який приймає аргументи.
# Аргументами будуть типи даних, порядок аргументів декоратору відповідає порядку аргументів функції
# Приклад:
# @decor(int, float, int, float)
# def func(1, 1.2, 4)
# Зверніть увагу що декоратор приймає на 1 аргумент більше ніж функція, останній аргумент це строга типізація того, що
# функція повертає
# можете написати власний ексепшин і кидати його тоді коли тип даних не відповідає тому, що очікується.

class InvalidType(Exception):
    pass


def decor(a1, a2, a3, a4):
    def dec(function):
        def wrap(z, x, c):
            try:
                if isinstance(z, a1) \
                        and isinstance(x, a2) \
                        and isinstance(c, a3) \
                        and isinstance(function(z, x, c), a4):
                    return function(z, x, c)
                else:
                    raise InvalidType
            except InvalidType:
                print("\tInvalid type. Excessive argument.")

        return wrap

    return dec


@decor(int, float, int, float)
def func(z, x, c):
    result = z * x * c
    return result


# Two output with exception and correct values.
#
# print(func(3, "somebody", 5))
print(func(3, 4.0, 5))