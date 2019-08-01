from __future__ import annotations
from typing import Set
from uuid import uuid4

from .person_class import Person

class Country:
    """class to create towns and hold citizens in each town """
    def __init__(self, name: str, capacity: int):
        self.uid = uuid4()  ###gives each country a unique id
        self.name = name  ##gives name, capacity, citizens, and limits on the created "roads"
        self.capacity = capacity
        self.citizens = set()

    def get_citizens(self) -> Set[Person]:  ###gets the set of people in a country
        return self.citizens

    def add_citizen(self, person: Person):
        """Adds person to the town"""
        self.citizens.add(person)

    def remove_citizen(self, person: Person):
        """Removes person from town"""
        if person in self.citizens:
            self.citizens.remove(person)
            return
        raise KeyError

