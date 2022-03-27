from constants import DISPLAYWIDTH, ALPHABET, bcolors

def getExtra(line):
    return " " * (DISPLAYWIDTH - len(line))

# COVERTING FUNCTIONS

# Finds index in alphabet
def convertAlpha(letter):
        index = ALPHABET.find(letter.upper())
        return index

# Make's integer corresponding letter
def revertAlpha(index):
    return ALPHABET[index]

# Peeking into memory
def checkMem(memory):
    for p in memory:
        if type(p[0]) is int:
            return True
    return False

# MODIFYING FUNCTION(S)
# Changes grid based on where player targets
def updateGrid(gridList, index, AI = False):  
        # Converts letter to number index
        col = convertAlpha(index[0])
        row = index[1]
        # First Grid index is row (numeric), second index is column (charatcer)
        if gridList[row][col] == "=":
            gridList[row][col] = f"{bcolors.RED}X{bcolors.reset}"
            # When there's a hit
            return True
        # If it's not a hit it defaults to a miss
        else:
            gridList[row][col] = f"{bcolors.ITALIC}0{bcolors.reset}"
            return False


# CHECKING FUNCTIONS
# Scans rows for ship peices
def checkRow(row):
    if row:
        for char in row:
            if char == "=":
                return True
        return False
    else:
        return row

# Make sure the grid has ships in it
def checkGrid(gridList):
    # Handling
    if gridList:
        # Iterating each row
        for row in gridList:
            # If there's still pieces on the grid
            if checkRow(row):
                # Indicate the grid is still playable
                return True
        # Default to not playable & return False if there's no '=' pieces
        return False
    # For whatever reason the grid is empty
    else:
        return gridList

# sees if a ship is sunken based on battleship class ships list
def sinkedShip(shipsList, AI = True):
    # checking each ship
    for ship in shipsList:
        # if the ship is empty for AI on player
        if len(ship) == 1 and AI:
            shipsList.remove(ship) # take it out the ships list (which changes the length) 
            return True # indicate that a ship was sunken
        # for player on AI
        elif len(ship) == 0:
            shipsList.remove(ship) # remove from AI's ships list
            return True # indicates the ship was sunken
    
    # after all iteration and no empty list was found, a ship was not sunken
    return False


def calcStat(playerStats):
    # player data
    playername = playerStats[0]
    h = playerStats[1]
    d = playerStats[2]
    s = playerStats[3]
    p = playerStats[4]
# Hit ship     Sunk ship     Streak     Only 1 point for defending
    total = round(h + d + s + p, 1)
    return [playername, h, d, s, p, total]

# Sorts the players
def sortPlayers(list):
    # Thanks geeksforgeeks lol
    list.sort(key = lambda x: x[1])
    return list

# Add's extra spaces based on given size (for formatting before I learned how to use String format methods)
def addExtra(string, size):
        # Get the len of string with no spaces
        strlen = len(string)
        # subtract that length from size
        diff = size - strlen
        # Add that many spaces to end of string and return it
        return string + "-" * diff

# Will add previous spaces based on where you want a word to be and add filler spaces if it needs
# to get to a wordlength threshhold (serious algorithm just to find out I didn't need it :|)
def positionWord(index_f, index_i, word, limit):
    # leading spaces
    spaces = " " * (index_f - index_i)
    if limit > len(word):
        extraSpaces = limit - len(word)
    else:
        extraSpaces = 0
        # trailing spaces
    word = word + " " * extraSpaces
    return spaces + word