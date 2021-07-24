# Task 1.

import logging


class Calculator(Exception):
    #  to created endless cycle
    a = 0
    b = 1
    while a <= b:
        b += 1
        a += 1

    template = "%(levelname)s: %(filename)s: %(asctime)s - %(message)s"
    logging.basicConfig(level=logging.ERROR, filename="log.log", filemode="a", format=template)

# To created methods calculator.
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        try:
            c = a / b
            return c
        # The catch error if will be to.
        except ZeroDivisionError:
            logging.error("Error. Zero")
            # print("This file can't divide on o")

    @staticmethod
    def exponentiation(a, b):
        return a ** b

    @staticmethod
    def take_under_root(a, b):
        return a ^ b

    @staticmethod
    def search_per_number(a, b):
        return a % b

print(Calculator.add)
# print(Calculator.minus)
# print(Calculator.mul)
print(Calculator.div)
# print(Calculator.exponentiation)
# print(Calculator.take_under_root)
# print(Calculator.search_per_number)

""" Why this code nothing not output?? What I'm doing to go wrong?"""