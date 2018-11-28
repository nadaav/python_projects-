# 6.00 Problem Set 3
# 
# Hangman

import random
import string

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

guesses = 8
letters_lower = 'abcdefghijklmnopqrstuvwxyz'

def hangman():
    global guesses
    global letters_lower
    word = choose_word(load_words())
    print(word)
    guessing_word = ['_']*len(word)
    print ('Welcome to the game Hangman!\nI am thinking of a word that is'
           , len(word), 'letters long.\n------------') 
    while guesses > 0 and '_' in guessing_word:
        print_out()
        letter = input('Please guess a letter: ').lower()
        assert letter in string.ascii_letters 
        letters_lower = letters_lower.replace(letter,'')
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessing_word[i]=letter
            print('Good guess: ', ''.join(guessing_word))
        if guesses == 0:
            break
        if letter not in word:
            guesses -= 1
            print('Oops! That letter was not on my mind:',''.join(guessing_word))
    guessing_word = ''.join(guessing_word)
    if '_' not in guessing_word:
        print('Congratulations, you won!')

def print_out():
    print ('You have',
           guesses, 'guesses left. \nAvailable letters:', letters_lower)
