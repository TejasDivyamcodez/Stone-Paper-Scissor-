from random import randint
game  = ["Rock", "Paper", "Scissors"]
computer = game[randint(0,2)]
playersPoint = 0
computersPoint = 0

goOn = True
while(goOn):
    player = input("Rock, Paper, Scissors {Type Finish to end} : \t")
    if(player == 'Finish'):
        goOn = False
    elif(player == computer):
        print("Tie!")
    elif(player == "Rock"):
        if(computer == "Paper"):
            print("You lose!", computer, "covers", player)
            computersPoint = computersPoint + 1
        else:
            print("You win!", player, "smashes", computer)
            playersPoint = playersPoint + 1
    elif(player == "Paper"):
        if(computer == "Scissors"):
            print("You lose!", computer, "cut", player)
            computersPoint = computersPoint + 1
        else:
            print("You win!", player, "covers", computer)
            playersPoint = playersPoint + 1
    elif(player == "Scissors"):
        if(computer == "Rock"):
            print("You lose...", computer, "smashes", player)
            computersPoint = computersPoint + 1
        else:
            print("You win!", player, "cut", computer)
            playersPoint = playersPoint + 1
    else:
        print("That's not a valid play. Check your spelling!")
    computer = game[randint(0,2)]
    print('********Next Turn********')

print("********Final Points********")
print("Player: ", playersPoint)
print("Computer: ", computersPoint)
