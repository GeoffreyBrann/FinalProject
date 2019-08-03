from __future__ import annotations
from classes.country_class import Country
from classes.map_class import Map
from classes.person_class import Person


def criteria(p1, p2):  ###defines person criteria
    return p1.name[0] == p2.name[0]


def start_game(our_map: Map):
    print("Welcome to our game: you get to infect people and have those people infect their friends\n" +
          "but its all through social media and yea it will be lots of fun. You get to choose a person to infect first"
          + "and you make all their friends infected and so on")
    our_map.infect_first_person()


def mid_game(our_map: Map):
    '''infects mutual friends of people and counts the number of turns taken'''
    number_of_turns = 0
    old = 0
    now = len(our_map.infected_people)
    our_map.infect_mutual_friends(our_map.infected_people[0])
    input("Press enter to take a turn: ")
    while old != now:
        old = now
        now = len(our_map.infected_people)
        number_of_turns += 1
        for person in our_map.infected_people:
            our_map.infect_mutual_friends(person)
        input("Press enter to take a turn: ")

    '''Display number of turns player took and how many people they infected'''
    turns = int(number_of_turns)  ###number_of_turns is made up
    number_people_infected = int(len(our_map.infected_people))  ###infected_people made up right now
    total_people = 0    ####all_people made up for now
    for z in our_map.countries:
        total_people += len(z.citizens)

    print("You took " + str(turns) + " turn(s). On your last turn you did not infect anyone new.")
    print("You infected " + str(number_people_infected) + " out of " + str(total_people) + " people.")


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
            if criteria(people[i], people[j]):
                people[i].add_friend(people[j], is_mutual=True)

    country1 = Country("America", capacity=10)  ###creates towns for sake of example
    country1.add_citizen(michelle)
    country1.add_citizen(james)
    country1.add_citizen(kyle)
    country1.add_citizen(jack)
    country2 = Country("Canada", capacity=10)
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

    start_game(map)
    mid_game(map)
