#--------------------------------------------------------------------------------------------------------------
# MODULES
#--------------------------------------------------------------------------------------------------------------
import random


#--------------------------------------------------------------------------------------------------------------
# FUNCTIONS
#--------------------------------------------------------------------------------------------------------------
def askOption(_inputMsg, _errorMsg, _listOfOptions):
    option = input(_inputMsg)

    option = option.upper()

    if (option not in _listOfOptions or option.isdigit()) and option != "E":
        print(_errorMsg)
        option = input(_inputMsg)
    return option

def endGame(_option, _opponentOption):
    if _option == "R" and _opponentOption == "S":
        win = True
    elif _option == "P" and _opponentOption == "R":
        win = True
    elif _option == "S" and _opponentOption == "P":
        win = True
    elif _option == _opponentOption:
        win = "Tie"
    else:
        win = False
    
    if win == True:
        print("Congrats you win :)")
    elif win == "Tie":
        print("So near but it is a tie")
    else:
        print("You lose :(")
    
    return win

def gameTracking(_win, counters):
    if _win == True:
        counters['wins'] += 1
    elif _win == False:
        counters['loses'] += 1

    print("RESULTS:")
    print(f"\tWINS\t|\tLOSES\n\t{counters['wins']}\t|\t{counters['loses']}")

def game():
    listOfOptions = ["R", "P", "S"]
    counters = {'wins': 0, 'loses': 0}

    inputMsg = "Choose your option ROCK(R)/PAPERS(P)/SCISSORS(S)/EXIT(E): "
    errorMsg = "Invalid option! Remember your options are only R/P/S"

    while True:
        option = askOption(inputMsg, errorMsg, listOfOptions)
        if option == "E":
            print("I hope to see you again soon")
            break

        opponentOption = random.choice(listOfOptions)
        print(f"Opponent option: {opponentOption}")

        win = endGame(option, opponentOption)

        gameTracking(win, counters)


    
def rules():
    print()
    print("----------------------------------------------------")
    print("RULES OF ROCK, PAPER, SCISSORS GAME")
    print("----------------------------------------------------")
    print()
    print("----------------------------------------------------")
    print("· The objective of the game is to choose between Rock (R), Paper (P), or Scissors (S) and try to beat the opponent.")
    print("· Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.")
    print("----------------------------------------------------")
    print()
    print("----------------------------------------------------")
    print("· HOW TO PLAY:")
    print("   - At each turn, you will choose one option: Rock (R), Paper (P), or Scissors (S).")
    print("   - The opponent will also randomly choose one of these three options.")
    print("   - The game will determine if you win, lose, or tie based on the choices.")
    print("----------------------------------------------------")
    print()
    print("----------------------------------------------------")
    print("· ENDING THE GAME:")
    print("   - The game ends after each round with a result of either win or loss.")    
    print("   - To exit the game you have to choose the option E(exit).")
    print("----------------------------------------------------")
    print()
    print("----------------------------------------------------")
    print("Good luck! Let the game begin.")
    print("----------------------------------------------------")


#--------------------------------------------------------------------------------------------------------------
# MENU
#--------------------------------------------------------------------------------------------------------------
while True:
    while True:
        try:
            print()
            print("-------------------------------------------")
            print("SYSTEM MENU")
            print("-------------------------------------------")
            print("[1] Play")
            print("[2] Rules")
            print("-------------------------------------------")
            print("[0] Exit")
            print("-------------------------------------------")
            print()
            menuOption = input("Choose an option: ")
            if menuOption in ["0","1","2"]:
                break
            else:
                input("Invalid option. Press ENTER to select again.")
        except ValueError:
            input("Invalid option. Press ENTER to select again.")

    if menuOption == "0":
        exit()

    elif menuOption == "1":  
       game()
        
    elif menuOption == "2":   
        rules()
    print()
    input("Press ENTER to return to the menu.")