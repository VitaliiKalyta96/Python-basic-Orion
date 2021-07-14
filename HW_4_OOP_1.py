# 1. Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


"""Example for execute code if taken symbol #"""


# porshe = Vehicle(300, 50)
# print(porshe.max_speed, porshe.mileage)

# 2. Create a child class Bus that will inherit all of the variables and methods of
# the Vehicle class and will have seating_capacity own method

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def seating_capacity(self):
        print(f"The capacity of a is {self.seating_capacity()} passengers")


School_bus = Bus(150, 100000)
"""Example for execute code if taken symbol #"""
# print("Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
# print(School_bus.seating_capacity(25))

# 3. Determine which class a given Bus object belongs to (Check type of an object)

print(type(School_bus))

# 4. Determine if School_bus is also an instance of the Vehicle class

print(isinstance(School_bus, Vehicle))


# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus
# and will have its own - bus_school_color

class SchoolBus(School, Bus):
    def __init__(self, max_speed, mileage, get_school_id, number_of_students):
        super(School, self).__init__(get_school_id, number_of_students)
        super(Bus, self).__init__(max_speed, mileage)

    def bus_school_color(self):
        self.bus_school_color()


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method.
# Create two instances, one of Bear and one of Wolf,make a tuple of it and
# by using for call their action using the same method.

class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound_method(self):
        print(f"I make the sound {self.sound}, because I'm a bear.")


bear = Bear('Boo')


class Wolf:
    def __init__(self, sound):
        self.sound = sound

    def make_sound_method(self):
        print(f"I make the sound {self.sound}, because I'm a wolf.")


wolf = Wolf('Woof')

for animal in (bear, wolf):
    animal.make_sound_method()


# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when
# population > 1500,otherwise return message: "Your city is too small".

class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)
        else:
            return print("Your city is too small")

    def __init__(self, name, population):
        self.name = name
        self.population = population


nw_city = City('Miami', 1200)


# 9. Override a printable string representation of the City class and return:
# The population of the city {name} is {population}

class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)
        else:
            return print("Your city is too small")

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f"The population of the city {self.name} is {self.population}."


nw_city_2 = City('Lviv', 900000)
print(nw_city_2)


# 10*. Override magic method __add__() to perform the additional action
# as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.

class Adding:
    def __init__(self, sum):
        self.sum = sum

    def __add__(self, anything):
        if self.sum > 10:
            return self.sum * anything.sum
        else:
            return self.sum + anything.sum


adding = Adding(20)
adding_2 = Adding(10)
print(adding + adding_2)


# 11. The __call__ method enables Python programmers to write classes where
# the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.

class New_class:
    def __init__(self):
        pass

    def __call__(self, a, b):
        print(a * b)


new_class = New_class()
# __call__ method will be called
new_class(10, 20)


# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        return len(self.cart) > 0


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))

# .