
import string
from string import ascii_letters, ascii_lowercase

def build_shift_dict(shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        box = {'a':1, 'b':2, 'c':3, 'd':4, 'e': 5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13,
                'n': 14, 'o': 15, 'p': 16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,
                'A':1, 'B':2, 'C':3, 'D':4, 'E': 5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13,
                'N': 14, 'O': 15, 'P': 16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26 
                }

        first_reverse = { 1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m',
            14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

        second_reverse = { 1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M',
            14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'  }

        holder = box

        for i in box:
            alpha = (((box.get(i) - 1) + shift) % 26) + 1
            holder[i] = alpha
        
        result = box

        for j in box:
            if j in string.ascii_lowercase:
                #For the letter a, find the value we have attached to the holder
                beta = holder[j]
                ans = first_reverse.get(beta)
                result[j] = str(ans)
            else:
                beta = holder[j]
                ans = second_reverse.get(beta)
                result[j] = str(ans)
        
        return result
            
       

    
def apply_shift(words, shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift        
        
    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
        down the alphabet by the input shift
    '''
    
    mapping = build_shift_dict(shift)   
    bank = list(words)
    solar = []

    for i in bank:
        if i in ascii_letters:
            solar.append(mapping.get(i))
        else:
            solar.append(i)
    s = ''
    s = s.join(solar)
    return s

words = 'abcdef'
power = build_shift_dict(0)
print(power)