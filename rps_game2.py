from random import randint
print ("Let's play rock, paper, scissors!")
user = input("Choose 'rock', 'paper', or 'scissors':")

#else print ("Sorry, you must input either 'rock', 'paper', or 'scissors'")

crand = randint(0,2)
if crand == 0:
    computer = "rock"
    print ("Computer chooses rock")
elif crand == 1:
    computer = "paper"
    print ("Computer chooses paper")
elif crand == 2:
    computer = "scissors"
    print ("Computer chooses scissors")

if computer == user:
    print ("It's a tie!")

if computer == "rock" and user == "scissors":
    print ("The computer wins!")
if computer == "paper" and user == "rock":
    print ("The computer wins!")
if computer == "scissors" and user == "paper":
    print ("The computer wins!")

if computer == "rock" and user == "paper":
    print ("You win!")
if computer == "paper" and user == "scissors":
    print ("You win!")
if computer == "scissors" and user == "rock":
    print ("You win!")
