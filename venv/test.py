def show_results():
    '''Displays the number of turns the user took and number of people infected out of total people'''
    turns = int(number_of_turns)
    number_people_infected = int(len(infected_people))
    total_people = int(len(all_people))
    print("You took " + turns)
    print("You infected " + number_people_infected + " out of " + total_people)
