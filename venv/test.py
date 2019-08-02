def show_results():
    '''Displays the number of turns the user took and number of people infected out of total people'''
    turns = str(int(number_of_turns + "taken! "))
    number_people_infected = str(int(len(infected_people)) + "of " + int(len(total_people)) + "total")
    return turns, number_people_infected