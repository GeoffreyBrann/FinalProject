from __future__ import annotations
from uuid import uuid4


class Person:
    """Class to create people, get their names, add friends, make a friendship mutual, and check and see if it is mutual"""
    def __init__(self, name: str, country, internet_time: bool, PE: bool, eat: bool, sleep: bool, cured: bool):
        self.uid = uuid4()  ###creates unique id, name, and a set for their friends and mutual friends
        self.name = name
        self.friends = set()
        self.mutual_friends = set()
        self.country = country   ###country person is in
        self.infected = False   ###boolean if the person is infected or not
        self.internet_time = internet_time
        self.PE = PE
        self.eat = eat
        self.sleep = sleep
        self.cured = cured

    def __repr__(self):  ###code to represent the name of each person
        return f"Person<{self.name}>"

    def __str__(self):   ###represents each persons name and uuid
        return f"{self.name}, {self.country}, {len(self.mutual_friends)} friend(s)"

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

    def is_infected(self)-> bool:
        '''Returns true if a person is infected'''
        return self.infected

    def can_be_infected(self, type_of_infection):
        if type_of_infection == "active":
            counter = 2
        elif type_of_infection == "passive":
            counter = 0

        if self.cured:
            return False
        else:
            if self.internet_time:
                counter += 1
            if self.PE:
                counter += 1
            if self.eat:
                counter += 1
            if self.sleep:
                counter += 1

        if counter >= 3:
            return True





