# 1 Task.
import logging


class Calculator:

    def __init__(self, num1, operation, num2):
        self.num1 = num1
        self.operation = operation
        self.num2 = num2

    def add(self):
        result_add = self.num1 + self.num2
        return print(f"{self.num1} + {self.num2} = {result_add}")

    def minus(self):
        result_minus = self.num1 - self.num2
        return print(f"{self.num1} - {self.num2} = {result_minus}")

    def mult(self):
        result_mult = self.num1 * self.num2
        return print(f"{self.num1} * {self.num2} = {result_mult}")

    def div(self):
        result_div = self.num1 / self.num2
        return print(f"{self.num1} / {self.num2} = {result_div}")

    def exponentiation(self):
        result_exponentiation = self.num1 ** self.num2
        return print(f"{self.num1} ** {self.num2} = {result_exponentiation}")

    def take_under_root(self):
        result_take_under_root = self.num1 ^ self.num2
        return print(f"{self.num1} ^ {self.num2} = {result_take_under_root}")

    def search_per_number(self):
        result_search_per_number = self.num1 % self.num2
        return print(f"{self.num1} % {self.num2} = {result_search_per_number}")


template = "%(levelname)s: %(filename)s: %(asctime)s - %(message)s"
logging.basicConfig(level=logging.INFO, filename="calculator.log", filemode="a", format=template)

while True:

    input_1 = input("Enter first number:")
    input_operation = input("Your action:")
    input_2 = input("Enter second number:")

    attributes = Calculator(input_1, input_operation, input_2)

    try:
        attributes.num1 = float(attributes.num1)
        attributes.num2 = float(attributes.num2)

        try:
            if input_operation == '+':
                attributes.add()
                logging.info("Action: '+'")

            elif input_operation == '-':
                attributes.minus()
                logging.info("Action: '-'")

            elif input_operation == '*':
                attributes.mult()
                logging.info("Action: '*'")

            elif input_operation == '/':
                attributes.div()
                logging.info("Action: '/'")

            elif input_operation == '**':
                attributes.exponentiation()
                logging.info("Action: '**'")

            elif input_operation == '^':
                attributes.take_under_root()
                logging.info("Action: '^'")

            elif input_operation == '%':
                attributes.search_per_number()
                logging.info("Action: '%'")

        except ZeroDivisionError:
            logging.error("Error. Division on zero can't.")
            print("Error. Division on '0' can't.")

    except ValueError:
        logging.error("Error. Not input value.")
        print("Not input value.")

# # 2 Task.
# Version 1. Then when try-except outside.
#
# from random import randrange
# import time
#
#
# class RobotVacuumCleaner:
#
#     def __init__(self, battery_charge, capacity_garbage, amount_of_water):
#         self.battery_charge = battery_charge
#         self.capacity_garbage = capacity_garbage
#         self.amount_of_water = amount_of_water
#
#     def move(self):
#         self.battery_charge -= 10
#         print("Robot Vacuum Cleaner move")
#
#         if self.battery_charge <= 0:
#             raise BatteryDischarged
#
#         if self.battery_charge <= 20:
#             raise BatteryLow
#
#         if self.amount_of_water >= 0:
#             self.wash()
#         else:
#             raise EmptyWater
#
#         if self.capacity_garbage <= 100:
#             self.vacuum_cleaner()
#         else:
#             raise FullCapacityGarbage
#
#         time.sleep(1)
#         print("___________________________________________")
#
#     def wash(self):
#         self.amount_of_water -= randrange(0, 10)
#         print("wash")
#
#         if self.amount_of_water <= 0:
#             raise EmptyWater
#
#         time.sleep(1)
#
#     def vacuum_cleaner(self):
#         self.capacity_garbage += randrange(0, 10)
#         print("cleaning")
#
#         if 80 < self.capacity_garbage < 100:
#             raise HighCapacityGarbage
#
#         elif self.capacity_garbage >= 100:
#             raise FullCapacityGarbage
#
#         time.sleep(1)
#
#
# class BatteryLow(Exception):
#     pass
#
#
# class BatteryDischarged(Exception):
#     pass
#
#
# class EmptyWater(Exception):
#     pass
#
#
# class HighCapacityGarbage(Exception):
#     pass
#
#
# class FullCapacityGarbage(Exception):
#     pass
#
#
# the_cleaning = RobotVacuumCleaner(randrange(0, 100), randrange(0, 100), randrange(0, 100))
#
# while True:
#     try:
#         print(
#             f"Charge:{the_cleaning.battery_charge}, Water:{the_cleaning.amount_of_water}, "
#             f"Garbage:{the_cleaning.capacity_garbage} ")
#         the_cleaning.move()
#
#     except EmptyWater:
#         print("Have not water.")
#         break
#
#     except HighCapacityGarbage:
#         print("Already 80% garbage.")
#
#     except FullCapacityGarbage:
#         print("The full bucket! Clean")
#         break
#
#     except BatteryLow:
#         print("The battery less 20%.")
#
#     except BatteryDischarged:
#         print("Robot Vacuum Cleaner discharged. Put in charge.")
#         break

# 2 Task.
# Version 2. Then when try-except inside.

from random import randrange
import time


class RobotVacuumCleaner:

    def __init__(self, battery_charge, capacity_garbage, amount_of_water):
        self.battery_charge = battery_charge
        self.capacity_garbage = capacity_garbage
        self.amount_of_water = amount_of_water

    def move(self):

        while True:
            self.vacuum_cleaner()
            self.wash()
            try:
                self.battery_charge -= 10
                print("Robot Vacuum Cleaner move")

                if self.battery_charge <= 0:
                    raise BatteryDischarged

                if self.battery_charge <= 20:
                    raise BatteryLow

            except BatteryLow:
                print("The battery less 20%.")
            except BatteryDischarged:
                print("Robot Vacuum Cleaner discharged. Put in charge.")
                break

            print("___________________________________________")
            time.sleep(1)

    def wash(self):
        try:
            self.amount_of_water -= randrange(0, 10)
            print("wash")

            if self.amount_of_water <= 0:
                raise EmptyWater

        except EmptyWater:
            print("Have not water.")

    time.sleep(1)

    def vacuum_cleaner(self):
        try:
            self.capacity_garbage += randrange(0, 10)
            print("cleaning")

            if 80 < self.capacity_garbage < 100:
                raise HighCapacityGarbage

            elif self.capacity_garbage >= 100:
                raise FullCapacityGarbage

        except HighCapacityGarbage:
            print("Already 80% garbage.")
        except FullCapacityGarbage:
            print("The full bucket! Clean")

    time.sleep(1)


class BatteryLow(Exception):
    pass


class BatteryDischarged(Exception):
    pass


class EmptyWater(Exception):
    pass


class HighCapacityGarbage(Exception):
    pass


class FullCapacityGarbage(Exception):
    pass


the_cleaning = RobotVacuumCleaner(randrange(0, 100), randrange(0, 100), randrange(0, 100))

print(f"Charge:{the_cleaning.battery_charge}, Water:{the_cleaning.amount_of_water}, "
      f"Garbage:{the_cleaning.capacity_garbage} ")

the_cleaning.move()





