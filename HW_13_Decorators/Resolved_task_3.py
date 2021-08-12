# 3. Написати функцію яка приймає список елементів і знаходить суму, до функції написати декоратор який перед тим як
# запустити функцію видаляє з списку всі не чисельні типи даних, але якщо є строка яку можна перевести в число,
# (наприклад “1”) то строка приводиться до чисельного типу даних.
#
def dec(func):
    def wrap(list_):
        print("Old list:", list_)
        new_list = []
        for x in list_:
            try:
                new_list.append(float(x)) if type(x) != int else new_list.append(x)
            except (ValueError, TypeError):
                continue
        return func(new_list)

    return wrap


@dec
def element_in_lists(list_update):
    print("New list:", list_update)
    return print(sum(list_update))


anybody_list = [1, 2.2, 3, 4, "anybody", 4.8, 5, "5"]
element_in_lists(anybody_list)