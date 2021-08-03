# 4. Написати функцію яка приймає на вхід ціле число n створює і повертає список цілих чисел від 0 до n.
# Написати до цієї функції декоратор який всі елементи отриманого списку переведе в строковий тип даних.
#
#
def decor(function):
    def wrap(n):
        result = function(n)
        new_list = [str(x) for x in result]
        return new_list

    return wrap


@decor
def new_str_list(z):
    return [i for i in range(z)]


print(new_str_list(5))