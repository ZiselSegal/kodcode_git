from random import choice
from words import words

def get_random_word():
    hangman_words = words
    word = choice(hangman_words)
    return word.lower().strip()


def get_valid_guess():
    guess = input('please enter your guess: ')
    while len(guess) != 1 or not guess.isalpha():
        print('invalid format please enter a single letter')
        guess = input('please enter your guess: ')
    return guess.lower().strip()


def get_guess_limit():
    limit = input('please enter guess limiit: ').strip()
    while not limit.isdigit() or not limit:
        print('invalid format please enter a number')
        limit = input('please enter guess limiit: ').strip()
    return int(limit)


def update_guess_state(guess,secret_word,guess_state):
    for i,letter in enumerate(secret_word):
        if letter == guess:
            guess_state = guess_state[:i] + letter + guess_state[i + 1:]
    return guess_state


def start_game_logo():
    start_message = """
    =========================
        WELCOME TO HANGMAN   
    =========================
        +---+
        |   |
            |
            |
            |
            |
        =========
        
    Good luck! Let's begin...
    """

    print(start_message)


def run_game():
    start_game_logo()
    previous_guesses = set()
    secret_word = get_random_word()
    print(f'the word length is {len(secret_word)} choose guess limit wisely')
    guesses_remaining = get_guess_limit()
    guess_state = '-' * len(secret_word)
    while guesses_remaining and guess_state != secret_word:
        print(f'\nprevious guesses: {' ,'.join([letter for letter in previous_guesses])}\n\nguesses_remaining:{guesses_remaining}\n\nprogress: {guess_state}\n')
        guess = get_valid_guess()
        if guess in previous_guesses:
            print('letter already guessed please try again')
            continue
        elif guess in secret_word:
            guess_state = update_guess_state(guess,secret_word,guess_state)
        previous_guesses.add(guess)
        guesses_remaining -= 1
    if guess_state == secret_word:
        print(f'\n congratulations you won!\n \n the word was: {secret_word}\n\n number of guesses: {len(previous_guesses)}')
    else:
        print(f' \n game over \n the word was: {secret_word}')