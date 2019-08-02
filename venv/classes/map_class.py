from __future__ import annotations
from typing import Dict, List

from .country_class import Country
from .person_class import Person


class Map:
    """class creating a map of connected countries to move people to and from"""
    def __init__(self, map_as_dict: Dict[Country, List[Country]]):
        self.countries: Dict[Country, List[Country]] = map_as_dict
        self.infected_people = set()

    def get_countries(self) -> List[Country]:
        """Returns a list of countries"""
        countries = list(self.countries.keys())
        return countries

    def get_country_of_person(self, person: Person, countries: List[Country]) -> Country:
        """Finds the town the person is in"""
        for country in countries:
            if person in country:
                return country

    def file(self):
        with open("info.txt", "w") as myFile:
            for country in self.countries.keys():
                for person in country.citizens:
                    myFile.write(person.name + ", " + person.country + ", " + str(len(person.mutual_friends)) + "\n")

    def infect_first_person(self, person: "Person"):
        pass

    def infect_mutual_friends(self, person):
        for p in person.mutual_friends:
            if not p.is_infected:
                p.infected = True
                self.infected_people.add(p)

