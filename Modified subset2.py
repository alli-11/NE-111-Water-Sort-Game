"""
This file contains code for the game "Water Sort Puzzle".
Author: GlobalCreativeCommunityFounder
Edited by: Alli Miles, Victoria Cella Xia, Fatima Varela Varela, Esha Saleem 
"""
# Importing necessary libraries
import copy #V: module with functions that allow copying elements/objects from lists, arrays, etc.
import sys #A: module that provides info on constants/functions/methods of python interpreter
import os #F: module that provides functions to interact with operating system info and control processes
import random #E&A: module that gives access to  functions that manipulate random integers
import time

# Creating necessary functions to be used throughout the game.

def is_int(possible) :
    try:
        int(possible)
    except ValueError:
        return False
    else :
        return True

def clear(): #V&A: test for a specific system version -> being able to run in different operating systems
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


def all_bottles_sorted(bottles: list) -> bool: #All: -> bool shows what the function will return but does not force function to return bool (solely for readability)
    # All: variable: list - indicates that the input will be in list form
    if len(bottles) == 0: #A: if there are no bottles, all bottles are sorted
        return True
    else:
        for bottle in bottles:
            if not bottle.sorted(): #from sorted() method in Bottles. Check if all colors in all bottles are sorted
                return False

        return True #prediction: return False for unsorted bottles in 'bottles' then return True if all bottles are sorted


# Creating necessary classes


class Bottle: #A: 'Bottle' is the name of the class
    """
    This class contains attributes of a water bottle.
    """

    BOTTLE_CAPACITY: int = 5 #constant

    def __init__(self, water_levels=None): #V&A: __init__ (method) - initializes object's attributes
        #F: None is default if water_levels not defined by user
        # type: (list) -> None
        if water_levels is None: #V: avoid error, list will always be given
            water_levels =  [] #V: in case no list is given - later filled with COLORS
        self.__water_levels: list = water_levels #V&A: bind object (self) to water_levels so that every instance (object created) reassigns water_levels

    def __str__(self): #F: __str__ (method) - actuator of the class (it actually prints/performs what need)
        # type: () -> str
        res: str = ""  #V: initial value (empty string). Initiating string that will 'draw' the bottle
            #THIS WILL BUILD ONE SINGLE TUBE
        for i in range(self.BOTTLE_CAPACITY - 1, -1, -1): #F: binding object to BOTTLE_CAPACITY #Range(4, -1, -1) -> [4, 0] 
            if i >= len(self.__water_levels): #V: for every level of the actual bottle (4, 3, 2, 1, 0), if number is greater or equal to the length of the list, the string is reset to 'empty walls of the tube' 
                #V: if the bottle capacity is greater than the water level --> for empty lists(water_levels), loop will run 5 times (create a tube with 5 lines of walls)
                res += "|       |\n" 
            else: #V: in case self's list is not empty
                curr_water_level: Water = self.__water_levels[i] #V: indexes 0, 1, 2, 3, 4 of list of water levels --> meant to align empty and filled tube wall sections
                if len(str(curr_water_level)) == 1:
                    res += "|   " + str(curr_water_level) + "  |\n"

        return res #output will be a visual representation of the water tube

    def add_water_level(self, water): #A: checks whether it is possible to add an additional color (if bottle is not full)
        #A&V: through logic we think 'water' must be a color
        # type: (Water) -> bool
        if len(self.__water_levels) < self.BOTTLE_CAPACITY: #A&V: at lower levels, BOTTLE CAPACITY = 5 --> "when the water level (i.e. colors) is less than full bottle capacity)
            self.__water_levels.append(water)
            return True
        return False

    def pour_water(self, other_bottle):
        # type: (Bottle) -> bool
        self_last: Water = self.get_last_water_level() #A&V: retrieve last (top) item in current bottle
        other_last: Water = other_bottle.get_last_water_level() #A&V: retrieve top item in another bottle (called by method) #V: applies list of colors as method on other_bottle
        if len(other_bottle.get_water_levels()) >= self.BOTTLE_CAPACITY: #A&V: length of list of colors in other bottle exceeds or equals Bottle Capacity return False 
            return False
        if other_last is None or self_last.colour == other_last.colour or len(other_bottle.__water_levels) == 0: #A&V: If the bottle is empty (written twice) or the top colors of both bottles are the same
            self.__water_levels.remove(self_last) #V: Removes the last item (top color) from the list of the current bottle
            other_bottle.add_water_level(self_last) #A: Adds the last item (top color) from the list of the current bottle to the end of the other bottle list (top of bottle)
            return True #V: so that the game will continue running
        return False

    def get_last_water_level(self):
        # type: () -> Water or None
        if len(self.__water_levels) > 0: #A&V: if there are colors in list (bottle is not empty)
            return self.__water_levels[len(self.__water_levels) - 1] #A&V: call last item of list
        else:
            return None

    def sorted(self):
        # type: () -> bool
        if len(self.__water_levels) == 0: #A&V: if bottle is empty = automatically sorted
            return True
        else:
            curr_colour: str = self.__water_levels[0].colour #A&V: check if first item (bottom of bottle) of randomly selected list of colors is in possible colors + assign string to variable
            for water in self.__water_levels: #for every color in that list of colors
                if water.colour != curr_colour: #A&V: if the colors in that original list are not equal to bottom color, return False
                    return False

            return True

    def get_water_levels(self): #A&V: returns color list (in tube) when called --> makes self.__water_levels a method
        # type: () -> list
        return self.__water_levels 

    def clone(self):
        # type: () -> Bottle
        return copy.deepcopy(self) #A&V: returns clone of object (completely independent from original)


