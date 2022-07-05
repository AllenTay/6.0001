# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
from textwrap import fill
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    guessed = False
    word = list(secret_word)
    for i in letters_guessed:
        if i in word:
            word.remove(i)

    if len(word) == 0:
        guessed = True

    return guessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    filler = []
    secret = list(secret_word)
    
    for i in secret_word:
      filler.append('_ ')
    
    for j in secret:
        if j in letters_guessed: 
            x = secret.index(j)
            filler[x] = j
            secret[x] = '_ '

    conversion = ''
    for k in filler:
        conversion += k
    return conversion

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    holder = list('abcdefghijklmnopqrstuvwxyz')
    for i in letters_guessed:
        if i in holder:
            holder.remove(i)

    conversion = ''
    for k in holder:
        conversion += k
    return conversion
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print(secret_word)
    length = len(secret_word)
    n = 6
    entries = []
    warnings = 3

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(length) + ' letters long.')
    print('You have '+ str(warnings)+ ' left')
    finished = get_guessed_word(secret_word, entries)
    done = False

    while (n > 0):
      print('-------------------')
      print('You have ' + str(n) + ' guesses left')
      print(get_guessed_word(secret_word, entries))
      print('Available letters: ' + get_available_letters(entries))
      alpha = input('Please guess a letter: ')

      if alpha.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        if warnings >= 1:
          warnings -= 1
        else:
          n -= 1
        print('Oops! That is not a valid letter. You have ' + str(warnings) + 'warnings left: ' + get_guessed_word(secret_word, entries))

      else:
        if alpha.lower() in entries:
          warnings -= 1
          print('Oops! You have already guessed that letter. You now have '+ str(warnings)+ 'warnings')

        else: 
          if alpha.lower() in secret_word:
            entries.append(alpha)
            print('Good guess: ' + get_guessed_word(secret_word, entries))
            finished = get_guessed_word(secret_word, entries)
            if finished == secret_word:
              done = True
              break
            
          else:
            if alpha.lower() in 'aeiou':
              n -= 2
            else:
              n -= 1
            entries.append(alpha)
            print('Oops! That letter is not in my word: ' + get_guessed_word(secret_word, entries))
        

    if n <= 0:
      print('Sorry you ran out of guesses. The word was ' + secret_word)   
    if done:
      score = n * len(secret_word)
      print('-------------------')
      print('Congratulations, you won!')
      print('Your total score for this game is: ' + str(score))





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
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
    number = 0 # Number in a_ple is 4, number in a__le is 3
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

    for x in checker1:
      if checker1.get(x) == checker2.get(x):
        counter -= 1
    
    if counter == 0:
      doubles = True

    if len(alpha) == len(beta):
      equal_length= True
    
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    copy = wordlist.copy()
    for k in range(len(copy)):
      string = copy[k]
      if(match_with_gaps(my_word, string)) == False:
        copy[k] = " "
    
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
    
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print(secret_word)
    length = len(secret_word)
    n = 6
    entries = []
    warnings = 3

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(length) + ' letters long.')
    print('You have '+ str(warnings)+ ' warnings left')
    finished = get_guessed_word(secret_word, entries)
    done = False

    while (n > 0):
      print('-------------------')
      print('You have ' + str(n) + ' guesses left')
      print(get_guessed_word(secret_word, entries))
      print('Available letters: ' + get_available_letters(entries))
      alpha = input('Please guess a letter: ')

      if alpha == '*':
        filler = get_guessed_word(secret_word,entries)
        print("Possible word matches are: "  + show_possible_matches(filler))

      if alpha.lower() not in 'abcdefghijklmnopqrstuvwxyz*':
        if warnings >= 1:
          warnings -= 1
        else:
          n -= 1
        print('Oops! That is not a valid letter. You have ' + str(warnings) + 'warnings left: ' + get_guessed_word(secret_word, entries))

      else:
        if (alpha.lower() in entries) and (alpha.lower() != '*'):
          warnings -= 1
          print('Oops! You have already guessed that letter. You now have '+ str(warnings)+ 'warnings')

        else: 
          if alpha.lower() in secret_word or (alpha.lower() == '*'):
            if alpha.lower == '*':
              print()
            else:
              entries.append(alpha)
              print('Good guess: ' + get_guessed_word(secret_word, entries))
              finished = get_guessed_word(secret_word, entries)
              if finished == secret_word:
                done = True
                break
            
          else:
            if alpha.lower() in 'aeiou':
              n -= 2
            else:
              n -= 1
            entries.append(alpha)
            print('Oops! That letter is not in my word: ' + get_guessed_word(secret_word, entries))
        

    if n <= 0:
      print('Sorry you ran out of guesses. The word was ' + secret_word)   
    if done:
      score = n * len(secret_word)
      print('-------------------')
      print('Congratulations, you won!')
      print('Your total score for this game is: ' + str(score))




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
