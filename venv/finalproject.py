from __future__ import annotations
from typing import Dict, List, Set
from uuid import uuid4


class Map:
    """class creating a map of connected towns to move people to and from"""
    def __init__(self, map_as_dict: Dict[Town, List[Town]]):
        self.towns: Dict[Town, List[Town]] = map_as_dict

    def get_towns(self) -> List[Town]:
        """Returns a list of towns"""
        towns = list(self.towns.keys())
        return towns

    def get_town_of_person(self, person: Person, towns: List[Town]) -> Town:
        """Finds the town the person is in"""
        for town in towns:
            if person in town:
                return town

    def move_person(self, person: Person, destination: Town):
        """Function to move people from town to town"""
        towns = self.get_towns()  ###Gets a list of all the towns
        town_of_person = self.get_town_of_person(person, towns) ###retrieves town person is in
        town_of_person.remove_citizen(person) ###removes person from that town
        destination.add_citizen(person) ##adds person to desired town
        ##Check the intersection of that town's citizens w the mutual friends of that person
        mf = person.get_mutual_friends()
        friends_to_alert = mf.intersection(destination.get_citizens())  ##once intersections are found create print statements to "alert" friends
        friends_to_unalert = mf.intersection(town_of_person.get_citizens())
        for fr in friends_to_alert:
            self.alert_friend(f"Hey {fr.get_name()}, I'm coming to your town.")
        for fr in friends_to_unalert:
            self.alert_friend(f"Sorry {fr.get_name()}, I have to go :(.")

    def alert_friend(self, msg: str):
        print(msg) ###prints statements made in move_person



class Town:
    """class to create towns and hold citizens in each town """
    def __init__(self, name: str, capacity: int, olimit: int, ilimit: int):
        self.uid = uuid4()  ###gives each town a unique id
        self.name = name  ##gives name, capacity, citizens, and limits on the created "roads"
        self.capacity = capacity
        self.citizens = set()
        self.outgoing_roads = set()
        self.incoming_roads = set()
        self.outgoing_limit = olimit
        self.incoming_limit = ilimit

    def __contains__(self, person: Person) -> bool: ###returns true or false if person is in town or not
        return person in self.citizens

    def get_citizens(self) -> Set[Person]:  ###gets the set of people in a town

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


class Person:
    """Class to create people, get their names, add friends, make a friendship mutual, and check and see if it is mutual"""
    def __init__(self, name: str, country):
        self.uid = uuid4()  ###creates unique id, name, and a set for their friends and mutual friends
        self.name = name
        self.friends = set()
        self.mutual_friends = set()
        self.country = country

    def __repr__(self):  ###code to represent the name of each person
        return f"Person<{self.name}>"

    def __str__(self):   ###represents each persons name and uuid
        return f"Person<{self.name}, {self.country}, {len(self.mutual_friends)}>"

    def get_name(self):  ###GETS NAME DUHHHHH
        return self.name

    def add_friend(self, person: "Person", is_mutual: bool = False) -> None:
        '''Add a friend to set of friends.'''
        self.friends.add(person)
        if is_mutual:  ###checks if added friend is mutual or not
            person.friends.add(self)
        if self in person.friends:  ###if it is mutual adds to set mutual friends
            self.mutual_friends.add(person)
            person.mutual_friends.add(self)

    def get_mutual_friends_as_string(self):
        """Returns a string representing mutual friends of current person"""
        content = f"{self.name}'s Mutual Friends List"
        content += f"\n{len(content) * '-'}\n"
        for friend in self.mutual_friends:
            content += f"{friend.name}\n"
        return content
    def get_mutual_friends(self):
        """Returns the set of mutual friends"""
        return self.mutual_friends

    def is_mutual(self, person: "Person")-> bool:
        '''Returns true if two people are mutual friends'''
        return self.uid in person.friends and person.uid in self.friends

def criteria(p1, p2):  ###defines person criteria
    return p1.name[0] == p2.name[0]


if __name__ == "__main__":
    michelle = Person("Michelle")  ###creates a group of people
    jack = Person("Jack")
    kyle = Person("Kyle")
    kim = Person("Kim")
    james = Person("James")
    jennifer = Person("Jennifer")

    people = [michelle, jack]

    for i in range(len(people)):   ###uses criteria to check people are mutual friends based off of name
        for j in range(len(people) - i - 1):
            j = j + i + 1
            if (criteria(people[i], people[j])):
                people[i].add_friend(people[j], is_mutual=True)

    town1 = Town("Ithaca", capacity=10, olimit=2, ilimit=2)  ###creates towns for sake of example
    town1.add_citizen(michelle)
    town1.add_citizen(james)
    town1.add_citizen(kyle)
    town1.add_citizen(jack)
    town2 = Town("New York City", capacity=10, olimit=2, ilimit=2)
    town2.add_citizen(jennifer)
    town2.add_citizen(kim)


    map = Map({
        town1: [town2],  ###creates map of the made towns
        town2: [town1]
    })

    michelle.add_friend(jack, is_mutual=True)  ##calls functions for people to make friends and determine if mutual
    michelle.add_friend(kyle, is_mutual=True)
    michelle.add_friend(jennifer, is_mutual=True)
    michelle.add_friend(kim, is_mutual=False)
    michelle.add_friend(james, is_mutual=False)

    map.move_person(michelle, town2)  ##moves person from town to town
    print(michelle.get_mutual_friends_as_string())