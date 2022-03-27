import random as rn
import numpy as np
from constants import WIDTH, ALPHABET, TAB, bcolors
from game_functions import found



class Battleship:
   
    def __init__(self, playername):
        # object data
        self.playername = playername
        self.grid = None
        self.ships = []
        self.ship_pieces = [3, 3, 3, 4, 4, 5, 5, 6]
        # makes grid
        self.createGrid()
        # makes grid with ships then tranposes (flips vertical)
        self.modifyGrid(self.grid, transpose=True)
        # adds horizontal ships
        self.modifyGrid(self.grid)


    # Self explainitory
    def getName(self):
        return self.playername

    # Makes a empty grid
    def createGrid(self):
        gridList = []
        temp = []
        for i in range(WIDTH):
            for j in range(WIDTH):
                temp += "O"
                if len(temp) == WIDTH:
                    gridList += [temp]
                    temp = []

        self.grid = gridList
    

    # Just makes ships will update to allow many sizes
    def createShip(self, size):
        return list(size * "=")
    
    # Sees if a ship will fit in a row
    def fits(self, ship, index, max_width, row):
        # Make sure ship does not exceed bounds
        if len(ship) + index <= max_width:
            # If there's no ship piece where the ship will be inserted, give it a go
            if "=" not in row[index - 1 if index > 0 else index: index + len(ship) + 1 if index + 
            len(ship) < 25 else index + len(ship)]:
                # Ship fits & piece not found in placement area
                return True
            # If the ship fits but there is a ship piece found
            return False
        # if the ship does not fit
        return False

    # modifies rows to have ship
    def insertShip(self, row):
        x = rn.randint(0, len(self.ship_pieces) - 1) # index of random ship
        size = self.ship_pieces.pop(x) # ship size popped
        # Ship sizes range from 3 to 6
        ship = self.createShip(size) # smallest ship to largest ship size in length
        # Index ranges from 0 to 25
        index = rn.randint(0, WIDTH)
        # Making sure the ship can be insrted into the row
        if self.fits(ship, index, WIDTH, row):
            for i in range(index, WIDTH):
                # Modding index
                row[i] = ship[0]
                # Cutting ship so loop ends
                ship.remove(ship[0])
                if len(ship) == 0:
                    return row
        # In the case that the ship does not fit redraw
        self.ship_pieces.insert(x, size)
        return self.insertShip(row)

    # Creates all the index where ships will be inserted
    def indexs(self):
        unq = []
        while len(unq) < 4: # this number is the number of ships times 2 
            n = rn.randint(0,25)
            # No duplicates
            if n not in unq:
                unq.append(n)
        # More readable
        unq.sort()
        return unq

    # Adds modified rows to grid list
    def modifyGrid(self, grid, transpose = False):
        inserts = self.indexs()
        for i, row in enumerate(grid):
            # If it's in a predefined location
            if i in inserts:
                row = self.insertShip(row)
                self.locate(i, row, transpose)
                
        # If the ships will become vertical
        if transpose:
            self.grid = np.array(grid).T.tolist()
        # Ships being horizontal
        else:
            self.grid = np.array(grid).tolist()

    def locate(self, index, row, transpose = False):
        locations = []
        # i is the column index
        for i, piece in enumerate(row):
            # If it's a ship piece add the row, and column index to locations
            if piece == "=":
                # Location of 1 ship
                if transpose:
                    # Vertical ships
                    location = (i, index)
                    # Only if this index is not already there
                    if found(location, self.ships):
                        # add to ship location list
                        locations.append(location)
                else:
                    # Horizontal ships
                    location = (index, i)
                    # Only if this index is not already there
                    if found(location, self.ships):
                        # add to ship location list
                        locations.append(location)

        # Adding the ships to the location of ships list for this gameboard
        self.ships.append(locations)

# Based on type shows row as is or row as opponent sees
    def convertRow(self, row):
        stringRow = ""
        # i is row num and char is the peice
        for i, char in enumerate(row):
            # dont show peices for AI
            if self.playername.lower() == "ai":
                # default colot
                color = bcolors.GREY
                # change ship peice to blank peice to mask
                if char == f"=":
                    # add to row str
                    stringRow += f"{color}O{bcolors.reset}"
                else:
                    # add normal blank
                    stringRow += f"{color}{char}{bcolors.reset}"
                # 25 rows made so return (index starts at 0)
                if i == WIDTH - 1:
                    return stringRow
                # spaces between
                else:
                    # space out
                    stringRow += " "
            # for displaying the player
            else:
                # default colors are green for player ship peices grey anything else
                color = bcolors.GREEN if char == "=" else bcolors.GREY
                stringRow += f"{color}{char}{bcolors.reset}"
                # 25 rows made so return (index starts at 0)
                if i == WIDTH - 1:
                    return stringRow
                # space inbetween
                else:
                    # space out
                    stringRow += " "

    # Allows the use of list() on Battleship object
    def __list__(self):
        return np.array(self.grid)

    def __str__(self):
        displayOutput = f"{TAB}    "
        # Adding column (A-Z)
        for letter in ALPHABET:
            # adding propper spaces
            if letter != "Z":
                displayOutput += letter + " "
            # if at Z add a new line
            else:
                displayOutput += letter + "\n"

        # Adding numeric rows with the grid spaces
        for i, row in  enumerate(self.grid):
            rowString = self.convertRow(row)
            # For spacing numbers 1-9 
            if i < 10:
                displayOutput += TAB + str(i) + "   " + rowString + "\n"
            # for numbers 10 - 25
            elif i < 25:
                displayOutput += TAB+ str(i) + "  " + rowString + "\n"
            # Not adding a newline when done printing the rows
            else:
                displayOutput += TAB + str(i) + "  " + rowString
                
        return displayOutput

