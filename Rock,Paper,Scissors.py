import random
import sys

def startMenu(a,b): 
    while True:
        try:
            choice = input("Please select (r)ock, (p)aper, or (s)cissors: ")
            if choice == "r":
                user = "rock"
                break
            elif choice == "p":
                user = "paper"
                break
            elif choice == "s":
                user = "scissors"
                break
        except ValueError:
            continue
    dice = random.randint(0,2)
    print(dice)
    if dice == 0:
#computer chose rock
        comp = "rock"
    elif dice == 1:
#computer chose paper
        comp = "paper"
    elif dice == 2:
#computer chose scissors
        comp = "scissors"
    print("You chose :", user)
    print("The computer chose: ", comp)
    rules(user,comp,a,b)
    
def rules(x,y,count,compCount):
#if comp and user choose the same thing
    if x == y:
        count += 1
        compCount += 1
#paper beats rock
    elif x == "rock" and y == "paper":
        compCount += 1
    elif x == "paper" and y == "rock":
        count += 1
#rock beats scissors
    elif x == "rock" and y == "scissors":
        count += 1
    elif x == "scissors" and y == "rock": 
        compCount += 1
#scissors beats paper
    elif x == "scissors" and y == "paper":
        count += 1
    elif x == "paper" and y == "scissors":
        compCount += 1
    print("User score: ", count)
    print("Computer score: ", compCount)
    while True:
        try:
            restart = input("Would you like to play again? (y)es or (n)o: ")
            if restart == "y":    
                startMenu(count,compCount)
            elif restart == "n":
                sys.exit(0)
            else:
                print("please enter y or n")
            continue
        except ValueError:
            print("please enter y or n")
            continue
    return
tally = 0
comptally = 0
startMenu(tally,comptally)
