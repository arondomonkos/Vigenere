# Vigenere Cipher Encoder
# Author: Áron Domonkos
# Year: 2022

# Function 1
#plain_text = input('Please enter a text up to 255 characters: ')
plain_text = 'Ez a próba szöveg, amit kódolunk!'

# Function 2
plain_text = plain_text.upper()
old_chars = ['Á', 'É', 'Ő', 'Ö', 'Ó', 'Ü', 'Ű', 'Í', '!', ',', '.', ' ']
new_chars = ['A', 'E', 'O', 'O', 'O', 'U', 'U', 'I', '', '', '', '']

for old, new in zip(old_chars, new_chars):
    plain_text = plain_text.replace(old, new)

# Function 3
print('\nFunction 3')
print(plain_text)

# Function 4
#key = input('Please enter a key (max 5 characters): ')
key = 'auto'
key = key.upper()

# Function 5
print('\nFunction 5')
repeats = len(plain_text) // len(key) + 1
key_text = (repeats * key)[:len(plain_text)]
print(key_text)

# Function 6
print('\nFunction 6')

vtable = []
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('Vtable.dat') as f:
    for line in f:
        line = line.strip()
        vtable.append(line)

encoded = []
for char, key_char in zip(plain_text, key_text):
    col = alphabet.index(char)
    row = alphabet.index(key_char)
    encoded_char = vtable[row][col]
    encoded.append(encoded_char)
encoded = ''.join(encoded)
print(plain_text)
print(key_text)
print(encoded)

# Function 7
with open('coded.dat', 'w') as f:
    f.writelines(encoded)