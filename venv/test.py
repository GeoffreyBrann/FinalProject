def show_results():
    '''Displays the number of turns the user took and number of people infected out of total people'''
    turns = int(number_of_turns)
    number_people_infected = int(len(infected_people))
    total_people = int(len(all_people))
    print("You took " + str(turns))
    print("You infected " + str(number_people_infected) + " out of " + str(total_people))