class Water: #V: second important object of the game
    """
    This class contains attributes of water
    """

    POSSIBLE_COLOURS: list = ["🌽", "🐔", "🦊"] #A: constant list

    def __init__(self, colour): #A&V: initializing, attributing color to self
        # type: (str) -> None
        self.colour: str = colour if colour in self.POSSIBLE_COLOURS else self.POSSIBLE_COLOURS[0] #A&V: assign 1 color to object. Deafult is blue

    def __str__(self): #A&V: generates user-readable/usable output (from __init__)
        # type: () -> str
        return str(self.colour) #color from __init__

    def clone(self):
        # type: () -> Water
        return copy.deepcopy(self) #A: returns a clone of the object (completely separate from original)


# Creating main function used to run the game.


def main():
    """
    This function is used to run the game.
    :return: None
    """

    print("Welcome to 'Water Sort Puzzle' by 'GlobalCreativeCommunityFounder'.") #A: Prints welcome on the screen
    print("You are farmer. You have a pen of chickens and a cornfield. Recently you discovered that the jealous Farmer Dave, your nemesis, has released your chickens into your cornfield. \nWhen you went to catch them, \
you spotted a family of foxes attempting to have chicken for lunch. Your job is to separate them all before \
it's too late.")
    print ("~ ~ ~ ~ ~")
    print ("Once you start (enter \"Y\"), you have 40 seconds to complete your task before all is lost.")
    print("Once 40 seconds are up, you can finish your move before the chickens claim your corn and the foxes devour you chickens.")
    print("Enter 'Y' for yes.") #A: Prints instructions on the screen #V: asks for input
    print("Enter anything else for no.")  #A: Prints instructions on the screen
    level: int = 1 #A: defines variable "level" (int) as initially equal to 1
    continue_playing: str = input("Do you want to continue playing 'Water Sort Puzzle'? ") #E: Defines a variable "continue_playing" for users input (string)
    while continue_playing == "Y" or continue_playing == "y": #A: while the user's answer is yes/"Y" (they want to continue playing), the game code below will run
        bottles: list = []  #E: instantiate "bottles" as an empty list
        number_of_bottles: int = 5 + (level // 5) #A: defines a variable for the number of bottles (int) and is equal to 5 plus integer division of the level number by 5 
                                                  #V: at levels 1&2 there'll be 5 bottles
        number_of_empty_bottles: int = number_of_bottles // 5 #A: defines a variable for the number of empty bottles (int) and is equal to the number of bottles integer divided by 5
                                                              #V: at 5 total bottles, there'll only be one empty
        possible_colours: list = Water.POSSIBLE_COLOURS if number_of_bottles >= 10 else Water.POSSIBLE_COLOURS[0:4] #A: creates list of possible colours:
                                                                                                                    #all of original possible colours if there are 10+ bottles
                                                                                                                    #object 1, 2, 3, 4 from the original list of possible colours if not
        for i in range(number_of_empty_bottles): #V: loop will run for every empty bottle. 1 empty bottle -> range = [0]
            bottles.append(Bottle([])) #A&V: creating empty bottles/empty lists (level 1 will have 1 empty bottle)

        for i in range(number_of_bottles - number_of_empty_bottles): #V: loop will run for every filled bottle
            water_levels: list = []  #A: defines a empty list "water_levels"
            for j in range(4): #A: for 0, 1, 2, 3 (4 times total)
                water_levels.append(Water(possible_colours[random.randint(0, len(possible_colours) - 1)])) #A: generates a random integer to be used as the index for the constant list of possible colors defined in Water then appends that entry (color) to the list water_levels

            bottles.append(Bottle(water_levels)) #A&V: append the list created above to the object bottles + applying it to the class Bottle

        start_time = time.time()
        time_limit = start_time + 40
        time_bool = True
        while time_bool == True:

            while not all_bottles_sorted(bottles): #A&V: while the user hasn't sorted like colors into one tube
                clear()

                print("You are now at level " + str(level))
                print("Current representation of each bottle is as below.\n") #A&V: prints both statements before the game starts
                for bottle in bottles: #V: for every item (bottle, which contain colors) in list of bottles created above
                    print(str(bottle) + "\n") #A&V: actually displays bottles built in Bottle

                bottle_from_index: int = input("Please enter index of water bottle you want to pour bottle from " #A&V: asks user to pick a bottle (take color out of it)
                                                "(1 - " + str(len(bottles)) + "): ") #REMINDER: ADD INTEGER CHECK
                bottle_to_index: int = input("Please enter index of water bottle you want to pour bottle to " #A&V: asks user for recipient bottle (put color into it)
                                                "(1 - " + str(len(bottles)) + "): ")
                while (is_int(bottle_from_index) == False or is_int(bottle_to_index) == False):
                    print("Invalid input! A different input is expected!") #A&V: checks for numerically invalid inputs (not TypeError inputs)
                    bottle_from_index = input("Please enter index of water bottle you want to pour bottle from "
                                                "(1 - " + str(len(bottles)) + "): ") #A&V: restates request for input (in case previous one was invalid)
                    bottle_to_index = input("Please enter index of water bottle you want to pour bottle to "
                                                "(1 - " + str(len(bottles)) + "): ")
                bottle_from_index = int(bottle_from_index)
                bottle_to_index = int(bottle_to_index)
                while bottle_from_index < 1 or bottle_from_index > len(bottles) or bottle_to_index < 1 or bottle_to_index > len(bottles) or bottle_from_index == bottle_to_index:
                    print("Invalid input! A different input is expected!") #A&V: checks for numerically invalid inputs (not TypeError inputs)
                    bottle_from_index = input("Please enter index of water bottle you want to pour bottle from "
                                                "(1 - " + str(len(bottles)) + "): ") #A&V: restates request for input (in case previous one was invalid)
                    bottle_to_index = input("Please enter index of water bottle you want to pour bottle to "
                                                "(1 - " + str(len(bottles)) + "): ")
                    while (is_int(bottle_from_index) == False or is_int(bottle_to_index) == False):
                        print("Invalid input! A different input is expected!") #A&V: checks for numerically invalid inputs (not TypeError inputs)
                        bottle_from_index = input("Please enter index of water bottle you want to pour bottle from "
                                                    "(1 - " + str(len(bottles)) + "): ") #A&V: restates request for input (in case previous one was invalid)
                        bottle_to_index = input("Please enter index of water bottle you want to pour bottle to "
                                                    "(1 - " + str(len(bottles)) + "): ")
                    bottle_from_index = int(bottle_from_index)
                    bottle_to_index = int(bottle_to_index)
            
                bottle_from: Bottle = bottles[bottle_from_index - 1] #A&V: new variable refering to class Bottle --> picks bottle (from bottles) chosen by user with corresponding index 
                bottle_to: Bottle = bottles[bottle_to_index - 1] #A&V: picks bottle (from bottles) to receive color --> from index chosen by user
                bottle_from.pour_water(bottle_to) #A&V: applies method pour_water (from Bottle) with bottle_from as self and bottle_to as other_bottle
                a = time.time()
                if a > time_limit:
                    break
            
            if all_bottles_sorted(bottles):
                for bottle in bottles: #V: for every item (bottle, which contain colors) in list of bottles created above
                    print(str(bottle) + "\n") #A&V: actually displays bottles built in Bottle
                print ("Congratulation, farmer! You have saved your chickens and crops from imminent doom (maybe you should consider giving the foxes a treat ;) )")
                break


            if time.time() > time_limit:
                print("")
                print ("Your time's up! \nYour chickens have eaten the corn and the foxes have eaten your chickens :(")
                print("")
                time_bool = False
                break
        
        continue_playing = input("Do you want to continue playing 'Water Sort Puzzle'? ") #A: once bottles are sorted, asks if while loop should continue
        print("Enter 'Y' for yes.") #A&V: printed after 'do you want to continue playing'
        print("Enter anything else for no.")
    sys.exit() #A&V: if user's input is anything other than "Y".


if __name__ == '__main__': #A: run only as script
    main()