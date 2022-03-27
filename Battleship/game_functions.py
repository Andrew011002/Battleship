import random as rn
import time

from miscellaneous import *
from display_functions import display
from constants import ALPHABET, TAB, bcolors



#   Asking for magic number function needs to be fixed 
def askNum():
    display("Guess a number between 0 & 100", style="")
    userInput = input(f"{TAB}{''.center(DISPLAYWIDTH // 2)}").strip()
    # Validating input 
    if userInput.isnumeric() and not userInput.isalpha():
        if 0 <= int(userInput) <= 100:
            return int(userInput)
        # Handling errors
        else:
            display("INVALID INPUT, TRY AGAIN!", color=bcolors.RED, center=True)
            time.sleep(1)
            return askNum()
    # Handling errors
    else:
        display(f"INVALID INPUT, TRY AGAIN!", color=bcolors.RED, center=True)
        time.sleep(1)
        return askNum()

# Generates random magic number and number for AI, then gets players number
def turnOrder():
        ranNum = rn.randint(1, 100)
        AINum = rn.randint(1, 100)
        playerNum = askNum()
        # Time before showing results numbers
        time.sleep(2)
        # See who's value is closer to ranNun
        display(f"Your number was {playerNum}. The AI's number was {AINum}. The magic number was {ranNum}", style = "")
        # least absolute difference is the winner
        # Time before showing who won
        time.sleep(3)
        if abs(ranNum - playerNum) < abs(ranNum - AINum):
            display("You won! You get to go first...", color = bcolors.GREEN, style="")
        # need to return True or False to see who gets to go first
        # AI is False player is True
            return True
        # If there's a tie breaker this will run the the function again
        elif playerNum == AINum:
            display("There's  a tie. Let's re-pick", color = bcolors.YELLOW, style="")
            time.sleep(2)
            return turnOrder()
        else:
            display("You lost. The AI gets to go first...", color = bcolors.RED, style="")
            return False
        # Make turn function that asks for coordinates of ships
        # Need to display grids as well

# TODO
def askPlayer(mem = [], clear = False):
    if clear:
        mem.clear()
        return None
    # Make sure inputs are valid
    display("Enter the position to attack", style = bcolors.ITALIC, center = True)
    pos = input(f"{TAB}{''.center(DISPLAYWIDTH // 2)}").strip()
    # filter the input only num and letters
    pos = "".join(c for c in pos if c.isalnum() or c == " ")
    pos = pos.replace(" ", "")
    # checking for correct format
    if 2 <= len(pos) <= 3:
        if pos[0].isalpha() and pos[1:].isdigit():
            # valid row
            if 0 <= int(pos[1:]) <= 25:
                # col row index
                choice = [pos[0].upper(), int(pos[1:])]
                # no repeats
                if choice not in mem:
                    mem.append(choice)
                    time.sleep(1) # time before showing players selection
                    display(f"Row: {choice[1]} Column: {choice[0]}", center=True)
                    return choice
                else:
                    display("Make a different selection please", style=bcolors.ITALIC, center=True)
            
    # error case
    display("INVALID POSITION", color=bcolors.RED, center=True)
    return askPlayer()
    

def askAI(mem = [], s = [], clear = False):    
    if clear:
        # Clearing memory & ships for new games
        mem.clear()
        s.clear()
        return None
    # All possible choice
    if not mem:
        for letter in ALPHABET:
            for i in range(26):
                mem.append([letter, i])
    
    # A ship exist with more than one choice
    if s:
        # ship location in numbers
        index = rn.choice(s)
        # changing choice back to original format
        choice = [revertAlpha(index[1]), index[0]]
    else:
        # The selection
        choice = rn.choice(mem)
        # ALl choices
    if len(mem) == (26 ** 2):
        display(f"AI: for my first selecion, I am going to do column {choice[0]} and row {choice[1]}.", color=bcolors.RED, style = "")
    else:
        display(f"AI: for my next selecion, I am going to do column {choice[0]} and row {choice[1]}.", color = bcolors.RED, style = "")
    # TODO
    # Fail Safe for some random bug I don't know yet
    if choice in mem:
        mem.remove(choice)

    # choice return
    return choice

def shipFinder(target, ships):
    # print(f"Target: {target}\nShips: {ships}")
    # If there is a ship
    if ships:
        # Contains the series of indicies
        for ship in ships:
            # index of piece
            for location in ship:
                # piece and target match
                if target == location:
                    # location already used to hit ship so remove
                    ship.remove(location)
            
                    # ship found so return it
                    return ship
    # For whatever reason the ship isn't found
    return False

# Makes sure a piece isn't are stored in a ship array
def found(check, ships):
    # handling
    if ships:
        # ship list
        for ship in ships:
            # location as tuple row column pair
            for location in ship:
                # found a match
                if check == location:
                    # we don't want that
                    return False

    # After all iterations with no return we're safe
    return True

