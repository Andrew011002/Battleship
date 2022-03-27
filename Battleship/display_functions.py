import time

from constants import TAB, SPACERTOP, DISPLAYWIDTH, DIVIDER, MAX_LABEL_SIZE, bcolors, WARNING, POSITIVE, SPACE
from miscellaneous import *

# For displaying simple messages with formatting
def display(text, color = bcolors.WHITE, border = bcolors.GREY, style = bcolors.BOLD, center = False, prnt = True):
    # Removing leading and trailing spaces
    text = text.strip()
    # Counts charaters to check for new line
    chars = 0
    tmp = ""
    output = f"{TAB}{border}|{SPACERTOP}|\n"
    # If text is centered
    if center:
        # Adding letters & symbols to tmp
        for char in text:
            tmp += char
            chars += 1
            # Adding text to output if it's on a new word and exceeds line limit
            if chars >= 40 and char == " ":
                output += f"{TAB}|{color}{style}{tmp.center(DISPLAYWIDTH)}{bcolors.reset}{border}|\n"
                # Reseting counter and tmp
                tmp = ""
                chars = 0
        # Adding any leftover text
        output += f"{TAB}|{color}{style}{tmp.center(DISPLAYWIDTH)}{bcolors.reset}{border}|\n"
    # Text defaults to left align
    else:
        # Adding letters & symbols to tmp
        for char in text:
            tmp += char
            chars += 1
            # Adding text to output if it's on a new word and exceeds line limit
            if chars >= 40 and char == " ":
                output += f"{TAB}| {color}{style}{tmp.ljust(DISPLAYWIDTH - 1)}{bcolors.reset}{border}|\n"
                # Reseting counter and tmp
                tmp = ""
                chars = 0
        # Adding any leftover text
        output += f"{TAB}| {color}{style}{tmp.ljust(DISPLAYWIDTH - 1)}{bcolors.reset}{border}|\n"
    # Adding bar
    output += f"{border}{TAB}|{SPACERTOP}|\n{bcolors.reset}"
    # prints output by default
    if prnt:
        print(output)
    # If it's not defaulted then the function returns the output
    else:
        return output
# Displays a menu and gives back an input if valid
def menu(save = False):
    # Situational printing
    if save:
        gameType = ' RESUME GAME'
    else:
        gameType = ' NEW GAME'
    # All of the options
    # Special options based on state of game
    m = f"{TAB}{bcolors.GREY}|{SPACERTOP}|\n"
    m += f"{TAB}|{bcolors.RED}{bcolors.BOLD}{'WELCOME TO BATTLESHIP!'.center(DISPLAYWIDTH)}{bcolors.reset}{bcolors.GREY}|\n"
    m += f"{TAB}|{SPACERTOP}|\n"
    line_1 = f"{'[1]'.ljust(DISPLAYWIDTH // 3)}{gameType.center(DISPLAYWIDTH // 3)}"
    m += f"{TAB}|{bcolors.WHITE}{bcolors.BOLD}{line_1}{getExtra(line_1)}{bcolors.reset}{bcolors.GREY}|\n{TAB}|{DIVIDER}|\n"
    line_2 = f"{'[2]'.ljust(DISPLAYWIDTH // 3)}{'  LEADERBOARD'.center(DISPLAYWIDTH // 3)}"
    m += f"{TAB}|{bcolors.WHITE}{bcolors.BOLD}{line_2}{getExtra(line_2)}{bcolors.reset}{bcolors.GREY}|\n{TAB}|{DIVIDER}|\n"
    line_3 = f"{'[3]'.ljust(DISPLAYWIDTH // 3)}{' QUIT'.center(DISPLAYWIDTH // 3)}"
    m += f"{TAB}|{bcolors.WHITE}{bcolors.BOLD}{line_3}{getExtra(line_3)}{bcolors.reset}{bcolors.GREY}|\n{TAB}|{DIVIDER}|\n"
    line_4 = f"{'[4]'.ljust(DISPLAYWIDTH // 3)}{' CREDITS'.center(DISPLAYWIDTH // 3)}"
    m += f"{TAB}|{bcolors.WHITE}{bcolors.BOLD}{line_4}{getExtra(line_4)}{bcolors.reset}{bcolors.GREY}|\n{TAB}|{DIVIDER}|\n{TAB}|{SPACERTOP}|"

    # Input
    userInput = input(f"{m}\n{TAB}{''.center(DISPLAYWIDTH // 2)}{bcolors.reset}").strip()
    # Only allowing numbers to be passed
    if userInput.isdigit():
        userInput = int(userInput)
        # Making sure it's in a selectedable range of options
        if 1 <= userInput  <= 4:
            return userInput
        # Handling invalid inputs
        else:
            display("INVALID INPUT, TRY AGAIN!",color = bcolors.RED, center = True)            
            time.sleep(1)
            return menu()
    # Handling invalid inputs
    display("INVALID INPUT, TRY AGAIN!",color = bcolors.RED, center = True)            
    time.sleep(1)
    return menu()


