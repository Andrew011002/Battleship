import random as rn
import time

from miscellaneous import updateGrid, checkGrid, convertAlpha
from constants import TAB, DISPLAYWIDTH, SPACER, bcolors
from game_functions import sinkedShip, askPlayer, askAI, turnOrder, shipFinder
from display_functions import displayScore, play, display
from battleship_class import Battleship

                   
def game(saves = []):
    # If the game is being resumed after being saved
    if saves:
        display("GAME RESUMED FROM SAVE", color = bcolors.WHITE,border= bcolors.GREEN, style = bcolors.BOLD + bcolors.ITALIC)
        # Player & AI
        playerOne = saves[0][0]
        computerAI = saves[1][0]

        # Round
        count = saves[2][0] + 1
        # Scores for displayScore function
        scores = saves[2][1]
        # Boolean for flow of saves
        turn = saves[2][2]
        # To help indicate who hit who before the game was saved & exited
        hitFlag = saves[2][3]

        # For AI to know where to attack from a save
        AI = saves[2][4]
        streakPlayer = saves[0][1]
        streakAI = saves[1][1]
        # knowing the last choice
        last_AI_choice = saves[2][5]

        # scores from a game save and the game might terminate
        stats = [(playerOne.playername.lower(), scores[playerOne.playername.lower()][0][4]), 
        (computerAI.playername.lower(), scores[computerAI.playername.lower()][0][4])]
        
    else:    
        # setup pre-grame
        display("It is recommended that you play with your terminal on full screen to get the best playing experience", style="", center=True)
        time.sleep(5) # message on screen time
        display("Enjoy!", center=True, style="")
        time.sleep(2.5) # time before going into game flow
        # Generate the AI
        computerAI = Battleship("AI")
        while True:
            display("Enter a playername",style = "", center = True)
            userInput = input(f"{TAB}{''.center(DISPLAYWIDTH // 2)}")

            # If the input isn't empty and doesn't
            if userInput.strip():
                # making sure it can't be named AI to hide grid
                if userInput != "ai" and userInput != "AI" and userInput != "Ai" and userInput != "aI":
                    # Removing any spaces or special characters
                    player = ''.join(c for c in userInput if c.isalnum())
                    # Making everything lowercase
                    player = player.lower()
                    # Capitalizing first letter
                    player = player.capitalize()
                    # Create an Instance for the player
                    playerOne = Battleship(player)
                    break
                else:
                    display("CANT USE NAME: 'AI', TRY AGAIN!",color = bcolors.RED, center = True)
                # invalid input
            else:
                display("INVALID NAME, TRY AGAIN!",color = bcolors.RED, center = True)
        SPACER
        display("The Game is About to Begin!", style = bcolors.BOLD + bcolors.ITALIC, center = True)
        SPACER
        # Time before showing players
        time.sleep(3)
        display(f"Player 1 in this game is {playerOne.playername} and Player 2 is AI", style = "")
        SPACER
        # Time before being asked for magic number
        time.sleep(3)
        display(" Pick a number between 1 and 100. If you guess closer to my magic number you will go first otherwise the AI will go. If there is a tie there will be a tie breaker. Remeber to pick wiseley.", center=True, style = "")
        SPACER
        # Time before calling turnOrder()
        time.sleep(4.5)
        turn = turnOrder()
        SPACER
        # Time before grids will be generated
        time.sleep(3)
        display(f"Generating {playerOne.playername}'s grid & AI's grid. One moment please...", 
        style = bcolors.BOLD + bcolors.ITALIC)
        # Time before going into game
        time.sleep(5)
        display("Starting game!", color = bcolors.GREEN, style = bcolors.BOLD + bcolors.ITALIC, center = True)
        time.sleep(5)
        count = 0
        streakPlayer = 0
        streakAI = 0
        last_AI_choice = None
    # As long as there's peices on each playerboard, play on
    while checkGrid(computerAI.grid) == checkGrid(playerOne.grid):
        # game attributes
        hitPlayer = 0
        hitAI = 0
        protectedPlayer = 0
        protectedAI = 0
        destroyedPlayer = 0
        destroyedAI = 0
        display(f"ROUND {count + 1}", color = bcolors.GREEN, center = True)
        # Time after showing the round
        time.sleep(1.5)
        if count == 0:
            display(f"{playerOne.playername}'s grid", center = True)
        else:
            display(f"{playerOne.playername}'s Updated  grid", center = True)
        time.sleep(1.25)
        print(playerOne)
        print()
        # Time between showing or updating grids after a round
        time.sleep(1)
        if count == 0:
            display("AI grid", center = True)
            time.sleep(1)
        # updated AI grid
        else:
            display("Updated AI grid", center = True)
        # AI grid
        print(computerAI)
        print()
        time.sleep(1.75) # time before message below
        # Only display when first round
        if count == 0:
            display("AI: You cannot see my grid hahaha!", color = bcolors.RED, style = "")
            time.sleep(1.25)

        time.sleep(1)

        # player goes first
        if turn:
            PLAYER = askPlayer()
            SPACER
            # Time between asking players
            time.sleep(0.75)
            if count > 0:
                # ship hit
                if hitFlag:
                    # grab ship
                    ship = shipFinder(last_AI_choice, playerOne.ships)
                    AI = askAI(s = ship)
                # Runs as normal if not 
                else:
                    AI = askAI()
            # Runs as normal if not
            else:
                AI = askAI()
        # AI goes first
        else:
            # time.sleep(1.25)
            if count > 0:
                # ship hit
                if hitFlag:
                    ship = shipFinder(last_AI_choice, playerOne.ships)
                    AI = askAI(s = ship)
                # Runs as normal if not
                else:
                    AI = askAI()
            # Runs as normal if not
            else:
                AI = askAI()
            SPACER
            # Time between asking players
            time.sleep(1.25)
            PLAYER = askPlayer()
        # Time before seeing the results then seeing results (makes sense)
        time.sleep(1)
        # self explainatory
        last_AI_choice = (AI[1], convertAlpha(AI[0]))
        # Time before showing results of the round
        time.sleep(1)
        display("AI: Let's see how we both did this round.", color = bcolors.RED, style = "")
        SPACER
        time.sleep(1.5) # time before showing results
        # AI's impact on player
        if updateGrid(playerOne.grid, AI):
            # AI hitting ship points
            hitAI = 5
            display("AI: It appears I have hit you hahaha!", color = bcolors.RED, style = "")
            # Sucken ship condition for AI
            if sinkedShip(playerOne.ships):
                # AI destroying ship points
                destroyedAI = 9
                time.sleep(1.25)
                display("SHIP SUNKEN", style = bcolors.ITALIC + bcolors.BOLD, center = True)
                time.sleep(1.25)
                display("AI: I have sucken one of your ships!", color = bcolors.RED, style = "")

            streakAI += 1
            if streakAI == 2:
                time.sleep(1.25)
                display("AI: Two in a row! Let's go!", color = bcolors.RED, style = "")
            elif streakAI == 3:
                time.sleep(1.25)
                display("AI: It appears I'm on a role", color = bcolors.RED, style = "")
            elif 4 <= streakAI <= 6:
                time.sleep(1.25)
                display("AI: You cannot stop me!", color = bcolors.RED, style = "")
            elif streakAI > 8:
                time.sleep(1.25)
                display("AI: I am unstopplable", color = bcolors.RED, style = "")
            # AI hit player
            hitFlag = True
        # AI misses
        else:
            # player protecting points
            protectedPlayer = 1
            # no hit
            hitFlag = False
            display("AI: I have missed you this round but not for long...", color = bcolors.RED, style = "")
            # no streak
            streakAI = 0
        # Player's impact on AI
        if updateGrid(computerAI.grid, PLAYER):
            # Player hitting points 
            hitPlayer = 5
            SPACER
            display("AI: You have hit me!", color = bcolors.RED, style = "")
            # increase streak
            streakPlayer += 1
            # special comments if AI on streak
            if streakPlayer == 2:
                time.sleep(1.25)
                display("AI: Wow! Two in a row. I'll see if that lasts.", color = bcolors.RED, style = "")
            elif streakPlayer == 3:
                time.sleep(1.25)
                display("AI: You sure are lucky. This luck won't last long...", color = bcolors.RED, style = "")
            elif 4 <= streakPlayer <= 6:
                time.sleep(1.25)
                display("AI: You have to be cheating!", color = bcolors.RED, style = "")
                display("AI: There's no way you're this precise.", style = "", color = bcolors.RED)
            elif streakPlayer > 8:  
                time.sleep(1.25)
                display("AI: You're a cheat code.", color = bcolors.RED, style = "")
            # removes a hit ship from the AI ship list
            shipFinder((PLAYER[1], convertAlpha(PLAYER[0])), computerAI.ships)
            # time before sunken ship commments
            # Sucken shipn condition for player
            if sinkedShip(computerAI.ships, AI = False):
                # Player destroying ship points
                destroyedPlayer = 9
                time.sleep(1.25)
                display("SHIP SUNKEN", color = bcolors.WHITE, border = bcolors.OKGREY, style = bcolors.ITALIC, center = True)
                display("AI: You have sucken my ship :(", color = bcolors.RED, style = "",)
            # Time before seeing how player will do next round
            time.sleep(2)
            display("AI: Well played. Let's see how you do next round.", color = bcolors.RED, style = "")
        else:
            # AI Protecting points
            protectedAI = 1
            # no streak for player
            streakPlayer = 0
            time.sleep(2)
            display("AI: Looks like you missed your target hahaha. Better luck next round.", color = bcolors.RED, style = "")

        # Get players name, then if they hit, if they sunk a ship, their streak
        playerStats = [playerOne.playername, hitPlayer, destroyedPlayer, streakPlayer, protectedPlayer]
        AIStats = [computerAI.playername, hitAI, destroyedAI, streakAI, protectedAI]

        time.sleep(2)
        display("ROUND DATA", center = True)

        # Get the stats to add to the leaderboard
        # stats is a tuple of lists with each playername & their score (some other attributes)

        # If there's a save use the saved scores MIGHT NOT BE NEEDED because the same function is called
        if saves:
            # Changes sets memory to previous save and shows the scores
            stats = displayScore([playerStats, AIStats], [len(playerOne.ships), len(computerAI.ships)], memDict= scores)
        else:
            # Uses a blank memory
            stats = displayScore([playerStats, AIStats], [len(playerOne.ships), len(computerAI.ships)])            

        # see if the player wants to continue player
        save = play(stats)

        # if the player wants to save the game but quit
        if type(save) == dict:
            g = ([playerOne, streakPlayer], [computerAI, streakAI], [count, save, turn, hitFlag, AI, last_AI_choice], stats)
            # Returning stats to add to leaderboard & the game for the save
            return g

        # if the player wants to quit and not save data
        elif save == False:
            # clearing AI to have a new set of selections to make
            askAI(clear = True)
            # clearing player to allow new selections for game
            askPlayer(clear = True)
            # returning false indicate the game is done and progress not saved
            return False
        
        time.sleep(0.75)
        # Change the round using count
        count += 1
        
    # If the games finsihes    

    # Player scores if there is no save, scores are defined from saves above
   
    ps_1 = stats[0][1]
    ps_2 = stats[1][1]
    # Printing result
    # AI beating player
    if ps_2 > ps_1:
        display("YOU HAVE LOST TO THE AI",color = bcolors.RED, center = True)
        display("AI: BETTER LUCK NEXT TIME, GOOD GAME!", color = bcolors.RED, style = "", center = True)
    # Player beating AI
    elif ps_2 < ps_1:
        display("YOU HAVE BEATEN THE AI",color = bcolors.GREEN, center = True)
        display("AI: CONGRADULATIONS, YOU BESTED ME!", color = bcolors.RED, style = "" ,center = True)
    # Tie game
    else:
        display("YOU HAVE TIED WITH THE AI",color = bcolors.YELLOW, center = True)
        display("AI: GOOD GAME, LETS PLAY AGAIN!", color = bcolors.RED, style = "", center = True)

    # Updating the leaderboard and clearing memory
    displayScore(playerScores= None,ships = None, clear= True)
    askAI(clear = True)
    askPlayer(clear = True)
    # Returning stats for leaderboard
    return stats
    