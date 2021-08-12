# 2. Написати функцію яка приймає два катети і повертає значення гіпотензузи. Написати декоратор на функцію,
# який виводить на екран текст з довжиною катетів і гіпотенузи.
# Важливо! Функція повинно повернути саме значення гіпотенузи як число, а декоратор повинен зробити вивід на екран
# наприклад такого тексту “При катетах 3, 4 – гіпотенуза дорівнює 5”.

def decor_func(function):
    def wrap(a, b):
        action = function(a, b)
        print(f" При катетах {a}, {b} – гіпотенуза дорівнює {action}.")
        return action

    return wrap


@decor_func
def hyp(a, b):
    action = (a ** 2 + b ** 2) ** 0.5
    return int(action)


hyp(3, 4)