# Pauses the game and displays options that player can make
def play(scores):
    # continue menu
    playString = f"{display('Continue to next round?', center= True, prnt= False)}"
    question = f"{TAB}{bcolors.GREY}|{bcolors.WHITE}{'Press enter to continue'.center(DISPLAYWIDTH)}\
{bcolors.GREY}|\n{TAB}|{bcolors.WHITE}{'Press any other button to pause'.center(DISPLAYWIDTH)}{bcolors.GREY}\
|\n{TAB}|{SPACERTOP}|\n{TAB}{''.center(DISPLAYWIDTH // 2)}{bcolors.reset}"
    playString += question
    userInput = input(playString)
    if userInput != "":
        statement = pause(scores)
        # Making sure it's true because "s" is considered True but we don't want it to print when the game is saved then exited
        if statement == True:
           display("PLAY ON!",color = bcolors.GREEN, center = True)
           time.sleep(1)
        # If the player decides to quit & save
        elif statement == "s": 
            # Not clearing memory but indicating to display Scores there's save
            return displayScore(scores, save = True)
        # If players decide to quit & not save (dafaults to this)
        else:
            # Clearing the memory for a new game
            displayScore(scores, clear = True)

            # Indicate no save by False
            return False

# Ask players if they want to save their game, should ask if they are sure they want to quit
def end():
    quitMenu = f"{TAB}{bcolors.GREY}|{SPACERTOP}|\n"
    title = f"{TAB}|{bcolors.WHITE}{'Would you like'.center(DISPLAYWIDTH)}{bcolors.GREY}|\
\n{TAB}|{bcolors.WHITE}{'to save your current'.center(DISPLAYWIDTH)}{bcolors.GREY}\
|\n{TAB}|{bcolors.WHITE}{'game in memory?'.center(DISPLAYWIDTH)}{bcolors.GREY}|\n{bcolors.reset}"
    quitMenu += f"{title}{TAB}{bcolors.GREY}|{SPACERTOP}|{bcolors.reset}"
    # Add yes or no selection
    yes = f"{POSITIVE}{bcolors.BOLD}{f'{SPACE}[1] YES'.center(DISPLAYWIDTH // 2)}{bcolors.reset}"
    no = f"{WARNING}{bcolors.BOLD}{'[0] NO'.center(DISPLAYWIDTH // 3)}{bcolors.reset}{bcolors.GREY}"
    line = yes + no
    quitMenu += f"\n{TAB}{bcolors.GREY}|{line}{getExtra(line)}{SPACE}|\n{TAB}|{SPACERTOP}|{bcolors.reset}"
    print(quitMenu)
    userInput = input(f"{TAB}{''.center(DISPLAYWIDTH // 2)}").strip()
    # Verifying input is a number and is 1 or 0
    if userInput.isdigit() and (userInput == '1' or userInput == '0'):
        # Player selecting quit & to save the game
        if userInput == '1':
            display("Game Progress Saved!", color = bcolors.GREEN, style = bcolors.BOLD + bcolors.ITALIC, center= True)
            time.sleep(1)
            # Returning s to indicate to pause to indicate to play to save
            return 's'
        # Player selecting to quit & not save the game
        elif userInput == '0': 
            # Player selecting to quit without saving
            display("Game Progress Terminated!", color = bcolors.RED, style = bcolors.BOLD + bcolors.ITALIC, center= True)
            time.sleep(1)
            # Retrunign False to indicate to pause to indicate to save that user wants to quit without save
            return False
    else:
        # Bad inputs
        display("INVALID INPUT, TRY AGAIN!",color = bcolors.RED, center = True)            
        time.sleep(1)
        return end()

