"""
Name: Brendon Purchase
Student Number: 119473576
"""

# !/usr/bin/python
# comments in Python, irrespective of verison
from game import App

"""
In this lab, I want you to write the code to call the Python Game
1   the game should ask how many players want to play?
    read input, convert to int, catch problems
2   the game will ask how many games you want (best out of)?
    read input, convert to int, make sure input is an odd number, \
    catch problems
#   '\' is used to spread the print out over multiple lines :)
3   the game asks for the name of each player and creates a \
    list or dictionary to store results
4   You must write the code.
"""

'''
#################################################
                    FUNCTIONS
#################################################
'''


def getIntegerInput(question):
    """
    get an number value as input from the user - return an integer
    """
    try:
        num = int(input(question))
    except:
        print("This is not a valid integer. Try again: ")
        num = getIntegerInput(question)

    return num


def getStringInput(question):
    '''
    get a string input from the user
    '''

    string = (input(question))
    return string


def getNumberPlayers():
    '''
    get the number of players
    '''
    players = getIntegerInput("How many players do you want? ")
    return players


def getNumberGames():
    '''
    get the number of games
    '''
    games = getIntegerInput("How many games do you want? ")
    return games


def oddNumberGame(numGamesInput):
    '''
    make sure the number of games input is an odd, positive number
    '''

    if numGamesInput % 2 == 0:
        print('Number is even. Try again. ')
        getNumberGames()
    return


def main():
    # OUR MAIN FUNCTION
    '''
    #################################################
            GET NUMBER OF USERS AND GAMES
    #################################################
    '''

    '''
    how many players?
    '''
    num_players = getNumberPlayers()
    print('Number of players: ', num_players)
    '''
    how many games (best out of)?
    '''
    numGames = getNumberGames()
    print('Number of games', numGames)
    '''
    #################################################
                GET NAMES OF USERS
    #################################################
    '''

    # lists
   # player_names = []
    player_values = []
  #  i = 0
   # while i < num_players:
      #  name = getStringInput('What is your name? ')
     #   player_names.append(name)
   #     i += 1

    '''
    create a list of initial player score values
    create a list of player names - asking the user for their names
    
    to call the game using lists uncomment these next 2 lines:
    '''
    #theApp = App()
   # theApp.on_execute_list(numGames, player_names, player_values)

    # dictionary
    player_dictionary = {}
    name = getStringInput('What is your name? ')
    player_dictionary[name] = 0

    '''
    create a dictionary
    create a dictionary of players names - asking the user for their names, as keys
    with the initial player score values, as values
    
    to call the game using a dictionary uncomment these next 2 lines:
    '''
    theApp = App()
    theApp.on_execute(numGames, player_dictionary)


'''
THIS IS HOW WE START THE PROGRAM
'''
if __name__ == '__main__':
    main()
