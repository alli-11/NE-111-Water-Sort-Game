   # Importing necessary libraries: MODIFIED
import copy 
import sys 
import os 
import random 
import time

while True:
    print()
    print("Welcome to Sorting Game created by GlobalCreativeCommunityFounder and edited by: Alli Miles, Fatima Varela Varela, Victoria Cella Xia and Esha Saleem")
    user_input = input("Please press 1 to play WaterSortPuzzle, press 2 to play Chemist's Jumble, press 3 to play Farmer's Hustle and press 4 to exit: ")

    if user_input == "1":
        # Creating necessary functions to be used throughout the game.

        def is_int(possible) :
            try:
                int(possible)
            except ValueError:
                return False
            else :
                return True

        def clear(): # test for a specific system version -> being able to run in different operating systems
            # type: () -> None
            if sys.platform.startswith('win'):
                os.system('cls') # For Windows System
            else:
                os.system('clear')  # For Linux System


        def all_bottles_sorted(bottles: list) -> bool: #bool shows what the function will return but does not force function to return bool (solely for readability)
            # All: variable: list - indicates that the input will be in list form
            if len(bottles) == 0: 
                return True
            else:
                for bottle in bottles:
                    if not bottle.sorted(): 
                        return False

                return True 

        # Creating necessary classes


        class Bottle: # 'Bottle' is the name of the class
            """
            This class contains attributes of a water bottle.
            """

            BOTTLE_CAPACITY: int = 5 #constant

            def __init__(self, water_levels=None): # __init__ (method) - initializes object's attributes
                # None is default if water_levels not defined by user
                # type: (list) -> None
                if water_levels is None: #avoid error, list will always be given
                    water_levels =  [] #in case no list is given - later filled with COLORS
                self.__water_levels: list = water_levels #bind object (self) to water_levels so that every instance (object created) reassigns water_levels

            def __str__(self): # __str__ (method) - actuator of the class (it actually prints/performs what need)
                # type: () -> str
                res: str = ""  # initial value (empty string). Initiating string that will 'draw' the bottle
                    #THIS WILL BUILD ONE SINGLE TUBE
                for i in range(self.BOTTLE_CAPACITY - 1, -1, -1):
                    if i >= len(self.__water_levels): 
                        #if the bottle capacity is greater than the water level --> for empty lists(water_levels), loop will run 5 times (create a tube with 5 lines of walls)
                        res += "|        |\n" 
                    else: #in case self's list is not empty
                        curr_water_level: Water = self.__water_levels[i] 
                        if len(str(curr_water_level)) == 3: 
                            res += "|   " + str(curr_water_level) + "  |\n"  #for 'RED'
                        elif len(str(curr_water_level)) == 4: 
                            res += "|  " + str(curr_water_level) + "  |\n" #for 'BLUE'
                        elif len(str(curr_water_level)) == 5:
                            res += "|  " + str(curr_water_level) + " |\n" #for 'GREEN'
                        else: 
                            res += "| " + str(curr_water_level) + " |\n" # for "ORANGE", "PURPLE", "YELLOW

                return res #output will be a visual representation of the water tube

            def add_water_level(self, water): #checks whether it is possible to add an additional color (if bottle is not full)
                # type: (Water) -> bool
                if len(self.__water_levels) < self.BOTTLE_CAPACITY: # at lower levels, BOTTLE CAPACITY = 5 --> "when the water level (i.e. colors) is less than full bottle capacity)
                    self.__water_levels.append(water)
                    return True
                return False

            def pour_water(self, other_bottle):
                # type: (Bottle) -> bool
                self_last: Water = self.get_last_water_level() #retrieve last (top) item in current bottle
                other_last: Water = other_bottle.get_last_water_level() 
                if self_last == None:
                    return False
                if len(other_bottle.get_water_levels()) >= self.BOTTLE_CAPACITY: 
                    return False
                if other_last is None or self_last.colour == other_last.colour or len(other_bottle.__water_levels) == 0:
                    self.__water_levels.remove(self_last)
                    other_bottle.add_water_level(self_last) 
                    return True 
                return False

            def get_last_water_level(self):
                # type: () -> Water or None
                if len(self.__water_levels) > 0: 
                    return self.__water_levels[len(self.__water_levels) - 1] 
                else:
                    return None

            def sorted(self):
                # type: () -> bool
                if len(self.__water_levels) == 0:
                    return True
                else:
                    curr_colour: str = self.__water_levels[0].colour 
                    for water in self.__water_levels: 
                        if water.colour != curr_colour:  
                            return False

                    return True

            def get_water_levels(self): #returns color list (in tube) when called --> makes self.__water_levels a method
                # type: () -> list
                return self.__water_levels 

            def clone(self):
                # type: () -> Bottle
                return copy.deepcopy(self) #returns clone of object (completely independent from original)


        class Water: #second important object of the game
            """
            This class contains attributes of water
            """
            POSSIBLE_COLOURS: list = ["BLUE", "RED", "ORANGE", "GREEN", "PURPLE", "YELLOW"] 

            def __init__(self, colour): #initializing, attributing color to self
                # type: (str) -> None
                self.colour: str = colour if colour in self.POSSIBLE_COLOURS else self.POSSIBLE_COLOURS[0] #assign 1 color to object. Deafult is blue

            def __str__(self): #generates user-readable/usable output (from __init__)
                # type: () -> str
                return str(self.colour)

            def clone(self):
                # type: () -> Water
                return copy.deepcopy(self) 

        # Creating main function used to run the game.


        def main():
            """
            This function is used to run the game.
            :return: None
            """
            print()
            print("Welcome to 'Water Sort Puzzle' by 'GlobalCreativeCommunityFounder'.") 
            print("In this game, you are required to make sure that each water bottle only contains one colour of water.") 
            print()
            print("Enter 'Y' for yes.") 
            print("Enter anything else for no and exit the game.") 
            level: int = 1 
            continue_playing: str = input("Do you want to play 'Water Sort Puzzle'? ") 
            while continue_playing == "Y" or continue_playing == "y": 
                bottles: list = [] 
                number_of_bottles: int = 5 + (level // 5) 
                                                       
                number_of_empty_bottles: int = number_of_bottles // 5 
                                                                    
                filled_bottles = number_of_bottles - number_of_empty_bottles
                possible_colours: list = Water.POSSIBLE_COLOURS if number_of_bottles >= 10 else Water.POSSIBLE_COLOURS[0:4] #creates list of possible colours:  all of original possible colours if there are 10+ bottles
                                                                                                                       
                for i in range(number_of_empty_bottles): #loop will run for every empty bottle. 1 empty bottle -> range = [0]
                    bottles.append(Bottle([])) #creating empty bottles/empty lists (level 1 will have 1 empty bottle)
                
                i = 0
                while i < filled_bottles: #loop will run for every filled bottle
                    water_levels: list = [] 
                    for j in range(4): 
                        water_levels.append(Water(possible_colours[random.randint(0, len(possible_colours) - 1)])) #generates a random integer to be used as the index for the constant list of possible colors defined in Water then appends that entry (color) to the list water_levels

                    bottles.append(Bottle(water_levels)) #append the list created above to the object bottles + applying it to the class Bottle
                    i += 1

                while not all_bottles_sorted(bottles): #while the user hasn't sorted like colors into one tube
                    clear()

                    print("You are now at level " + str(level))
                    print("Current representation of each bottle is as below.\n") 
                    for bottle in bottles: #for every item (bottle, which contain colors) in list of bottles created above
                        print(str(bottle) + "\n") #actually displays bottles built in Bottle

                    bottle_from_index: int = input("Press \"r\" at any time to restart. \nPlease enter index of water bottle you want to pour coloured water from " #asks user to pick a bottle (take color out of it)
                                                    "(1 - " + str(len(bottles)) + "): ") #REMINDER: ADD INTEGER CHECK
                    if bottle_from_index == "r":
                            break
                    bottle_to_index: int = input("Please enter index of water bottle you want to pour coloured water to " #asks user for recipient bottle (put color into it)
                                                    "(1 - " + str(len(bottles)) + "): ")
                    if bottle_to_index == "r":
                            break
                    while (is_int(bottle_from_index) == False or is_int(bottle_to_index) == False): #checks for numerically invalid inputs (not TypeError inputs)
                        print("Invalid input! A different input is expected!") 
                        bottle_from_index = input("Press \"r\" at any time to restart. \nPlease enter index of water bottle you want to pour coloured water from "
                                                    "(1 - " + str(len(bottles)) + "): ") 
                        if bottle_from_index == "r":
                            break
                        bottle_to_index = input("Please enter index of water bottle you want to pour coloured water to "
                                                    "(1 - " + str(len(bottles)) + "): ")
                        if bottle_to_index == "r":
                            break
                    bottle_from_index = int(bottle_from_index)
                    bottle_to_index = int(bottle_to_index)
                    while bottle_from_index < 1 or bottle_from_index > len(bottles) or bottle_to_index < 1 or bottle_to_index > len(bottles) or bottle_from_index == bottle_to_index:
                        print("Invalid input! A different input is expected!") #checks for numerically invalid inputs (not TypeError inputs)
                        bottle_from_index = input("Press \"r\" at any time to restart. \nPlease enter index of water bottle you want to pour coloured water from "
                                                    "(1 - " + str(len(bottles)) + "): ") 
                        if bottle_from_index == "r":
                            break
                        bottle_to_index = input("Please enter index of water bottle you want to pour coloured water to "
                                                    "(1 - " + str(len(bottles)) + "): ")
                        if bottle_to_index == "r":
                            break
                        while (is_int(bottle_from_index) == False or is_int(bottle_to_index) == False):
                            print("Invalid input! A different input is expected!") #checks for numerically invalid inputs (not TypeError inputs)
                            bottle_from_index = input("Press \"r\" at any time to restart. \nPlease enter index of water bottle you want to pour coloured water from "
                                                        "(1 - " + str(len(bottles)) + "): ")
                            if bottle_from_index == "r":
                                break
                            bottle_to_index = input("Please enter index of water bottle you want to pour coloured water to "
                                                        "(1 - " + str(len(bottles)) + "): ")
                            if bottle_to_index == "r":
                                break
                        bottle_from_index = int(bottle_from_index)
                        bottle_to_index = int(bottle_to_index)

                        
                    bottle_from: Bottle = bottles[bottle_from_index - 1] # new variable refering to class Bottle --> picks bottle (from bottles) chosen by user with corresponding index 
                    bottle_to: Bottle = bottles[bottle_to_index - 1] #picks bottle (from bottles) to receive color --> from index chosen by user
                    bottle_from.pour_water(bottle_to) #applies method pour_water (from Bottle) with bottle_from as self and bottle_to as other_bottle
            
                if all_bottles_sorted(bottles):
                    for bottle in bottles: # for every item (bottle, which contain colors) in list of bottles created above
                        print(str(bottle) + "\n") #actually displays bottles built in Bottle
                    print ("Congratulations! The coloured water is sorted:(")
                    level += 1
                    print("Enter 'Y' for yes.") 
                    print("Enter anything else to return to game selection.")
                    continue_playing = input("Do you want to continue playing 'Water Sort Puzzle'? ") #once bottles are sorted, asks if while loop should continue


        if __name__ == '__main__': 
            main()

    elif user_input == "2":
        # Creating necessary functions to be used throughout the game.

        def is_int(possible) :
            try:
                int(possible)
            except ValueError:
                return False
            else :
                return True

        def clear(): #test for a specific system version -> being able to run in different operating systems
            if sys.platform.startswith('win'):
                os.system('cls')  
            else:
                os.system('clear') 


        def all_bottles_sorted(bottles: list) -> bool: #bool shows what the function will return but does not force function to return bool (solely for readability)
            #variable: list - indicates that the input will be in list form
            if len(bottles) == 0: #if there are no bottles, all bottles are sorted
                return True
            else:
                for bottle in bottles:
                    if not bottle.sorted(): 
                        return False

                return True


        # Creating necessary classes


        class Bottle: #'Bottle' is the name of the class
            """
            This class contains attributes of a water bottle.
            """

            BOTTLE_CAPACITY: int = 5 

            def __init__(self, water_levels=None): # __init__ (method) - initializes object's attributes
                #None is default if water_levels not defined by user
                # type: (list) -> None
                if water_levels is None: #avoid error, list will always be given
                    water_levels =  [] #in case no list is given - later filled with COLORS
                self.__water_levels: list = water_levels #bind object (self) to water_levels so that every instance (object created) reassigns water_levels

            def __str__(self): # __str__ (method) - actuator of the class (it actually prints/performs what need)
                # type: () -> str
                res: str = ""  #initial value (empty string). Initiating string that will 'draw' the bottle
                    #THIS WILL BUILD ONE SINGLE TUBE
                for i in range(self.BOTTLE_CAPACITY - 1, -1, -1): # binding object to BOTTLE_CAPACITY 
                    if i >= len(self.__water_levels): #for every level of the actual bottle (4, 3, 2, 1, 0), if number is greater or equal to the length of the list, the string is reset to 'empty walls of the tube' 
                        #if the bottle capacity is greater than the water level --> for empty lists(water_levels), loop will run 5 times (create a tube with 5 lines of walls)
                        res += "|                     |\n" 
                    else: #Vin case self's list is not empty
                        curr_water_level: Water = self.__water_levels[i] #indexes 0, 1, 2, 3, 4 of list of water levels --> meant to align empty and filled tube wall sections
                        if len(str(curr_water_level)) == 3: # for 'H2O'
                            res += "|         " + str(curr_water_level) + "         |\n"
                        elif len(str(curr_water_level)) == 4: # for 'NaCl'and 'SiO2'
                            res += "|        " + str(curr_water_level) + "         |\n"
                        elif len(str(curr_water_level)) == 5: # for 'NaOCl' and 'Water' and 'MgSO4'
                            res += "|        " + str(curr_water_level) + "        |\n"
                        elif len(str(curr_water_level)) == 6: # for 'NaHCO3' and 'Bleach'and 'Quartz'
                            res += "|       " + str(curr_water_level) + "        |\n"
                        elif len(str(curr_water_level)) == 10: # for 'Table salt' and 'Epsom salt'
                            res += "|     " + str(curr_water_level) + "      |\n"
                        elif len(str(curr_water_level)) == 11: # for 'Baking soda'
                            res += "|     " + str(curr_water_level) + "     |\n"
                        elif len(str(curr_water_level)) == 15: # for 'Sodium chloride' and 'Silicon dioxide'
                            res += "|   " + str(curr_water_level) + "   |\n"
                        elif len(str(curr_water_level)) == 17: # for 'Magnesium sulfate'
                            res += "|  " + str(curr_water_level) + "  |\n"
                        elif len(str(curr_water_level)) == 18: # for 'Sodium bicarbonate'
                            res += "| " + str(curr_water_level) + "  |\n"
                        else: # 'Dihydrogen monoxide' and 'Sodium hypochlorite'
                            res += "| " + str(curr_water_level) + " |\n"

                return res #output will be a visual representation of the water tube

            def add_water_level(self, water): #checks whether it is possible to add an additional compound (if bottle is not full)
               
                # type: (Water) -> bool
                if len(self.__water_levels) < self.BOTTLE_CAPACITY: #at lower levels, BOTTLE CAPACITY = 5 --> "when the water level (i.e. compounds) is less than full bottle capacity)
                    self.__water_levels.append(water)
                    return True
                return False

            def pour_water(self, other_bottle):
                # type: (Bottle) -> bool
                self_last: Water = self.get_last_water_level() 
                other_last: Water = other_bottle.get_last_water_level() #retrieve top item in another bottle (called by method) #applies list of compounds as method on other_bottle
                if self_last == None:
                    return False
                if len(other_bottle.get_water_levels()) >= self.BOTTLE_CAPACITY: #length of list of compounds in other bottle exceeds or equals Bottle Capacity return False 
                    return False
                if other_last is None or (self_last in Water.WATER  and  other_last in Water.WATER) or (self_last in Water.TABLE_SALT and other_last in Water.TABLE_SALT) or (self_last in Water.BAKING_SODA and other_last in Water.BAKING_SODA) or (self_last in Water.BLEACH and other_last in Water.BLEACH) or (self_last in Water.EPSOM_SALT and other_last in Water.EPSOM_SALT) or (self_last in Water.QUARTZ and other_last in Water.QUARTZ) or len(other_bottle.__water_levels) == 0: #If the bottle is empty (written twice) or the top colors of both bottles are the same
                    self.__water_levels.remove(self_last) #Removes the last item (top compound) from the list of the current bottle
                    other_bottle.add_water_level(self_last) #Adds the last item (top compound) from the list of the current bottle to the end of the other bottle list (top of bottle)
                    return True 
                return False

            def get_last_water_level(self):
                # type: () -> Water or None
                if len(self.__water_levels) > 0: #if there are compounds in list (bottle is not empty)
                    return self.__water_levels[len(self.__water_levels) - 1] #call last item of list
                else:
                    return None

            def sorted(self):
                # type: () -> bool
                if len(self.__water_levels) == 0:
                    return True
                else:
                    curr_colour: str = self.__water_levels[0] #check if first item (bottom of bottle) of randomly selected list of compounds is in possible compounds + assign string to variable
                    #for compounds in self.__water_levels: #for every compound in that list of compound
                    length = len(self.__water_levels)
                    i = 0
                    trues = []
                    while i < length:
                        if (self.__water_levels[i] in Water.WATER and curr_colour in Water.WATER) or (self.__water_levels[i] in Water.TABLE_SALT and curr_colour in Water.TABLE_SALT) or (self.__water_levels[i] in Water.BAKING_SODA and curr_colour in Water.BAKING_SODA) or (self.__water_levels[i] in Water.BLEACH and curr_colour in Water.BLEACH) or (self.__water_levels[i] in Water.EPSOM_SALT and curr_colour in Water.EPSOM_SALT) or (self.__water_levels[i] in Water.QUARTZ and curr_colour in Water.QUARTZ):
                            trues.append(1)
                            i += 1
                        else:
                            return False
                    if len(trues) == length:
                        return True 

            def get_water_levels(self): #eturns compound list (in tube) when called --> makes self.__water_levels a method
                # type: () -> list
                return self.__water_levels 

            def clone(self):
                # type: () -> Bottle
                return copy.deepcopy(self) #returns clone of object (completely independent from original)


        class Water: # second important object of the game
            """
            This class contains attributes of water
            """
            WATER = ["H\N{SUBSCRIPT TWO}O", "Dihydrogen monoxide", "Water"] #added subscript for H2O
            TABLE_SALT = ["NaCl", "Sodium chloride", "Table salt"]
            BAKING_SODA = ["NaHCO\N{SUBSCRIPT THREE}", "Sodium bicarbonate", "Baking soda"] #added subscript for NAHCO3
            BLEACH = ["NaOCl", "Sodium hypochlorite", "Bleach"]
            EPSOM_SALT = ["MgSO\N{SUBSCRIPT FOUR}", "Magnesium sulfate", "Epsom salt"]#added subscript for MgSO4
            QUARTZ = ["SiO\N{SUBSCRIPT TWO}","Silicon dioxide","Quartz"] #added subscript for SiO2

            POSSIBLE_COLOURS: list = [WATER, TABLE_SALT, BAKING_SODA, BLEACH, EPSOM_SALT, QUARTZ] #constant list

            def __init__(self, colour): #initializing, attributing color to self
                # type: (str) -> None
                if colour in self.WATER or colour in self.TABLE_SALT or colour in self.BAKING_SODA or colour in self.BLEACH or colour in self.EPSOM_SALT or colour in self.QUARTZ: 
                    self.colour: str = colour  #assign 1 compound to object. 
                else:
                    self.colour = self.WATER[0]

            def __str__(self): #generates user-readable/usable output (from __init__)
                # type: () -> str
                return str(self.colour) #compound from __init__

            def clone(self):
                # type: () -> Water
                return copy.deepcopy(self) #returns a clone of the object (completely separate from original)


        # Creating main function used to run the game.


        def main():
            """
            This function is used to run the game.
            :return: None
            """
            
            print()
            print("Welcome to Chemist's Jumble.") 
            print("In this game, you are required to make sure that each beaker only contains one type of chemical compound.") 
            print()
            print("Enter 'Y' for yes.") 
            print("Enter anything else for no and exit the game.")  
            level: int = 1 #defines variable "level" (int) as initially equal to 1
            continue_playing: str = input("Do you want to play 'Chemist's Jumble'? ") #Defines a variable "continue_playing" for users input (string)
            while continue_playing == "Y" or continue_playing == "y":
                bottles: list = []  #instantiate "bottles" as an empty list
                number_of_bottles: int = 5 + (level // 5) #defines a variable for the number of bottles (int) and is equal to 5 plus integer division of the level number by 5 
                                                        #at levels 1&2 there'll be 5 bottles
                number_of_empty_bottles: int = number_of_bottles // 5 #defines a variable for the number of empty bottles (int) and is equal to the number of bottles integer divided by 5
                                                                    #at 5 total bottles, there'll only be one empty
                possible_colours: list = Water.POSSIBLE_COLOURS if number_of_bottles >= 10 else Water.POSSIBLE_COLOURS[0:4] #creates list of possible compound --> all of original possible compounds if there are 10+ bottles
                for i in range(number_of_empty_bottles): #loop will run for every empty bottle. 1 empty bottle -> range = [0]
                    bottles.append(Bottle([])) #creating empty bottles/empty lists (level 1 will have 1 empty bottle)

                for i in range(number_of_bottles - number_of_empty_bottles): #loop will run for every filled bottle
                    water_levels: list = []  
                    for j in range(3): 
                        group = possible_colours[random.randint(0, len(possible_colours) - 1)]
                        water_levels.append(group[random.randint(0, 2)]) #generates a random integer to be used as the index for the constant list of possible compounds defined in Water then appends that entry (compound) to the list water_levels

                    bottles.append(Bottle(water_levels)) #append the list created above to the object bottles + applying it to the class Bottle

                while not all_bottles_sorted(bottles): #while the user hasn't sorted like compound into one tube
                    clear()

                    print("You are now at level " + str(level))
                    print("Current representation of each beaker is as below.\n") 
                    for bottle in bottles: #for every item (bottle, which contain compound) in list of bottles created above
                        print(str(bottle) + "\n") 

                    bottle_from_index: int = input("Please enter index of beaker you want to pour chemical compound from " #asks user to pick a bottle (take color out of it)
                                                    "(1 - " + str(len(bottles)) + "): ")
                    if bottle_from_index == "r":
                            break
                    bottle_to_index: int = input("Please enter index of beaker you want to pour chemical compound to "  #asks user for recipient bottle (put color into it)
                                                    "(1 - " + str(len(bottles)) + "): ")
                    if bottle_to_index == "r":
                            break
                    while (is_int(bottle_from_index) == False or is_int(bottle_to_index) == False):
                        print("Invalid input! A different input is expected!") #checks for numerically invalid inputs (not TypeError inputs)
                        bottle_from_index = input("Please enter index of beaker you want to pour chemical compound from "
                                                    "(1 - " + str(len(bottles)) + "): ") #restates request for input (in case previous one was invalid)
                        if bottle_from_index == "r":
                            break
                        bottle_to_index = input("Please enter index of beaker you want to pour chemical compound to "
                                                    "(1 - " + str(len(bottles)) + "): ")
                        if bottle_to_index == "r":
                            break
                    bottle_from_index = int(bottle_from_index)
                    bottle_to_index = int(bottle_to_index)
                    while bottle_from_index < 1 or bottle_from_index > len(bottles) or bottle_to_index < 1 or bottle_to_index > len(bottles) or bottle_from_index == bottle_to_index:
                        print("Invalid input! A different input is expected!") #checks for numerically invalid inputs (not TypeError inputs)
                        bottle_from_index = input("Please enter index of beaker you want to pour chemical compound from "
                                                    "(1 - " + str(len(bottles)) + "): ") #restates request for input (in case previous one was invalid)
                        if bottle_from_index == "r":
                            break
                        bottle_to_index = input("Please enter index of beaker you want to pour chemical compound to "
                                                    "(1 - " + str(len(bottles)) + "): ")
                        if bottle_to_index == "r":
                            break
                        while (is_int(bottle_from_index) == False or is_int(bottle_to_index) == False):
                            print("Invalid input! A different input is expected!") #checks for numerically invalid inputs (not TypeError inputs)
                            bottle_from_index = input("Please enter index of beaker you want to pour chemical compound from "
                                                        "(1 - " + str(len(bottles)) + "): ") #restates request for input (in case previous one was invalid)
                            if bottle_from_index == "r":
                                break
                            bottle_to_index = input("Please enter index of beaker you want to pour chemical compound to "
                                                        "(1 - " + str(len(bottles)) + "): ")
                            if bottle_to_index == "r":
                                break
                        bottle_from_index = int(bottle_from_index)
                        bottle_to_index = int(bottle_to_index)
                    
                    
                        
                    bottle_from: Bottle = bottles[bottle_from_index - 1] #new variable refering to class Bottle --> picks bottle (from bottles) chosen by user with corresponding index 
                    bottle_to: Bottle = bottles[bottle_to_index - 1] #picks bottle (from bottles) to receive compound --> from index chosen by user
                    bottle_from.pour_water(bottle_to) #applies method pour_water (from Bottle) with bottle_from as self and bottle_to as other_bottle

                if all_bottles_sorted(bottles):
                    for bottle in bottles: # for every item (bottle, which contain compounds) in list of bottles created above
                        print(str(bottle) + "\n") #actually displays bottles built in Bottle
                    print ("Congratulations! Ace that chem exam ;)")
                    level += 1
                    print("Enter 'Y' for yes.") 
                    print("Enter anything else to return to game selection.")
                    continue_playing = input("Do you want to continue playing Chemist's Jumble? ") #once bottles are sorted, asks if while loop should continue


        if __name__ == '__main__': #run only as script
            main()

    elif user_input == "3":
            # Creating necessary functions to be used throughout the game.

        def is_int(possible) :
            try:
                int(possible)
            except ValueError:
                return False
            else :
                return True

        def clear(): #test for a specific system version -> being able to run in different operating systems
            # type: () -> None
            if sys.platform.startswith('win'):
                os.system('cls')  
            else:
                os.system('clear') 


        def all_bottles_sorted(bottles: list) -> bool: #bool shows what the function will return but does not force function to return bool (solely for readability)
            #variable: list - indicates that the input will be in list form
            if len(bottles) == 0: 
                return True
            else:
                for bottle in bottles:
                    if not bottle.sorted(): #from sorted() method in Bottles. Check if foxes/chickens/corn in all bottles are sorted
                        return False

                return True 


        # Creating necessary classes


        class Bottle: #'Bottle' is the name of the class
            """
            This class contains attributes of a water bottle.
            """

            BOTTLE_CAPACITY: int = 5 #constant

            def __init__(self, water_levels=None): # __init__ (method) - initializes object's attributes
                #None is default if water_levels not defined by user
                # type: (list) -> None
                if water_levels is None: #avoid error, list will always be given
                    water_levels =  [] 
                self.__water_levels: list = water_levels #bind object (self) to water_levels so that every instance (object created) reassigns water_levels

            def __str__(self): # __str__ (method) - actuator of the class (it actually prints/performs what need)
                # type: () -> str
                res: str = ""  # initial value (empty string). Initiating string that will 'draw' the bottle
                    #THIS WILL BUILD ONE SINGLE TUBE
                for i in range(self.BOTTLE_CAPACITY - 1, -1, -1): # binding object to BOTTLE_CAPACITY
                    if i >= len(self.__water_levels): #for every level of the actual bottle (4, 3, 2, 1, 0), if number is greater or equal to the length of the list, the string is reset to 'empty walls of the tube' 
                        # if the bottle capacity is greater than the water level --> for empty lists(water_levels), loop will run 5 times (create a tube with 5 lines of walls)
                        res += "|       |\n" 
                    else: # in case self's list is not empty
                        curr_water_level: Water = self.__water_levels[i] # indexes 0, 1, 2, 3, 4 of list of organism levels --> meant to align empty and filled tube wall sections
                        if len(str(curr_water_level)) == 1:
                            res += "|   " + str(curr_water_level) + "  |\n"

                return res #output will be a visual representation of the water tube

            def add_water_level(self, water): #checks whether it is possible to add an additional foxes/chickens/corn (if bottle is not full)
                # type: (Water) -> bool
                if len(self.__water_levels) < self.BOTTLE_CAPACITY: # at lower levels, BOTTLE CAPACITY = 5 --> "when the water level (i.e. foxes/plants/chickens) is less than full bottle capacity)
                    self.__water_levels.append(water)
                    return True
                return False

            def pour_water(self, other_bottle):
                # type: (Bottle) -> bool
                self_last: Water = self.get_last_water_level() # retrieve last (top) item in current bottle
                other_last: Water = other_bottle.get_last_water_level() # retrieve top item in another bottle (called by method) #applies list of foxes/chickens/corn as method on other_bottle
                if self_last == None:
                    return False
                if len(other_bottle.get_water_levels()) >= self.BOTTLE_CAPACITY: #length of list of foxes/chickens/corn in other bottle exceeds or equals Bottle Capacity return False 
                    return False
                if other_last is None or self_last.colour == other_last.colour or len(other_bottle.__water_levels) == 0: # If the bottle is empty (written twice) or the top foxes/plants/chickens of both bottles are the same
                    self.__water_levels.remove(self_last) 
                    other_bottle.add_water_level(self_last) 
                    return True # game will continue running
                return False

            def get_last_water_level(self):
                # type: () -> Water or None
                if len(self.__water_levels) > 0: # if there are foxes/chickens/corn in list (bottle is not empty)
                    return self.__water_levels[len(self.__water_levels) - 1] # calls last item of list
                else:
                    return None

            def sorted(self):
                # type: () -> bool
                if len(self.__water_levels) == 0: # if bottle is empty = automatically sorted
                    return True
                else:
                    curr_colour: str = self.__water_levels[0].colour # check if first item (bottom of bottle) of randomly selected list of foxes/plants/chickens is in possible foxes/plants/chickens + assign string to variable
                    for water in self.__water_levels: #for every foxes/chickens/corn in that list of foxes/plants/chickens
                        if water.colour != curr_colour: # if the foxes/chickens/corn in that original list are not equal to bottom foxes/plants/chickens, return False
                            return False

                    return True

            def get_water_levels(self): # returns foxes/chickens/corn list (in tube) when called --> makes self.__water_levels a method
                # type: () -> list
                return self.__water_levels 

            def clone(self):
                # type: () -> Bottle
                return copy.deepcopy(self) # returns clone of object (completely independent from original)


        class Water: # second important object of the game
            """
            This class contains attributes of water
            """

            POSSIBLE_COLOURS: list = ["🌽", "🐔", "🦊"] 

            def __init__(self, colour): #initializing, attributing foxes/plants/chickens to self
                # type: (str) -> None
                self.colour: str = colour if colour in self.POSSIBLE_COLOURS else self.POSSIBLE_COLOURS[0] #assign 1 foxes/chickens/corn to object. 
            def __str__(self): # generates user-readable/usable output (from __init__)
                # type: () -> str
                return str(self.colour) #color from __init__

            def clone(self):
                # type: () -> Water
                return copy.deepcopy(self) #returns a clone of the object (completely separate from original)


        # Creating main function used to run the game.


        def main():
            """
            This function is used to run the game.
            :return: None
            """
            print()
            print("Welcome to 'Farmer's Hustle'.")
            print("You are farmer. You have a pen of chickens and a cornfield. Recently you discovered that the jealous Farmer Dave, your nemesis, has released your chickens into your cornfield. \nWhen you went to catch them, \
        you spotted a family of foxes attempting to have chicken for lunch. Your job is to separate them all before \
        it's too late.")
            print ("---------")
            print ("Once you start (enter \"Y\"), you have 60 seconds to complete your task before all is lost.")
            print("Once 60 seconds are up, you can finish your move before the chickens claim your corn and the foxes devour you chickens.")
            print()
            print("Enter 'Y' for yes.")
            print("Enter anything else for no and exit the game.")  
            level: int = 1 
            continue_playing: str = input("Do you want to play 'Farmer Hustle'? ")
            while continue_playing == "Y" or continue_playing == "y":
                bottles: list = []  
                number_of_bottles: int = 5 + (level // 5) #defines a variable for the number of bottles (int) and is equal to 5 plus integer division of the level number by 5 
                                                        #at levels 1&2 there'll be 5 bottles
                number_of_empty_bottles: int = number_of_bottles // 5 #defines a variable for the number of empty bottles (int) and is equal to the number of bottles integer divided by 5
                                                                    #at 5 total bottles, there'll only be one empty
                possible_colours: list = Water.POSSIBLE_COLOURS if number_of_bottles >= 10 else Water.POSSIBLE_COLOURS[0:4] #creates list of possible colours: all of original possible foxes/plants/chickens if there are 10+ bottles
                                                                                                                            
                                                                                                                          
                for i in range(number_of_empty_bottles): #loop will run for every empty bottle. 1 empty bottle -> range = [0]
                    bottles.append(Bottle([])) #creating empty bottles/empty lists (level 1 will have 1 empty bottle)

                for i in range(number_of_bottles - number_of_empty_bottles): #loop will run for every filled bottle
                    water_levels: list = []  #defines a empty list "water_levels"
                    for j in range(4):
                        water_levels.append(Water(possible_colours[random.randint(0, len(possible_colours) - 1)])) #generates a random integer to be used as the index for the constant list of possible foxes/plants/chickens defined in Water then appends that entry (foxes/plants/chickens) to the list water_levels

                    bottles.append(Bottle(water_levels)) #append the list created above to the object bottles + applying it to the class Bottle

                start_time = time.time()
                time_limit = start_time + 60
                time_bool = True
                while time_bool == True:

                    while not all_bottles_sorted(bottles): #while the user hasn't sorted like colors into one tube
                        clear()

                        print("You are now at level " + str(level))
                        print("Current representation of each barn is as below.\n") 
                        for bottle in bottles: #for every item (bottle, which contain foxes/plants/chickens) in list of bottles created above
                            print(str(bottle) + "\n") #actually displays bottles built in Bottle

                        bottle_from_index: int = input("Please enter index of barn you want to move organism from " 
                                                        "(1 - " + str(len(bottles)) + "): ") 
                        
                        bottle_to_index: int = input("Please enter index of barn you want to move organism to "
                                                        "(1 - " + str(len(bottles)) + "): ")
                        while (is_int(bottle_from_index) == False or is_int(bottle_to_index) == False):
                            print("Invalid input! A different input is expected!") # checks for numerically invalid inputs (not TypeError inputs)
                            bottle_from_index = input("Please enter index of barn you want to move organism from "
                                                        "(1 - " + str(len(bottles)) + "): ") 
                            bottle_to_index = input("Please enter index of water bottle you want to move organism to "
                                                        "(1 - " + str(len(bottles)) + "): ")
                        bottle_from_index = int(bottle_from_index)
                        bottle_to_index = int(bottle_to_index)
                        while bottle_from_index < 1 or bottle_from_index > len(bottles) or bottle_to_index < 1 or bottle_to_index > len(bottles) or bottle_from_index == bottle_to_index:
                            print("Invalid input! A different input is expected!") #checks for numerically invalid inputs (not TypeError inputs)
                            bottle_from_index = input("Please enter index of barn you want to move organism from "
                                                        "(1 - " + str(len(bottles)) + "): ")
                            bottle_to_index = input("Please enter index of barn you want to move organism to "
                                                        "(1 - " + str(len(bottles)) + "): ")
                            while (is_int(bottle_from_index) == False or is_int(bottle_to_index) == False):
                                print("Invalid input! A different input is expected!") #checks for numerically invalid inputs (not TypeError inputs)
                                bottle_from_index = input("Please enter index of barn you want to move organism from "
                                                            "(1 - " + str(len(bottles)) + "): ") 
                                bottle_to_index = input("Please enter index of barn you want to move organism to "
                                                            "(1 - " + str(len(bottles)) + "): ")
                            bottle_from_index = int(bottle_from_index)
                            bottle_to_index = int(bottle_to_index)
                    
                        bottle_from: Bottle = bottles[bottle_from_index - 1] # new variable refering to class Bottle --> picks bottle (from bottles) chosen by user with corresponding index 
                        bottle_to: Bottle = bottles[bottle_to_index - 1] #picks bottle (from bottles) to receive color --> from index chosen by user
                        bottle_from.pour_water(bottle_to) #applies method pour_water (from Bottle) with bottle_from as self and bottle_to as other_bottle
                        a = time.time()
                        if a > time_limit:
                            break
                    
                    if all_bottles_sorted(bottles):
                        for bottle in bottles: # for every item (bottle, which contain foxes/plants/chickens) in list of bottles created above
                            print(str(bottle) + "\n") #actually displays bottles built in Bottle
                        level += 1
                        print ("Congratulations, farmer! You have saved your chickens and crops from imminent doom (maybe you should consider giving the foxes a treat ;) )")
                        break


                    if time.time() > time_limit:
                        print("")
                        print ("Your time's up! \nYour chickens have eaten the corn and the foxes have eaten your chickens :(")
                        print("")
                        time_bool = False
                        break
                
                continue_playing = input("Do you want to continue playing 'Farmer Hustle'? ") # once bottles are sorted, asks if while loop should continue
                print("Enter 'Y' for yes.") 
                print("Enter anything else to return to game selection.")

        if __name__ == '__main__': 
            main()

    elif user_input == "4":
        sys.exit()

    else:
        print("A different input was expected. Please try again.")
