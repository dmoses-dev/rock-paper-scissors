import random
from random import choices

def get_choices():
    player = input("Enter a chioce(rock, paper, scissors): ")
    options = ['rock', 'paper', 'scissors']
    computer = random.choice(options)
    print("You chose " + player + " Computer chose " + computer)
    if player == computer:
        return "it's a tie"
    elif player == 'rock' and computer == 'paper':
        return "You lose. Paper covers rock"
    elif player == 'paper' and computer == 'rock':
        return "You win!. Paper covers rock"
    elif player == 'scissors' and computer == 'rock':
        return "You lose. Rock smashes scissors"
    elif player == 'rock' and computer == 'scissors':
        return "You win!. Rock smashes scissors"
    elif player == 'paper' and computer == 'scissors':
        return "You lose. Scissors cuts through paper"
    elif player == 'scissors' and computer == 'paper':
        return "You win!. Scissors cuts through paper"  
    else:
        return "Wrong input" 

result = get_choices()
print(result)   

