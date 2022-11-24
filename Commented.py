"""
This file contains code for the game "Water Sort Puzzle".
Author: GlobalCreativeCommunityFounder
"""

# Importing necessary libraries
import copy #V: module with functions that allow copying elements/objects from lists, arrays, etc.
import sys #A: module that provides info on constants/functions/methods of python interpreter
import os #F: module that provides functions to interact with operating system info and control processes
import random #E&A: module that gives access to  functions that manipulate random integers


# Creating necessary functions to be used throughout the game.


def clear(): #needs clarification -> test for a specific system version -> being able to run in different operating systems
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


def all_bottles_sorted(bottles: list) -> bool: #All: -> bool shows what the function will return but does not force function to return bool (solely for readability)
    # All: variable: list - indicates that the input will be in list form
    if len(bottles) == 0:
        return True
    else:
        for bottle in bottles:
            if not bottle.sorted(): #in lexicographic order
                return False

        return True #prediction: return False for unsorted colors in every bottle in 'bottles' then return True for the game to continue


# Creating necessary classes


class Bottle: #F: blueprint for creating objects. 'Bottle' is object
    """
    This class contains attributes of a water bottle.
    """

    BOTTLE_CAPACITY: int = 5 #constant

    def __init__(self, water_levels=None): #__init__ (method) is a function called when object created from class - initializes object's attributes
        #F: None is default if water_levels not defined by user
        # type: (list) -> None
        if water_levels is None: #V: avoid error, list will always be given
            water_levels =  [] # in case no list is given
        self.__water_levels: list = water_levels #V&F: binding the attribute 'water_levels' to object Bottle (instance)

    def __str__(self): #F: __str__ (method) returns string representation of the object (self)
        # type: () -> str
        res: str = ""  # initial value (empty string)
        for i in range(self.BOTTLE_CAPACITY - 1, -1, -1): #F: binding bottle to BOTTLE_CAPACITY #Range(1, -1, -1) -> [1, 0]
            if i >= len(self.__water_levels):
                res += "|        |\n"
            else:
                curr_water_level: Water = self.__water_levels[i]
                if len(str(curr_water_level)) == 3:
                    res += "|   " + str(curr_water_level) + "  |\n"
                elif len(str(curr_water_level)) == 4:
                    res += "|  " + str(curr_water_level) + "  |\n"
                elif len(str(curr_water_level)) == 5:
                    res += "|  " + str(curr_water_level) + " |\n"
                else:
                    res += "| " + str(curr_water_level) + " |\n"

        return res

    def add_water_level(self, water):
        # type: (Water) -> bool
        if len(self.__water_levels) < self.BOTTLE_CAPACITY:
            self.__water_levels.append(water)
            return True
        return False

    def pour_water(self, other_bottle):
        # type: (Bottle) -> bool
        self_last: Water = self.get_last_water_level()
        other_last: Water = other_bottle.get_last_water_level()
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

    def get_water_levels(self):
        # type: () -> list
        return self.__water_levels

    def clone(self):
        # type: () -> Bottle
        return copy.deepcopy(self)


class Water:
    """
    This class contains attributes of water
    """

    POSSIBLE_COLOURS: list = ["BLUE", "RED", "ORANGE", "GREEN", "PURPLE", "YELLOW"]

    def __init__(self, colour):
        # type: (str) -> None
        self.colour: str = colour if colour in self.POSSIBLE_COLOURS else self.POSSIBLE_COLOURS[0]

    def __str__(self):
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

    print("Welcome to 'Water Sort Puzzle' by 'GlobalCreativeCommunityFounder'.") #A: Prints welcome game on the screen
    print("In this game, you are required to make sure that each water bottle only contains one colour of water.")
    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    level: int = 1  # initial value #A: defines variable "level" (which will be an int) as initially equal to 1
    continue_playing: str = input("Do you want to continue playing 'Water Sort Puzzle'? ") #E: Defines a variable asking user input (string)
    while continue_playing == "Y": #A: while the user's answer is yes/"Y" (they want to continue playing), the game code below will run
        bottles: list = []  # initial value #E: instantiate bottles as an empty list
        number_of_bottles: int = 5 + (level // 5) #A: defines a variable for the number of bottles that will be an int and is equal to 5 #V:at levels 1&2 there'll be 5 bottles
        number_of_empty_bottles: int = number_of_bottles // 5
        possible_colours: list = Water.POSSIBLE_COLOURS if number_of_bottles >= 10 else Water.POSSIBLE_COLOURS[0:4]
        for i in range(number_of_empty_bottles):
            bottles.append(Bottle([]))

        for i in range(number_of_bottles - number_of_empty_bottles):
            water_levels: list = []  # initial value
            for j in range(4):
                water_levels.append(Water(possible_colours[random.randint(0, len(possible_colours) - 1)]))

            bottles.append(Bottle(water_levels))

        while not all_bottles_sorted(bottles):
            clear()

            print("You are now at level " + str(level))
            print("Current representation of each bottle is as below.\n")
            for bottle in bottles:
                print(str(bottle) + "\n")

            bottle_from_index: int = int(input("Please enter index of water bottle you want to pour bottle from "
                                               "(1 - " + str(len(bottles)) + "): "))
            bottle_to_index: int = int(input("Please enter index of water bottle you want to pour bottle to "
                                             "(1 - " + str(len(bottles)) + "): "))
            while bottle_from_index < 1 or bottle_from_index > len(bottles) or bottle_to_index < 1 or \
                    bottle_to_index > len(bottles) or bottle_from_index == bottle_to_index:
                print("Invalid input! A different input is expected!")
                bottle_from_index = int(input("Please enter index of water bottle you want to pour bottle from "
                                              "(1 - " + str(len(bottles)) + "): "))
                bottle_to_index = int(input("Please enter index of water bottle you want to pour bottle to "
                                            "(1 - " + str(len(bottles)) + "): "))

            bottle_from: Bottle = bottles[bottle_from_index - 1]
            bottle_to: Bottle = bottles[bottle_to_index - 1]
            bottle_from.pour_water(bottle_to)

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_playing = input("Do you want to continue playing 'Water Sort Puzzle'? ")
    sys.exit()


if __name__ == '__main__':
    main()