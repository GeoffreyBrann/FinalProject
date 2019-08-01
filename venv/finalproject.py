from __future__ import annotations

from classes.country_class import Country
from classes.map_class import Map
from classes.person_class import Person


def criteria(p1, p2):  ###defines person criteria
    return p1.name[0] == p2.name[0]


if __name__ == "__main__":
    michelle = Person("Michelle", "a")  ###creates a group of people
    jack = Person("Jack", "a")
    kyle = Person("Kyle", "a")
    kim = Person("Kim", "a")
    james = Person("James", "a")
    jennifer = Person("Jennifer", "a")

    people = [michelle, jack]

    for i in range(len(people)):   ###uses criteria to check people are mutual friends based off of name
        for j in range(len(people) - i - 1):
            j = j + i + 1
            if (criteria(people[i], people[j])):
                people[i].add_friend(people[j], is_mutual=True)

    country1 = Country("America", capacity=10, olimit=2, ilimit=2)  ###creates towns for sake of example
    country1.add_citizen(michelle)
    country1.add_citizen(james)
    country1.add_citizen(kyle)
    country1.add_citizen(jack)
    country2 = Country("Canada", capacity=10, olimit=2, ilimit=2)
    country2.add_citizen(jennifer)
    country2.add_citizen(kim)


    map = Map({
        country1: [country2],  ###creates map of the made countries
        country2: [country1]
    })

    michelle.add_friend(jack, is_mutual=True)  ##calls functions for people to make friends and determine if mutual
    michelle.add_friend(kyle, is_mutual=True)
    michelle.add_friend(jennifer, is_mutual=True)
    michelle.add_friend(kim, is_mutual=False)
    michelle.add_friend(james, is_mutual=False)

    print(michelle.get_mutual_friends_as_string())