from random import choice

def get_random_word():
    hangman_words = [
        "mountain", "bicycle", "penguin", "elephant", "keyboard", 
        "sunflower", "rainbow", "thunder", "pyramid", "jupiter", 
        "pancakes", "volcano", "telescope", "blanket", "whisper", 
        "country", "library", "diamond", "avocado", "marathon", 
        "calendar", "dolphin", "journey", "mansion", "orchard", 
        "glacier", "hammock", "village", "fountain", "horizon", 
        "lantern", "compass", "sculpture", "notebook", "starlight", 
        "backpacker", "adventure", "waterfall", "blueprint", "festival", 
        "microscope", "wildlife", "symphony", "platinum", "umbrella", 
        "harvest", "campfire", "clover", "monument", "lighthouse"
    ]
    return choice(hangman_words)


def get_valid_guess():
    guess = input('please enter your guess: ')
    while len(guess) != 1 or not guess.isalpha():
        print('invalid format please enter a single letter')
        guess = input('please enter your guess: ')
    return guess.lower()



def get_guess_limit():
    limit = input('please enter guess limiit: ')
    while not limit.isdigit() or not limit:
        print('invalid format please enter a number')
        limit = input('please enter guess limiit: ')
    return int(limit)


def run_game():
    previous_guesses = ''
    secret_word = get_random_word()
    print(f'the word length is {len(secret_word)} choose guess limit wisely')
    guesses_remaining = get_guess_limit()
    guess_state = '-' * len(secret_word)
    while guesses_remaining and guess_state != secret_word:
        if previous_guesses:
            print(f'previous guesses: {' '.join([letter for letter in previous_guesses])} \n \n  guesses_remaining:{guesses_remaining} \n \n progress: {guess_state}')
        guess = get_valid_guess()
        if guess in previous_guesses:
            print('letter already guessed please try again')
            continue
        elif guess in secret_word:
            for i,letter in enumerate(secret_word):
                if letter == guess:
                    guess_state = guess_state[:i] + letter + guess_state[i + 1:]
        previous_guesses += guess
        guesses_remaining -= 1
    if guesses_remaining:
        print(f'congratulations you won!\n \n the word was: {secret_word} \n \n number of guesses: {guesses_remaining + len(previous_guesses) - guesses_remaining}')
    else:
        print(f'game over \n the word was{secret_word}')

run_game()