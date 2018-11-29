import random
import string
import re

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = str.split(line)
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def hangman():
    guesses = 8
    letters_lower = 'abcdefghijklmnopqrstuvwxyz'
    word = choose_word(load_words())
    print(word)
    guessing_word = ['_']*len(word)
    print ('Welcome to the game Hangman!\nI am thinking of a word that is'
           , len(word), 'letters long.\n------------') 
    while guesses > 0 and '_' in guessing_word:
        print_out(guesses, letters_lower)
        letter = input('Please guess a letter: ').lower()
        assert letter in string.ascii_letters 
        if letter in word:
            print('Good guess: ', find_letter(guessing_word, word, letter))
        else:
            if letter in letters_lower:
                guesses -= 1
                print('Oops! That letter was not on my mind:',''.join(guessing_word))
            else:
                print('You already used the letter', letter)
        letters_lower = letters_lower.replace(letter,'')
    guessing_word = ''.join(guessing_word)
    if '_' not in guessing_word:
        print('Congratulations, you won!')
    if guesses == 0 and '_' in guessing_word:
        print('Sorry, you lost! The word was', word)

def find_letter(guessing_word, word, letter):
    for match in re.finditer(letter, word):
        a = match.start()
        guessing_word[a] = letter
    return ''.join(guessing_word)

def print_out(guesses, letters_lower):
    print ('You have',
           guesses, 'guesses left. \nAvailable letters:', letters_lower)

