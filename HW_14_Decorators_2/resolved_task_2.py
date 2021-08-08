# 2. Те ж саме що й в завданні 1, але зробити через функтор.


class InvalidType(Exception):
    pass


class DecorModern:
    def __init__(self, a1, a2, a3, a4):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4

    def __call__(self, function):
        def wrap(z, x, c):
            try:
                if isinstance(z, self.a1) \
                        and isinstance(x, self.a2) \
                        and isinstance(c, self.a3) \
                        and isinstance(function(z, x, c), self.a4):
                    return function(z, x, c)
                else:
                    raise InvalidType
            except InvalidType:
                print("\tInvalid type. Excessive argument.")

        return wrap


@DecorModern(int, float, int, float)
def func(z, x, c):
    result = z * x * c
    return result


# Two output with exception and correct values.

# print(func(3, "somebody", 5))
print(func(3, 4.0, 5))