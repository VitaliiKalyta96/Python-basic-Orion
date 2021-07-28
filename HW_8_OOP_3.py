from __future__ import annotations

import random
from abc import ABC, abstractmethod
from typing import Dict, Any


class Animal:
    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        pass


class Predator(Animal):
    def eat(self, forest: Forest):
        print(f"Predator use{self.speed} and {self.max_power}, because he hunt.")

    def __iter__(self):
        self.a = 0
        self.b = 50
        return self

    def __next__(self):
        restore_2 = self.a + self.b
        if restore_2 >= self.max_power:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return restore_2

    def died(self):
       self.max_power = []
       if self.max_power == 0:
           return print(f'{self.max_power} Predator havent more')

predator = [Predator(25, 100) for i in range(random.randint(25, 100))]


class Herbivorous(Animal):

    def eat(self, forest: Forest):
        print(f"Herbivorous use{self.current_power}, because he is eat. "
              f"And Herbivorous use{self.speed} and {self.max_power},because he run")
    def __iter__(self):
        self.a = 0
        self.b = 50
        return self

    def __next__(self):
        restore = self.a + self.b
        if restore >= self.max_power:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return restore

    def died(self):
       self.max_power = []
       if self.max_power == 0:
           return print(f'{self.max_power} Herbivorous havent more')

herbivorous = [Herbivorous(25, 100) for i in range(random.randint(25, 100))]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        self.animals = animal

    def remove_animal(self, animal: AnyAnimal):
        self.animals = animal

AnyAnimal: Any[Herbivorous, Predator]

Herbivorous = ['Badger', 'Haas']

for herbivorous_generator in Herbivorous:
    print(herbivorous_generator)

def generator_first():
    for herbivorous_generator in Herbivorous:
        yield herbivorous_generator

def herbivorous_generator_value(gen):
    try:
        while True:
            print(f'Next herbivorous animal: {next(gen)}')
    except StopIteration:
        print('Last herbivorous animal')

print('___________')

Predator = ['Bear', 'Wolf']

for predator_generator in Predator:
    print(predator_generator)

def generator_second():
    for predator_generator in Predator:
        yield predator_generator

def predator_generator_value(gen):
    try:
        while True:
            print(f'Next predator animal: {next(gen)}')
    except StopIteration:
        print('Last animal')

print('The hunt is over.')






