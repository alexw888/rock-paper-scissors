from random import randint

cscore = 0
uscore = 0

while cscore < 5 and uscore < 5:
    def clear():
        print(" \n"*17)

    clear()

    print ("Let's play rock, paper, scissors!")
    user = input("Choose 'rock', 'paper', or 'scissors' or 'q' to quit: ")
    if user not in{"rock", "paper", "scissors", "q"}:
        print("\tNot a valid input!")
        continue
    elif user == "q":
        print("\tGoodbye")
        break

    crand = randint(0,2)
    if crand == 0:
        computer = "rock"
        print ("\tComputer chooses rock")
    elif crand == 1:
        computer = "paper"
        print ("\tComputer chooses paper")
    elif crand == 2:
        computer = "scissors"
        print ("\tComputer chooses scissors")

    if computer == user:
        print ("\tIt's a tie!")

    if computer == "rock" and user == "scissors":
        print ("\tThe computer wins!")
        cscore = cscore + 1
    if computer == "paper" and user == "rock":
        print ("\tThe computer wins!")
        cscore = cscore + 1
    if computer == "scissors" and user == "paper":
        print ("\tThe computer wins!")
        cscore = cscore + 1

    if computer == "rock" and user == "paper":
        print ("\tYou win!")
        uscore = uscore + 1
    if computer == "paper" and user == "scissors":
        print ("\tYou win!")
        uscore = uscore + 1
    if computer == "scissors" and user == "rock":
        print ("\tYou win!")
        uscore = uscore + 1

    print("Computer score is", cscore, "User score is", uscore)
    if uscore == 5:
        print("Good job!  You won the tournament!")
        clear()
    elif cscore == 5:
        print("Sorry, the computer outplayed ya!")
        clear()
     
