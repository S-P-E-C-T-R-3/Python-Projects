import random
from hangman_art import stages, logo
from hangman_words import words
from os import system

selected_word = random.choice(words)
print("selected word is ", selected_word)
lives = 6
display = []
print(logo)

for _ in range((len(selected_word))):
    display += "_"

game_ended = False

while not game_ended:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        system('cls')
        print(f"You guessed {guess}")

    for position in range(len(selected_word)):
        letter = selected_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in selected_word:
        system('cls')
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_ended = True
            print("You loose")
    print(f"{''.join(display)}")
    if "_" not in display:
        game_ended = True
        print("You win")
    print(stages[lives])
