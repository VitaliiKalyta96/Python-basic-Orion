# 1.
""" Make the class with composition."""
class Laptop:
    def __init__(self):
        battery_1 = Battery('4000 mAh')
        battery_2 = Battery('5000 mAh')
        self.batteries = [battery_1, battery_2]

class Battery:
    def __init__(self, charge):
        self.charge = charge

laptop = Laptop


# 2.
""" Make the class with aggregation """
class Guitar:
    def __init__(self, guitarstring):
        self.guitarstring = guitarstring

class GuitarString:
    def __init__(self):
        pass

guitarstring_new = GuitarString()
guitar_new = Guitar(guitarstring_new)


# 3. """ Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters."""
#     """ Note: this method should be static. """
class Calc:
    def __init__(self):
        pass

    @staticmethod
    def add_numbs(parameter1, parameter2, parameter3):
        return parameter1 + parameter2 + parameter3


calc = Calc()
print(Calc.add_numbs(1, 2, 3))


# 4.
"""
Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
It should have 2 methods:
carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
which should create Pasta instances with predefined list of ingredients.
Example:
    pasta_1 = Pasta(["tomato", "cucumber"])
    pasta_1.ingredients will equal to ["tomato", "cucumber"]
    pasta_2 = Pasta.bolognaise()
    pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
"""

class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'({self.ingredients})'

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
pasta_2 = Pasta.bolognaise()

print(pasta_1)
print(Pasta.bolognaise())


# 5*.
"""
Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
In case of setting visitors_count - max_visitors_num should be checked,
if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
Example:
    Concert.max_visitor_num = 50
    concert = Concert()
    concert.visitors_count = 1000
    print(concert.visitors_count)  # 50
"""

class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        self._visitors_count = Concert.max_visitor_num if value > Concert.max_visitors_num else value

Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000

print(concert.visitors_count)


# 6."""Create dataclass with 7 fields - key (int), name (str),
# phone_number (str), address (str), email (str), birthday (str), age (int)"""

from dataclasses import dataclass

@dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

address_book = AddressBookDataClass(1, 'Kobzar', '380321212312', 'street_Schevchenko',
                                    't.s.@ukr.net', '26.04.1840', 161)
print(address_book.key)
print(address_book.name)
print(address_book.phone_number)
print(address_book.address)
print(address_book.email)
print(address_book.birthday)
print(address_book.age)

# 7. Create the same class (6) but using NamedTuple

from collections import namedtuple

AddressBookDataClass = namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number',
                                                           'address', 'email', 'birthday', 'age'])

address_book = AddressBookDataClass(1, 'Kobzar', '380321212312', 'street_Schevchenko',
                                    't.s.@ukr.net', '26.04.1840', 161)

print(address_book[0])
print(address_book.name)
print(address_book[2])
print(address_book[3])
print(address_book[4])
print(address_book[5])
print(address_book[6])


# 8.""" Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.

class AddressBook:

    def __init__(self, key, name, phone_number, address, email, birthday, age):
            self.key = key
            self.name = name
            self.phone_number = phone_number
            self.address = address
            self.email = email
            self.birthday = birthday
            self.age = age

    def __str__(self):
        return f'{self.key}, {self.name}, {self.phone_number}, {self.address}, {self.email},' \
                   f'{self.birthday}, {self.age}'

address_book = AddressBook(1, 'Kobzar', '380321212312', 'street_Schevchenko',
                               't.s.@ukr.net', '26.04.1840', 161)
print(address_book)

# 9. """ Change the value of the age property of the person object. """

class Person:
        name = "John"
        age = 36
        country = "USA"

p = Person()
setattr(p, 'age', 30)

print('The genuine age is:', p.age)
# or 2 example output result
print('The genuine age is:', getattr(p, 'age'))


# 10. """Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr """
class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student(7, 'John')
setattr(student, 'email', 'km@gmail.com')
student_email = getattr(student, 'email')
print(student_email)


# 11*.
#     """
#     By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)
#     """
# class Celsius:
#     def __init__(self, temperature=0):
#         self._temperature = temperature
# # create an object
# {obj} = ...
#
# print({obj}.temperature)

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def fahrenheit(self):
        return (self._temperature * 1.8) + 32

temper = Celsius()
print(temper.fahrenheit)

# .



