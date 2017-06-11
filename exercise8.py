WEAPONS = ["Rock", "Paper", "Scissors"]
score = [0,0]
isWinner = False

def convert_weapon(choice):
    if(choice == "1"):
        return WEAPONS[0]
    elif(choice == "2"):
        return WEAPONS[1]
    else:
        return WEAPONS[2]

def is_winner():
    if(score[0] >= 3):
        print(player1.upper() + " WON THE FIGHT!!!")
        return True
    elif(score[1] >= 3):
        print(player2.upper() + " WON THE FIGHT!!!")
        return True
    else:
        return False

def getWeapon(user):
    valid = False
    while not valid:
        weapon = str(input(user + ",\nPress 1 for Rock, 2 for Paper, 3 for Scissors: "))
        print("\n")
        if weapon == "1" or weapon == "2" or weapon == "3":
            valid = True
        else:
            print("Invalid Response.  Choose 1, 2, or 3\n")
    return weapon

def get_winner(player1_turn, player2_turn):
    player1_turn = int(player1_turn)
    player2_turn = int(player2_turn)
    if(player1_turn == player2_turn):
        return 0
    elif (player1_turn == 1):
        if player2_turn == 3:
            return 1
        else:
            return 2
    elif (player1_turn == 2):
        if player2_turn == 1:
            return 1
        else:
            return 2
    elif (player1_turn == 3):
        if player2_turn == 2:
            return 1
        else:
            return 2
    else:
        return -1

def updateScore(player):
    if player == 0:
        print("\nIt's a tie!")
        return
    elif player == 1:
        print(player1 + " won this round!")
        score[0] = score[0] + 1
        return
    elif player == 2:
        print(player2 + " won this round!")
        score[1] = score[1] + 1
        return
    else:
        print("There was an error")
        return

player1 = input("Enter first player's name: ").capitalize()
player2 = input("Enter second player's name: ").capitalize()
while(not isWinner):
    player1_turn = getWeapon(player1)
    player1_choice = convert_weapon(player1_turn)
    player2_turn = getWeapon(player2)
    player2_choice = convert_weapon(player2_turn)

    battleWinner = get_winner(player1_turn, player2_turn)
    updateScore(battleWinner)

    print("  " + player1 + " chose : " + player1_choice + "\n  " + player2 + " chose: " + player2_choice)
    print("\nScore Update:\n  " + player1 + " - " + str(score[0]) + " points\n  " + player2 + " - " + str(score[1]) + " points" +
    "\n***** END OF TURN *****\n")
    isWinner = is_winner()
