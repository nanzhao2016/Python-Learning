# programme for achiving the game "scissors, paper, rock, lizard and spock" with python2

import random

# generate a move
def generateMove ():
    move=["scissors", "paper", "rock", "lizard", "spock"]
    return random.choice(move)

# match a move to a number 
def matching (aMove):
    if aMove == "scissor":
        number = 5
    elif aMove == "paper":
        number = 4
    elif aMove == "rock":
        number = 3
    elif aMove == "lizard":
        number = 2
    elif aMove == "spock":
        number = 1
    else:
        number = 0

    return number

# compare between two moves by using modulo 5
def comparing (number1, number2):
    if number1 == 0 | number2 == 0:
        return "Programme Error!"
    else:
        if (number1-number2)%5 == 1:
            return number1
        elif(number1-number2)%5 == 2:
            return number2
        elif (number1-number2)%5 == 3:
            return number1
        elif(number1-number2)%5 == 4:
            return number2
        elif (number1-number2)%5 == 0:
            return 0

# the general function to decide who to win
def whoWin(player1, player2):
    print "Player1 :", player1
    print "Player2 :", player2
    print
    number1 = matching(player1)
    number2 = matching(player2)    
    who = comparing (number1, number2)
    if who == "Programme Error!":
        print "***************************************"
        print "* There is an error in the programme. *"
        print "***************************************"
    elif who == number1:
        print "*****************"
        print "* Player1 wins! *"
        print "*****************"
    elif who == number2:
        print "*****************"
        print "* Player2 wins! *"
        print "*****************"
    else:
        print "*****************"
        print "* Equal!        *"
        print "*****************"    
    

# start the game with two players
player1 = generateMove()
player2 = generateMove()
whoWin(player1, player2)
