# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import re
import string
from turtle import up
from typing import Mapping

from idna import valid_contextj
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
word_list = load_words(WORDLIST_FILENAME)

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.text = text
        self.valid_words = []
        wave = text.split()

        for i in wave:
            if is_word(word_list, str(i)) == True:
                self.valid_words.append(i)
        
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy = self.valid_words.copy()
        return copy
        
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        box = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f',
         'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm',
          'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 
          'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', 'A': 'A',
           'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H',
            'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O',
             'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V',
              'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'}

        
        lower_vowels = list(vowels_permutation)
        upper_vowels = list(vowels_permutation.upper())

        lower = 'aeiou'
        upper = 'AEIOU'

        num = 0

        for i in lower:
            box[i] = str(lower_vowels[num])
            num += 1

        nums = 0

        for j in upper:
            box[j] = str(upper_vowels[nums])
            nums += 1
        
        return box

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        # You have to take the whole string and split it and then change the vowels 
        # There's probably a string replace function 
        
        s = self.text
        sieve = list(s)
        
    
        for i in range(len(sieve)):
            if sieve[i] in transpose_dict.keys():
                sieve[i] = transpose_dict[sieve[i]]
        
        answer = ''
        for i in sieve:
            answer += i
 
        return answer

class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        sample = 'aieou'
        bank = get_permutations(sample)
        keeper = {}

        for i in bank:
            # Make a transpose dictionary with the sample[i]
            dictionary = SubMessage.build_transpose_dict(self, i)
            # Build a string of the messages 
            trial_words = SubMessage.apply_transpose(self, dictionary)
            
            counter = 0

            #trial_words = trial_words.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
            bank = trial_words.split(" ")
            for j in bank:
                if is_word(word_list, j) == True:
                    counter += 1
            #print(bank, i, counter)

            # Count how many words you get from each aieou combo 
            keeper[i] = counter
        
        #for key, value in keeper.items():
        #    print(key, value)


        driver = max(keeper, key=keeper.get)
        #Driver is the optimal combo 
        solar = SubMessage.build_transpose_dict(self, driver)
        answer = SubMessage.apply_transpose(self, solar)

        return answer
        

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello Apple Moose Paper String Writer There Bamboo!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print(enc_dict)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    #
