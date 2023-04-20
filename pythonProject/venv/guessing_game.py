secret_word = "giraffe"
guessing_word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guessing_word != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guessing_word = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose!")
else:
    print("Great Guess!")
