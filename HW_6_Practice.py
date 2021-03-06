from abc import abstractmethod


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits, pests, gardener):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener


    def show_the_garden(self):
        print(f'I have such vegetables {self.vegetables}')
        print(f'I have such fruits {self.fruits}')
<<<<<<< HEAD
        print(f'I have such pests {self.pests}')
        print(f'I have a gardener {self.gardener}')
=======
        # print(f'I have such pests {self.pests}')
        print(f'I have a gardener {self.gardener}')

    def attack_pests(self):
        self.pests.eat(self.gardener.plants)
>>>>>>> 1f6541124c2b87d2e2a05a2b1d75f8035a3d8b59


class Vegetables:
    def __init__(self, vegetable_type):
        self.vegetable_type = vegetable_type
        self.pests = []

    states = {"0": "None", "1": "Flowering", "2": "Green", "3": "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")

    @abstractmethod
<<<<<<< HEAD
    def pests_eat_plants(self):
=======
    def eating(self):
>>>>>>> 1f6541124c2b87d2e2a05a2b1d75f8035a3d8b59
        raise NotImplementedError("You missed me")


class Fruits:
    def __init__(self, fruits_type):
        self.fruits_type = fruits_type
        self.pests = []


    states = {0: "None", 1: "Flowering", 2: "Green", 3: "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")

    @abstractmethod
<<<<<<< HEAD
    def pests_eat_plants(self):
=======
    def eating(self):
>>>>>>> 1f6541124c2b87d2e2a05a2b1d75f8035a3d8b59
        raise NotImplementedError("You missed me")


class Tomato(Vegetables):
    def __init__(self, vegetable_type, number_of_tomatoes):
        Vegetables.__init__(self, vegetable_type)
        self.number_of_tomatoes = number_of_tomatoes
        self.states = 0
        self.vegetable_type = vegetable_type

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def print_state(self):
        print(f"{self.vegetable_type}, {self.number_of_tomatoes} , {self.states}")

    def is_ripe(self):
        return self.states == 3

<<<<<<< HEAD
    def pests_eat_plants(self):
        if self.states >= 2:
            return print(f'Pests eat this {self.number_of_tomatoes} tomatos. ')
        else:
            return print(f" Pests don't eat this tomatos.")
=======
    def eating(self):
        return self.states in [1, 2]
>>>>>>> 1f6541124c2b87d2e2a05a2b1d75f8035a3d8b59

class Apple(Fruits):
    def __init__(self, fruits_type, number_of_apples):
        Fruits.__init__(self, fruits_type)
        self.number_of_apples = number_of_apples
        self.states = 0
        self.fruits_type = fruits_type

    def print_state(self):
        print(f"{self.fruits_type}, {self.number_of_apples} , {self.states}")

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def is_ripe(self):
        return self.states == 3

<<<<<<< HEAD
    def pests_eat_plants(self):
        if self.states <= 2:
            return print(f'Pests eat this {self.number_of_apples} apples.')
        else:
            return print(f" Pests don't eat this apples.")
=======
    def eating(self):
        return self.states in [1, 2]
>>>>>>> 1f6541124c2b87d2e2a05a2b1d75f8035a3d8b59

class TomatoBush:
    def __init__(self, number_of_tomatoes):
        self.tomatoes = [Tomato('Cherry', index) for index in range(0, number_of_tomatoes - 1)]

    def growth_all(self):
        for tomato in self.tomatoes:
            tomato.growth()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

    def attack_pests(self):
        for tomato in self.tomatoes.copy():
            if tomato.eating():
                self.tomatoes.remove(tomato)
                print('Om-nom-nom')
            else:
                print("What happened with this food? She's not like that")

    def to_check_states(self):
        for tomato in self.tomatoes:
            tomato.print_state()

class AppleTree:
    def __init__(self, number_of_apples):
        self.apples = [Apple('White', index) for index in range(0, number_of_apples - 1)]

    def growth_all(self):
        for apple in self.apples:
            apple.growth()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []

    def attack_pests(self):
        for apple in self.apples.copy():
            if apple.eating():
                self.apples.remove(apple)
                print('Om-nom-nom')
            else:
                print("What happened with this food? She's not like that")

    def to_check_states(self):
        for apple in self.apples:
            apple.print_state()

class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    def work(self):
        for plant in self.plants:
            plant.growth_all()

    def harvest(self):
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
                print("Finally collect all harvest")
            else:
                print('Too early to harvest')

    def to_poison_pests(self):
        Garden().pests.quantity = 0
        print("Go away pests!!! This is my garden and only my garden!")

    def to_check_states(self):
        for plant in self.plants:
            plant.to_check_states()

<<<<<<< HEAD
=======

>>>>>>> 1f6541124c2b87d2e2a05a2b1d75f8035a3d8b59
class Pests:
    def __init__(self, pests_type, quantity):
        self.pests_type = pests_type
        self.quantity = quantity

    def quantity_pests(self):
        print(f'A pests is quantity {self.quantity}.')

