from flask import Flask, render_template, request
import random

app = Flask("MyApp")

def rockPaperScissors(player_input):
    choices = {'rock': 1, 'paper': 2, 'scissors': 3}
    computer = random.randint(1,3)
    for key, value in choices.iteritems():
        if computer == value:
            computer = key

    if player_input == 'rock':
        if computer == 'rock':
            result = "It's a draw!"
        elif computer == 'paper':
            result = "I win!!"
        else:
            result = "You win!!"

    if player_input == 'paper':
        if computer == 'paper':
            result = "It's a draw!"
        elif computer == 'scissors':
            result = "I win!!"
        else:
            result = "You win!!"

    if player_input == 'scissors':
        if computer == 'scissors':
            result = "It's a draw!"
        elif computer == 'rock':
            result = "I win!!"
        else:
            result = "You win!!"
    return "You chose " + player_input + " and I chose " + computer + ". " + result


@app.route("/")
def RPS():
    return render_template("rps.html")

@app.route("/", methods=["POST"])
def resulting():
    player = request.form["choice"]
    return rockPaperScissors(player)

if __name__ == '__main__':
    app.run(debug = True)
