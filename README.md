# Vigenère cipher project

This project implements a simple Vigenère cipher encoder based on a classic 16th-century cryptographic technique using a Vigenère table.

## Description

The program performs the following steps:

1. **Function 1** – Reads a maximum 255-character plaintext input from the user.
2. **Function 2** – Transforms the plaintext:
   - Replaces accented Hungarian characters with their base equivalents (e.g., ő → o).
   - Keeps only letters from the English alphabet.
   - Converts the entire string to uppercase.
3. **Function 3** – Displays the cleaned plaintext on screen.
4. **Function 4** – Asks for a keyword (up to 5 characters, must be uppercase and only English letters).
5. **Function 5** – Repeats the keyword until it matches the length of the plaintext, forming the key string.
6. **Function 6** – Encrypts the text using the Vigenère table (loaded from `Vtable.dat`), where for each character:
   - Finds the row corresponding to the keyword letter.
   - Finds the column corresponding to the plaintext letter.
   - Uses the intersecting cell as the encoded character.
7. **Function 7** – Writes the encoded message to a file named `coded.dat`.

## Input files

- `Vtable.dat`: Contains the Vigenère table used for encoding.

## Output files

- `coded.dat`: Contains the encoded result.

## Example

Plaintext: `Ez a próba szöveg, amit kódolunk!`  
Transformed plaintext: `EZAPROBASZOVEGAMITKODOLUNK`  
Keyword: `auto` → Transformed to `AUTO`  
Generated key string: `AUTOAUTOAUTOAUTOAUTOAUTOAUT`  
Encoded output: `ETTDRIUOSTHJEATAINDCDIEINE`

---
Developed by Áron Domonkos, 2022.