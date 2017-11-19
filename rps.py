import random

player = raw_input("Rock (r), paper (p) or scissors (s)? ")
while player != 'r' and player != 'p' and player != 's':
    player = raw_input("Please choose from rock (r), paper (p) or scissors (s): ")

player_choices = {'r':'rock', 'p': 'paper', 's': 'scissors'}
choices = {'rock': 1, 'paper': 2, 'scissors': 3}
computer = random.randint(1,3)
for key, value in choices.iteritems():
    if computer == value:
        computer = key
print "You chose " + player_choices[player] + " and I chose " + computer + "."

if player == 'r':
    if computer == 'rock':
        result = "It's a draw!"
    elif computer == 'paper':
        result = "I win!!"
    else:
        result  "You win!!"

if player == 'p':
    if computer == 'paper':
        result = "It's a draw!"
    elif computer == 'scissors':
        result = "I win!!"
    else:
        result = "You win!!"

if player == 's':
    if computer == 'scissors':
        result = "It's a draw!"
    elif computer == 'rock':
        result = "I win!!"
    else:
        result = "You win!!"

game = [player, computer, result]
