from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Any
import random
import uuid
import time


class Animal(ABC):
    def __init__(self, power: int, speed: int):
        self.max_power = power
        self.current_power = power
        self.speed = speed
        self.id: uuid = uuid.uuid1()

    @abstractmethod
    def eat(self, forest: Forest):
        pass


class Predator(Animal):

    def __init__(self):
        power = random.randrange(25, 100)
        speed = random.randrange(25, 100)
        Animal.__init__(self, power, speed)

    def eat(self, forest: Forest):
        victim: AnyAnimal = random.choice(list(forest.animals.values()))
        if victim.id == self.id:
            print(f"{self.__class__.__name__} unlucky, without dinner.")
        else:
            print(f"speed = {self.speed}, power = {self.current_power}, {self.__class__.__name__} "
                  f"Run and Chase {victim.__class__.__name__}: power =  {victim.current_power}, speed = {victim.speed}")
            if self.speed > victim.speed:
                print(f"{self.__class__.__name__} caught {victim.__class__.__name__}")

                if self.current_power < victim.current_power:
                    print(f"{victim.__class__.__name__} animal survived.")
                elif self.current_power > victim.current_power:
                    print(f'{self.__class__.__name__} victim hunted.')

        self.current_power = round(self.current_power * 0.5, 1)
        if self.current_power <= 1:
            print(f'{self.__class__.__name__} died.')
            forest.remove_animal(self)


class Herbivorous(Animal):

    def __init__(self):
        power = random.randrange(25, 100)
        speed = random.randrange(25, 100)
        Animal.__init__(self, power, speed)

    def eat(self, forest: Forest):
        self.current_power += self.current_power * 0.7

        if self.current_power > self.max_power:
            self.current_power = self.max_power
        print(f'Herbivorous has: {self.current_power} power.')


AnyAnimal: Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        # self.animals.update({animal.id: animal})
        # The definition names/id animals
        self.animals.update({animal.id: animal})
        print(f'The {animal.__class__.__name__} Added {animal.id}')

    def remove_animal(self, animal: AnyAnimal):
        self.animals.pop(animal.id)

    def anybody_predators(self):
        animal_exist = False
        for key in self.animals.values():
            if isinstance(key, Predator):
                animal_exist = True
        return animal_exist


def animal_generator():
    while True:
        generator_animal = random.choice([Herbivorous(), Predator()])
        yield generator_animal


if __name__ == "__main__":
    nature = animal_generator()

    forest = Forest()
    for i in range(5):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        if not forest.anybody_predators():
            break
        for animal in forest.animals.copy().values():
            animal.eat(forest=forest)
            print('----------------------------------------------------------------------------')
        time.sleep(1)

print("Surviving in forest.")
print("The end.")

