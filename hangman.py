import random, string, sys

words = ["python", "java", "swift", "javascript"]
secret_word = list(random.choice(words))
hidden_word = list('-' * len(secret_word))  # [- - - - -]
letters_in_word = set(secret_word)  # {p, y, t, h, o, n}
letters_appeared = list()
attempts = 8
score = {'won': 0, 'lost': 0}

print('H A N G M A N')

while True:
    game_type = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    
    if game_type == 'play':
        secret_word = list(random.choice(words))
        hidden_word = list('-' * len(secret_word))
        letters_in_word = set(secret_word)
        letters_appeared = []
        attempts = 8

        while attempts > 0:
            print(f"\n{''.join(hidden_word)}")
            guess_letter = input("Input a letter: ").strip()

            if len(guess_letter) != 1:
                print('Please, input a single letter.')
                continue

            if guess_letter not in string.ascii_lowercase:
                print('Please, enter a lowercase letter from the English alphabet.')
                continue

            if guess_letter in letters_appeared:
                print('You\'ve already guessed this letter.')
                continue

            letters_appeared.append(guess_letter)

            if guess_letter in secret_word:
                for i in range(len(secret_word)):
                    if secret_word[i] == guess_letter:
                        hidden_word[i] = guess_letter
                if hidden_word == secret_word:
                    print(f'You guessed the word {"".join(secret_word)}!')
                    print('You survived!')
                    score['won'] += 1
                    break
            else:
                attempts -= 1
                print('That letter doesn\'t appear in the word.')
                if attempts == 0:
                    print(f'\nYou lost! The word was {"".join(secret_word)}.')
                    score['lost'] += 1
                    break

    elif game_type == 'results':
        print(f'You won: {score["won"]} times.\nYou lost: {score["lost"]} times.')
    elif game_type == 'exit':
        sys.exit()
    else:
        print("Invalid input. Please choose 'play', 'results', or 'exit'.")
