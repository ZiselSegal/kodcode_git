from random import choice
from words import random_words, programming_terms, architecture_design, nature_words


def category_menu():
    print('1.all words\n' \
          '2.programming terms\n' \
          '3.architecture design\n' \
          '4.nature words\n' \
          '5.random')


def get_word_category():
    category_random_words = random_words
    category_programming_terms = programming_terms
    category_architecture_design = architecture_design
    category_nature_words = nature_words
    while True:
        category_menu()
        action = input('enter category number: ')
        match action:
            case '1':
                return category_random_words
            case '2':
                return category_programming_terms
            case '3':
                return category_architecture_design
            case '4':
                return category_nature_words
            case '5':
                return choice([category_nature_words,category_programming_terms,category_architecture_design,category_random_words])
            case _:
                print('unrecognized action please try again')



def get_random_word(hangman_words):
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
    guess_points = 0
    for i,letter in enumerate(secret_word):
        if letter == guess:
            guess_state = guess_state[:i] + letter + guess_state[i + 1:]
            guess_points += 5
    return guess_state,guess_points


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
    score = 0
    previous_guesses = set()
    category = get_word_category()
    secret_word = get_random_word(category)
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
            guess_state, guess_points = update_guess_state(guess,secret_word,guess_state)
            score += guess_points
        else:
            score -= 2.5
            print('incorrect guess')
        previous_guesses.add(guess)
        guesses_remaining -= 1
    if guess_state == secret_word:
        print(f'\n congratulations you won!\n\n the word was: {secret_word}\n\n number of guesses: {len(previous_guesses)}\n\n score: {score}')
    else:
        print(f' \n game over \n the word was: {secret_word}')