from __future__ import annotations
from typing import Dict, List

from .country_class import Country
from .person_class import Person


class Map:
    """class creating a map of connected countries to move people to and from"""
    def __init__(self, map_as_dict: Dict[Country, List[Country]]):
        self.countries: Dict[Country, List[Country]] = map_as_dict

    def get_countries(self) -> List[Country]:
        """Returns a list of countries"""
        countries = list(self.countries.keys())
        return countries

    def get_country_of_person(self, person: Person, countries: List[Country]) -> Country:
        """Finds the town the person is in"""
        for country in countries:
            if person in country:
                return country