<<<<<<< HEAD
tomato_bush = TomatoBush(5)
apple_tree = AppleTree(4)
Tom = Gardener('Tom', [tomato_bush, apple_tree])
pests = Pests('worm', 10)
garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, pests=pests, gardener=Tom)
garden.show_the_garden()
pests.quantity_pests()

# print(tomato_bush.tomatoes)
# print(apple_tree.apples)

Tom.work()
Tom.work()
Tom.harvest()
Tom.work()
Tom.harvest()



from abc import abstractmethod


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits, pests, gardener):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener


    def show_the_garden(self):
        print(f'I have such vegetables {self.vegetables}')
        print(f'I have such fruits {self.fruits}')
        print(f'I have such pests {self.pests}')
        print(f'I have a gardener {self.gardener}')


class Vegetables:
    def __init__(self, vegetable_type):
        self.vegetable_type = vegetable_type
        self.pests = []

    states = {"0": "None", "1": "Flowering", "2": "Green", "3": "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")

    @abstractmethod
    def pests_eat_plants(self):
        raise NotImplementedError("You missed me")


class Fruits:
    def __init__(self, fruits_type):
        self.fruits_type = fruits_type
        self.pests = []

    states = {0: "None", 1: "Flowering", 2: "Green", 3: "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")

    @abstractmethod
    def pests_eat_plants(self):
        raise NotImplementedError("You missed me")


class Tomato(Vegetables):
    def __init__(self, vegetable_type, number_of_tomatoes):
        Vegetables.__init__(self, vegetable_type)
        self.number_of_tomatoes = number_of_tomatoes
        self.states = 0
        self.vegetable_type = vegetable_type

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def print_state(self):
        print(f"{self.vegetable_type}, {self.number_of_tomatoes} , {self.states}")

    def is_ripe(self):
        return self.states == 3

    def pests_eat_plants(self):
        if self.states >= 2:
            return print(f'Pests eat this {self.number_of_tomatoes} tomatos. ')
        else:
            return print(f" Pests don't eat this tomatos.")

class Apple(Fruits):
    def __init__(self, fruits_type, number_of_apples):
        Fruits.__init__(self, fruits_type)
        self.number_of_apples = number_of_apples
        self.states = 0
        self.fruits_type = fruits_type

    def print_state(self):
        print(f"{self.fruits_type}, {self.number_of_apples} , {self.states}")

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def is_ripe(self):
        return self.states == 3

    def pests_eat_plants(self):
        if self.states <= 2:
            return print(f'Pests eat this {self.number_of_apples} apples.')
        else:
            return print(f" Pests don't eat this apples.")

class TomatoBush:
    def __init__(self, number_of_tomatoes):
        self.tomatoes = [Tomato('Cherry', index) for index in range(0, number_of_tomatoes - 1)]

    def growth_all(self):
        for tomato in self.tomatoes:
            tomato.growth()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class AppleTree:
    def __init__(self, number_of_apples):
        self.apples = [Apple('White', index) for index in range(0, number_of_apples - 1)]

    def growth_all(self):
        for apple in self.apples:
            apple.growth()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []


class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    def work(self):
        for plant in self.plants:
            plant.growth_all()

    def harvest(self):
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
                print("Finally collect all harvest")
            else:
                print('Too early to harvest')


class Pests:
    def __init__(self, pests_type, quantity):
        self.pests_type = pests_type
        self.quantity = quantity

    def quantity_pests(self):
        print(f'A pests is quantity {self.quantity}.')

=======
    def eat(self, plants):
        if self.quantity > 9:
            for plant in plants:
                plant.attack_pests()

>>>>>>> 1f6541124c2b87d2e2a05a2b1d75f8035a3d8b59
tomato_bush = TomatoBush(5)
apple_tree = AppleTree(4)
Tom = Gardener('Tom', [tomato_bush, apple_tree])
pests = Pests('worm', 10)
<<<<<<< HEAD
garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, pests=pests, gardener=Tom)
garden.show_the_garden()
pests.quantity_pests()
=======

garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, pests=pests, gardener=Tom)
>>>>>>> 1f6541124c2b87d2e2a05a2b1d75f8035a3d8b59

# print(tomato_bush.tomatoes)
# print(apple_tree.apples)

<<<<<<< HEAD
Tom.work()
Tom.work()
Tom.harvest()
=======
Tom.work()
Tom.to_check_states()
pests.quantity_pests()
garden.attack_pests()
Tom.to_poison_pests()
Tom.harvest()
garden.show_the_garden()
>>>>>>> 1f6541124c2b87d2e2a05a2b1d75f8035a3d8b59
Tom.work()
Tom.harvest()



<<<<<<< HEAD
=======

>>>>>>> 1f6541124c2b87d2e2a05a2b1d75f8035a3d8b59
