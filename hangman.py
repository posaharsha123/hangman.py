import random

# Hangman stages images
hangman_stages = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    """
]
print("welcome to hangman")

word_list = ["apple", "mango", "carrot", "onion"]
lives = 6
chosen_word = random.choice(word_list)

display = ["_" for _ in chosen_word]

print(display)

game_over = False
while not game_over:
    guess = input("Enter a letter: ").lower()
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        print(display)
    else:
        lives -= 1
        print(hangman_stages[6 - lives])
        print("Incorrect guess. Lives left:", lives)
        if lives == 0:
            print("You lose! The word was", chosen_word)
            game_over = True

    if "_" not in display:
        print("Congratulations! You guessed the word:", chosen_word)
        game_over = True
