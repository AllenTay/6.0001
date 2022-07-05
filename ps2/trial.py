
from itertools import count
import random
import string
from tkinter import wantobjects

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    filler = ''
    for i in my_word:
      if i != ' ':
        filler += i # ONE LOOKS LIKE a__le
      
    alpha = list(filler) # TWO LIKE ['a', '_', '_', 'l', 'e']
    beta = list(other_word)
    doubles = False
    equal_length = False 
    santa = False
    
    # Make a dictionary counting the number of p's in a_ple and apple and make sure they correspond 
    def check_freq(word):
      freq = {}
      for i in word:
        freq[i] = word.count(i)
      return freq
    
    checker1 = check_freq(alpha)
    checker2 = check_freq(beta)
    
    counter = 0
    number  = 0 # # Number in a_ple is 4, number in a__le is 3
    for j in alpha:
      if j != '_':
        number += 1
    
    #Count the number of unique letters in the keys
    for x in checker1.keys():
      if x in 'abcdeghijklmnopqrstuvwxyz':
        counter += 1

    # CHECK IF EACH PROVIDED LETTER MATCHES THE WHOLE THING
    for k in range(0, min(len(beta), len(alpha))):
        if beta[k] == alpha[k]:
          number -= 1
    
    if number == 0:
      santa = True

    #DICTIONARY TO CHECK IF THE P's are equal 
    for x in checker1:
      if checker1.get(x) == checker2.get(x):
        counter -= 1
    
    if counter == 0:
      doubles = True

    if len(alpha) == len(beta):
      equal_length = True
    
    solution_size = doubles and equal_length
    
    return solution_size and santa


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    copy = wordlist.copy()
    for k in range(len(copy)): # String is placeholder that takes current copy item and checks if it will match the gaps 
      string = copy[k]
      if(match_with_gaps(my_word, string)) == False:
        copy[k] = ' '
    
    stopwords = [' ']
    for word in list(copy):
      if word in stopwords:
        copy.remove(word)
    
    conversion = ''
    if len(copy) == 0:
      conversion = 'No matches found'
    else:
      for i in (copy):
        conversion += i + " "
    
    return conversion


print(show_possible_matches("t_ _ t"))
print(show_possible_matches("a_ pl_ "))
print(show_possible_matches("abbbb_ "))
#print(match_with_gaps('te_ t', 'tact'))
#print(match_with_gaps("a_ _ le", "banana"))
#print(match_with_gaps("a_ _ le", "apple"))
#print(match_with_gaps("a_ ple", "apple"))
#print(show_possible_matches('t_ _ t'))
