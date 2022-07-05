import re


other_word = 'bep'

my_word = 'a_ pl_ '

filler = ''
for i in my_word:
    if i != ' ':
     filler += i # ONE LOOKS LIKE a__le
      
alpha = list(filler) # TWO LIKE ['a', '_', '_', 'l', 'e']
beta = list(other_word)


number = 0
for j in alpha:
    if j != '_':
        number += 1


for k in range(len(beta)):
    if beta[k] == alpha[k]:
        number -= 1

print(str(number))