import sys
from game_body import game
from display_functions import menu, displayLeaderboard, display
from constants import CREDITS_1, CREDITS_2, bcolors


def main():
    gs = False
    lbs = []
    mem = []
    # Main looper
    while True:
        # If there's a save change the display format
        # Format is normal if there's no save
        ui = menu(save = True) if gs else menu()

        # Play game
        if ui == 1:
            # Run game from memory or run new game
            g = game(saves = mem[-1]) if mem else game()
            # Based on game results add or clear game memory
            mem.append(g) if type(g) is tuple else mem.clear()
            gs = True if type(g) is tuple else False # indicate there's a save
            # Quit with save
            if type(g) is tuple:
                # Leaderboard scores               
                lbs = g[-1]
            # Game ends with victor
            elif type(g) is list:
                # Leaderboard scores
                lbs = g

        # Asked for leaderboard
        elif ui == 2:
            # Shows leaderboard
            displayLeaderboard(playerList = lbs)
        
        # Quit
        elif ui == 3:
            # Exits program
            display("GAME QUIT", color=bcolors.RED, center=True)
            sys.exit()
        
        # Credits
        elif ui == 4:
            display("CREDITS", color = bcolors.GREEN, center = True)
            display(CREDITS_1, color = bcolors.WHITE, border = bcolors.GREY, style= bcolors.BOLD + bcolors.ITALIC, center= True)
            display(CREDITS_2, color = bcolors.WHITE, border = bcolors.GREY, style= bcolors.BOLD + bcolors.ITALIC, center= True)



        

if __name__ == '__main__':
    main()