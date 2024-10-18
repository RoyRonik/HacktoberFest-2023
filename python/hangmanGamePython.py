import random
import csv

def load_words_from_csv(file_name):
    words = []
    with open('hangman dataset.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            words.append(row[0])
    return words

def choose_word(words):
    return random.choice(words)

def display_current_state(word, guessed_letters):
    current_state = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print("Current word: ", current_state)

def play_hangman():
    words = load_words_from_csv('words.csv')  
    word = choose_word(words)
    guessed_letters = []
    attempts_left = 6  
    
    print("Welcome to Hangman!")
    
    while attempts_left > 0:
        display_current_state(word, guessed_letters)
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'!")
        elif guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.append(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            guessed_letters.append(guess)
            attempts_left -= 1
            print(f"Attempts left: {attempts_left}")
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word '{word}'. You win!")
            break
    else:
        print(f"Game over! The word was '{word}'.")

play_hangman()