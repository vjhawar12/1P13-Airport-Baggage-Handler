"""
1P13 Design Studio
Dr. Cam Churchill
Created on Fri Nov  8 15:14:57 2024
@authors: Vedant, Liam, Majuraa, Hanna
"""

from graphical import graphical_Fri53 # modulated code has graphical_teamID in another file in same directory

def overweight(passenger_data: list, fleet_data: list) -> tuple: # Liam
    """ Takes in passenger and fleet data and returns two lists in in tuple format """
    planes = [] # list of [[Plane 1 model, Number of passengers with overweight baggage],...etc.]
    people = [] # list of [[Passenger 1 first name, First letter of last name, Gate, weight difference], ...etc.]

    f = sorted(fleet_data, key=lambda x: x[4]) # sorting the planes by gate 
    
    i = 0 # placeholder increment variable
    for plane in f: 
        planes.append([plane[0], 0]) # initially adding 0 so it can be incremented layer
        for person in p: 
            if person[-1] == "Layover": # indices to compare vary based on Layover or not
                if plane[-1] < person[-2]: # if baggage exceeds weight limit
                    planes[i][1] += 1 
            else:
                if plane[-1] < person[-1]: # if baggage exceeds weight limit
                    planes[i][1] += 1
        i += 1

    i = 0 # resetting incrementer
    for person in passenger_data:
        people.append([person[0], person[1], person[2], 0]) # adding stuff to list
        for person in p:
            if person[-1] == "Layover": # indices vary based on layover or not
                if not abs(float(plane[-1])) - abs(float(person[-2])) < 0.1: # float subtraction is funky bc of lossy data so compare to check if decimals are within a range
                    people[i][1] = abs(round(float(plane[-1]) - float(person[-2]), 2)) # getting the weight difference
            else: 
                if not abs(float(plane[-1])) - abs(float(person[-1])) < 0.1: 
                    people[i][1] = abs(round(float(plane[-1]) - float(person[-1]), 2)) # getting the wegiht difference
        i += 1

    print("Planes: \n\n")
    print(planes)
    print("\n\n People: \n\n")
    print(people)

    return planes, people

def layover(passenger: list, fleet: list) -> tuple: # Hanna
    """ Takes in passenger and fleet data and returns two lists in in tuple format """
    planes = [] # list of [[model, # layovers], [], ...] 
    people = [] # list of [[passenger name, passenger last initial, gate], [], ...]
    
    f = sorted(fleet, key=lambda x: x[4]) # sorting the planes by gate

    i = 0 # placeholder increment variable
    for plane in f:
        planes.append([plane[0], 0])  # initially adding 0 so it can be incremented
        for person in passenger: 
            if person[-1] == "Layover": # does last index of person indicate layover
                planes[i][1] += 1 # incrementing because person has layover
        i += 1

    for person in passenger:
        if person[-1] == "Layover": # does last index of person indicate layover
            people.append([person[0], person[1], person[2]]) # adding stuff to list

    return planes, people # returning both lists in tuple format
        

def oversold(passenger: list, fleet: list, daily: list) -> tuple: # Vedant
    """ Takes in passenger, fleet, and daily data and returns two lists in in tuple format """
    business = [] # oversold business seats
    economy = [] # oversold economy seats
    
    f = sorted(fleet, key=lambda x: x[4]) # sorting fleet data by gate using lambda expression
    
    i = 0
    for plane in f:
        if daily[i][1] - int(plane[1]) > 0: # if oversold i.e # business passengers > # business seats
            business.append([plane[0], daily[i][1] - int(plane[1])]) # adding [model, business passengers - business seats]
        else:
            business.append([plane[0], 0]) # not oversold so adding [model, 0]
            
        if daily[i][2] - int(plane[2]) > 0:  # if oversold i.e # economy passengers > # economy seats
            economy.append([plane[0], daily[i][2] - int(plane[2])]) # adding [model, economy passengers - economy seats]
        else:
            economy.append([plane[0], 0])  # not oversold so adding [model, 0]
        i += 1
    
    print("Business: \n\n")
    print(business)
    print("\n\nEconomy: \n\n")
    print(economy)
    return business, economy # returning both business and economy in tuple format

def passenger_data() -> list: # Group
    """ Takes in nothing and reads fleet_data.txt and creates a list of 
    [[name, last name initial, gate, seating class, destination, arrival, weight, layover]] """

    f = open("passenger_data_v2.txt", 'r') # opening in read only mode bc file will not be modified
    lis = []
    lines = f.readlines()
    for line in lines:
        line = line.strip(" ,\n").split(",")
        lis.append(line)
    f.close()
    return lis

def fleet_data() -> list: # Group
    """ Takes in nothing and reads fleet_data.txt and creates a list of 
    [[model, # business seats, # economy seats, total # seats, Gate, Destination, arrival, weight]] """

    f = open("fleet_data.txt", 'r') # opening in read only mode bc file will not be modified
    lis = []
    lines = f.readlines()
    for line in lines:
        line = line.strip(" ,\n").split(",") # removing bad characters
        lis.append(line) 
    return lis

def get_business(gate: str, passenger: list) -> int: # Helper function by Vedant
    """ get_business function takes in a gate (str) and a passenger (list) and returns int: total number of
        business passengers for that gate """
    
    count = 0 # to be returned at end
    for person in passenger:
        if person[2] == gate:
            if person[4] == 'B': # if index 4 (seating class) is business
                count += 1
    return count

def get_economy(gate: str, passenger: list) -> int: # Helper function by Vedant
    """ Takes in a gate (str) and a passenger (list) and returns int: total number of
        economy passengers for that gate """
    
    count = 0 # to be returned at end
    for person in passenger:
        if person[2] == gate: # index 2 is the gate 
            if person[4] == 'E': # if index 4 (seating class) is economy
                count += 1 
    return count

def daily_data(passenger: list) -> list: # Majuraa
    """ Takes in a passenger (list) and returns a list: [gate, # business, # economy[] """

    data = sorted(passenger, key=lambda x: x[2]) # lambda expression to sort passenger list by gate (index 2)
    new = [] # to be returned
    for i in data: 
        gate = i[2] # index 2 is the gate
        if [gate] not in new: # adding gate only once in the list 
            new.append([gate])
    for gate in new: # for each gate, adding the # of business and economy passengers
        gate.append(get_business(gate[0], passenger)) # business passengers 
        gate.append(get_economy(gate[0], passenger)) # economy passengers
    return new 

p = passenger_data()
f = fleet_data()
d = daily_data(p)
ow = overweight(p, f)
os = oversold(p, f, d)
la = layover(p, f)

graphical_Fri53(ow, os, la)
