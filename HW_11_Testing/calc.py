class Calc:
    @staticmethod
    def sum(a, b):
        """ Функція для додавання чисел
        >>> Calc.sum(20, 10)
        30.0

        :param a: Число перше для додавання, може бути як int так і float
        :param b: Число друге для додавання, може бути як int так і float
        :return: Повертає суму при додаванні чисел
        """
        return a + b

    @staticmethod
    def minus(a, b):
        """ Функція для віднімання чисел
        >>> Calc.minus(20, 10)
        10.0

        :param a: Число перше, може бути як int так і float
        :param b: Число друге, може бути як int так і float
        :return: Повертає суму при відінманні чисел
        """
        return a - b

    @staticmethod
    def mul(a, b):
        """ Функція для множення чисел
        >>> Calc.mul(20, 10)
        200.0

        :param a: Число перше, може бути як int так і float
        :param b: Число друге, може бути як int так і float
        :return: Повертає суму при множенні чисел
        """
        return a * b

    @staticmethod
    def div(a, b):
        """ Функція для ділення чисел
        >>> Calc.div(20, 10)
        2.0

        :param a: Число перше, може бути як int так і float
        :param b: Число перше, може бути як int так і float
        :return: Повертає суму при діленні чисел
        """
        return a / b

    @staticmethod
    def pow(a, b):
        """ Функція для піднесення до степені чисел
        >>> Calc.pow(7, 2)
        49.0

        :param a: число перше
        :param b: число друге підноситься до степені до числа першого
        :return: повертає загальне перше число з-під степеня другого числа
        """
        return pow(a, b)

    @staticmethod
    def sqrt(a, b) -> float:
        """ Функція для кореня чисел
        >>> Calc.sqrt(6, 3)
        1.82

        :param a: число перше, має бути інт
        :param b: число друге, має бути інт
        :return: повертає результат від виконання функції
        """
        return round(a ** (1 / b), 2)

    @staticmethod
    def per_from_number(a, b) -> float:
        """ Функція для вирахування відсотка від числа
        >>> Calc.per_from_number(7, 4)
        0.28

        :param a: Перше значення числа
        :param b: Друге значення числа
        :return: Повертає відсоток від двох чисел
        """
        return (a * b) / 100

