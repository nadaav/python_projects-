import random
import string

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    WORDLIST_FILENAME = "words.txt"
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = str.split(line)
    return wordlist

# constants
letters_lower = string.ascii_lowercase
guesses = 8

# select random word
word = random.choice(load_words())
# print(word)

guessing_word = ['_'] * len(word)
print ('Welcome to the game Hangman!\nI am thinking of a word that is'
       , len(word), 'letters long.\n------------')

def find_letter(letter):
    for i, v in enumerate(word):
        if v == letter:
            guessing_word[i] = letter
    return ''.join(guessing_word)

def get_input():
    letter = input('Please guess a letter: ').lower()
    if len(letter) == 1 and letter in letters_lower:
        return letter
    else:
        print('Only one letter that you did not try before.')
        return get_input()

# main loop
while guesses > 0 and '_' in guessing_word:
    print ('You have', guesses, 'guesses left. \nAvailable letters:', letters_lower)
    letter = get_input()
    if letter in word:
        letters_lower = letters_lower.replace(letter,'')
        print('Good guess: ', find_letter(letter))
    else:
        guesses-=1
        letters_lower = letters_lower.replace(letter,'')
        print('Oops! That letter was not on my mind:',''.join(guessing_word))

guessing_word = ''.join(guessing_word)

if '_' not in guessing_word:
    print('Congratulations, you won!')
if guesses == 0 and '_' in guessing_word:
    print('Sorry, you lost! The word was', word)
