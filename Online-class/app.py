from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Initialize the game variables
number_to_guess = random.randint(50, 100)
max_guesses = 5
guess_counter = 0

@app.route('/', methods=['GET', 'POST'])
def guess_game():
    global number_to_guess, guess_counter
    message = ""

    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
        except ValueError:
            message = "Please enter a valid number."
            return render_template('index.html', message=message)
        
        guess_counter += 1

        if guess == number_to_guess:
            message = f"Congratulations! The number was {number_to_guess}. You found it in {guess_counter} guesses."
            # Reset the game
            number_to_guess = random.randint(50, 100)
            guess_counter = 0
        elif guess_counter >= max_guesses:
            message = f"Sorry, you've used all your chances! The number was {number_to_guess}. Better luck next time."
            # Reset the game
            number_to_guess = random.randint(50, 100)
            guess_counter = 0
        elif guess < number_to_guess:
            message = "Too low, try again!"
        elif guess > number_to_guess:
            message = "Too high, try again!"

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
