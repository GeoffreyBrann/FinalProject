def show_results():
    '''Displays the number of turns the user took and number of people infected out of total people'''
    turns = int(number_of_turns)  ###number_of_turns is made up
    number_people_infected = int(len(infected_people))  ###infected_people made up right now
    total_people = int(len(all_people))   ####all_people made up for now
    print("You took " + str(turns))
    print("You infected " + str(number_people_infected) + " out of " + str(total_people))