# Diplays pause menu with option like quitting resumingm & leaderboard
def pause(llist):
    # MENU 
    pauseMenu = display("PAUSED", color= bcolors.RED, center= True, prnt=False)
    DIVIDER = "-" * DISPLAYWIDTH
    resumeAtt = f" [1]".ljust(DISPLAYWIDTH // 3) + f"  RESUME".center(DISPLAYWIDTH // 3)
    resumeLine = resumeAtt + getExtra(resumeAtt)
    leaderboardAtts = f" [2]".ljust(DISPLAYWIDTH // 3) + f"  LEADERBOARD".center(DISPLAYWIDTH // 3)
    leaderboardLine = leaderboardAtts + getExtra(leaderboardAtts)
    quitAtt = f" [3]".ljust(DISPLAYWIDTH // 3) + f"  QUIT".center(DISPLAYWIDTH // 3)
    quitLine = quitAtt + getExtra(quitAtt)
    pauseMenu += f"{bcolors.GREY}{TAB}|{bcolors.WHITE}{bcolors.BOLD}{resumeLine}{bcolors.reset}{bcolors.GREY}|\n\
{TAB}|{DIVIDER}|\n{TAB}|{bcolors.WHITE}{bcolors.BOLD}{leaderboardLine}{bcolors.reset}{bcolors.GREY}|\n\
{TAB}|{DIVIDER}|\n{TAB}|{bcolors.WHITE}{bcolors.BOLD}{quitLine}{bcolors.reset}{bcolors.GREY}|\n{TAB}|{SPACERTOP}|"
    print(pauseMenu)
    enterLine = f"Press 1 to continue".center(DISPLAYWIDTH)
    showBoard = f"Press 2 to view Leaderboard".center(DISPLAYWIDTH)
    quitLine = f"Press 3 to quit".center(DISPLAYWIDTH)
    p = (input(f"{bcolors.GREY}{TAB}|{bcolors.WHITE}{enterLine}{bcolors.GREY}|\n\
{TAB}|{bcolors.WHITE}{showBoard}{bcolors.GREY}|\n{TAB}|{bcolors.WHITE}{quitLine}{bcolors.GREY}|\n\
{TAB}|{SPACERTOP}|\n{bcolors.reset}{TAB}{''.center(DISPLAYWIDTH // 2)}")).strip()
    # Handling inputs (making sure the input is a number)
    if p.isdigit():
        p = int(p)
        # Resuming game
        if p == 1:
            return True
        # Show the leaderboard & then return back to pause
        elif p == 2:
            displayLeaderboard(llist)
            return pause(llist)
        # Ask if users would like to save their game
        elif p == 3:

            # Warning
            yes = f"{WARNING}{bcolors.BOLD}{f'{SPACE}[1] YES'.center(DISPLAYWIDTH // 2)}"
            no = f"{POSITIVE}{'[0] NO'.center(DISPLAYWIDTH // 3)}{bcolors.reset}{bcolors.GREY}"
            line = f"{yes}{no}"
            base = display("Are you sure you want to quit?", center= True, prnt= False)
            base += f"{TAB}{bcolors.GREY}|{SPACERTOP}|\n{TAB}|{line}{getExtra(line)}{SPACE}|\n{TAB}|{SPACERTOP}|{bcolors.reset}"

            # Loop for quitting
            while True:
                userInput = input(f"{base}\n{TAB}{''.center(DISPLAYWIDTH // 2)}").strip()
                # Making sure the user input is a number & is 1 or 0
                if userInput.isdigit() and (userInput == "1" or userInput == "0"):
                    userInput = int(userInput)
                    # User wanting to quit
                    if userInput:
                        return end()
                    # User not wanting to quit after selecting quit
                    elif not userInput:
                        return pause(llist)
                # Invalid inputs
                else:
                    display("INVALID INPUT, TRY AGAIN!",color = bcolors.RED, center = True)            
                    time.sleep(1)
                    continue
        # Invalid inputs
        else:
            display("INVALID INPUT, TRY AGAIN!",color = bcolors.RED, center = True)            
            time.sleep(1)
            return pause(llist)
    # Invalid inputs
    else:
        display("INVALID INPUT, TRY AGAIN!",color = bcolors.RED, center = True)            
        time.sleep(1)
        return pause(llist)

# takes player scores and computes the score, also stores the score to be retrived in memory
# Computes scores by (playername, hit, sunk, streak, protected)
def displayScore(playerScores = [], ships = [], memDict = {}, save = False, clear = False):
    # If there's a save give back the stats
    if save:
        return memDict
    
    # If the user quits & doesn't save their game
    if clear:
        memDict.clear()
        return None

    # Initialize dictionary
    if not memDict:
        # Add players to dictionary
        for player in playerScores:
            # Player stats with total
            playerAtts = calcStat(player)
            # Players Name
            playerKey = playerAtts[0].lower()
            # Playername is dictionary key & player's attributes
            memDict.update({playerKey: [playerAtts[1:] + ["NA", "NA", "NA", "NA", 0]]})

    # If there's already players stored in the dictionary update their data
    else:
        # Compare keys to...
        for key in memDict:
            # scan players
            for player in playerScores:
                # check if the the key matches the normalized playername
                playerKey = player[0].lower()
                if key == playerKey:
                    # Update the value
                    lastAtts = memDict[key][-1]
                    # Total score
                    playerAtts = calcStat(player)[1:] # calculates score based on player stats
                    playerAtts[4] = round(playerAtts[4] + lastAtts[4], 2)
                    # Adding each previous stat to player stats
                    for i in range(5):
                        playerAtts.append(lastAtts[i])
                    # Adding player attributes with last attributes to memDict
                    memDict[key].append(playerAtts)
                    # Getting rid of the last attributes (stand alone) from memDict
                    memDict[key].remove(lastAtts)
        

    # Showing parts to scoreboard
    scoreboard = ""
    # Adding scoreboard header
    bar = f"{TAB}{bcolors.GREY}|{SPACERTOP}|\n"
    # scoreboard += bar
    scoreboard += bar
    # Scoreboard header end


    p_ships = ships[0]
    ai_ships = ships[1]
    for player in memDict:
        # Playername
        name = player.upper()
        # Most recent stat
        stats = memDict[player][-1]
        current = stats[:5]
        last = stats[5:]
        # Overview start
        leftPos = f"  PLAYER: {name}".ljust(50 // 3)
        centerPos = "OVERVIEW".center(50 // 3)
        rightPos = "PREVIOUS".rjust(50 // 4)
        overview = f"{leftPos}{centerPos}{rightPos}"
        scoreboard += f"{TAB}|{bcolors.WHITE}{bcolors.BOLD}{overview}{getExtra(overview)}{bcolors.reset}{bcolors.GREY}|\n"
        scoreboard += bar
        # Building scoreboard based on size of data attributes
        # The labels will hold a tuple, one for current data & one for previous data
        labels = ["hit", "sunk", "streak", "protected"]
        prevTag = "prev"
        for i, stat in enumerate(current):
            if i == 4:
                break
            # Create the left white space
            label = addExtra(labels[i], MAX_LABEL_SIZE)
            whitespace = " ".ljust(DISPLAYWIDTH // 3) if i != 0 else f" Ships: {p_ships if name.upper() != 'AI' else ai_ships}".ljust(DISPLAYWIDTH // 3)
            # Center position will be the the label formatted with the stat
            centerPos = f"{label}: {stat}".center(DISPLAYWIDTH // 3)
            # Right position will be the previous stat if possible
            rightPos = f"{prevTag}: {last[i]}".rjust(50 // 4)
            # Create the line without extra spaces
            line = f"{whitespace}{centerPos}{rightPos}"
            totalLine = f"{line}{getExtra(line)}"
            # Add line to scoreboard with right padding
            scoreboard += f"{TAB}{bcolors.GREY}|{bcolors.WHITE}{totalLine}{bcolors.GREY}|\n"
        # Create centerbar for total and rightbar for total
        # Centerbar
        centerbar = ("-" * 12).center(50 // 3)
        # Right bar
        rightbar = ("-" * 8).rjust(50 // 4)
        # Create line then add line to scoreboard
        line = f"{whitespace}{centerbar}{rightbar}"
        scoreboard += f"{TAB}|{line}{getExtra(line)}|\n"

        totalWord = f"total: {current[-1]}"
        # First part of line, need to add space and word
        centerPos = positionWord(18, 0, totalWord, 12)
        prevWord = f"{prevTag}: {last[-1]}"
        rightPos = positionWord(36, 30, prevWord, 0)
        line = f"{centerPos}{rightPos}"
        scoreboard += f"{TAB}|{bcolors.WHITE}{bcolors.BOLD}{line}{getExtra(line)}{bcolors.reset}{bcolors.GREY}|\n{bcolors.reset}"
        # Add bar to seperate players
        scoreboard += bar

    # Playernames
    player_name_01 = playerScores[0][0].lower()
    player_name_02 = playerScores[1][0].lower()
    # Data is the playername & their total
    data_01 = (player_name_01, memDict[player_name_01][0][4])
    data_02 = (player_name_02, memDict[player_name_02][0][4])
    # Display the score
    print(scoreboard)

    # List of player stats
    return [data_01, data_02]


# quick bug fix for this one function
fix = display

def displayLeaderboard(playerList = [], memory = {}, display = True):  
    # Only creating & updating dictionary if there's players
    if playerList:
    # Creating dictionary
        for player in playerList:
            # player data
            playername = player[0]
            playerscore = player[1]
            # Add player if not in memory
            if playername not in memory:
                memory.update({playername: playerscore})
                # Seeing if the score should be updated or not
            else:
                # If their new score is bigger than their previous and they're in the memory...
                if memory.get(playername) < playerscore:
                    # Updating to new score
                    memory.update({playername: playerscore})
        # converts dictionary to list
        def dictConvert(dictionary):
            dictList = []
            # Add get the key then the key value
            if dictionary:
                # iterate players
                for key in dictionary:
                    # player, stat form
                    playerStat = (key,dictionary[key])
                    # add player if not in dictionary list already
                    if playerStat not in dictList:
                        dictList.append(playerStat)
                return dictList
            # False dictionary
            return {}
        # Making the playerlist the dictionary so duplicates don't get printed
        playerList = sortPlayers(dictConvert(memory))[::-1]
    leaderboard = ""
    # For filling the leftover space
    bar = f"{TAB}{bcolors.GREY}|{SPACERTOP}|\n"
    leaderboard += bar
    leaderboard += f"{TAB}|{bcolors.WHITE}{bcolors.BOLD}{'LEADERBOARD'.center(DISPLAYWIDTH)}{bcolors.reset}{bcolors.GREY}|\n"
    # Leaderboard header start
    PLAYER = "  PLAYER".ljust(DISPLAYWIDTH // 3)
    SCORE = "SCORE".rjust(DISPLAYWIDTH // 3)
    LEADERBOARD = " POSITION".center(DISPLAYWIDTH // 3)
    # Title
    title = PLAYER + LEADERBOARD + SCORE
    leaderboard += bar
    leaderboard += f"{TAB}|{bcolors.WHITE}{bcolors.BOLD}{title}{getExtra(title)}{bcolors.reset}{bcolors.GREY}|\n"
    leaderboard += bar
    # Leaderboard header end
    
    # Begin adding players
    if playerList:
        for i, player in enumerate(playerList):
            # Add the playername then the score
            playername = f"   {player[0].upper()}".ljust(DISPLAYWIDTH // 3)
            playerscore = f"{player[1]}".rjust(DISPLAYWIDTH // 3)
            # Position the ranking
            position = f"{i + 1}".center(DISPLAYWIDTH // 3)
            playerline = playername + position + playerscore
            # Add the playername then the score
            leaderboard += f"{TAB}|{bcolors.GREEN}{playerline}{getExtra(playerline)}{bcolors.GREY}|\n"
            leaderboard += bar
        # End of adding players add empty slots for look
    # Empty slot start
    for i in range(2):
        emptyslot = f"{TAB}|{bcolors.WHITE}{'EMPTYSLOT'.center(DISPLAYWIDTH)}{bcolors.GREY}|\n{bar}"
        leaderboard += emptyslot
    # Empty slot end
    if display:
        print(leaderboard + bcolors.reset)
        fix("Press Enter to close", center = True)
        input(f"{TAB}{''.center(DISPLAYWIDTH // 2)}")
