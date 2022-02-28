#  File: Cipher.py

#  Description: Uses the Caesar Cipher to encrypt or decrypt a file.

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number: 54510

#  Date Created: 10/14/09

#  Date Last Modified: 10/16/09


# This function will encrypt a string using the Caesar Cipher to shift
# the characters an amount specified by the user.

def encrypt(st, shift):
  newSt = ""

# Look at each character in the string.

  for ch in st:

# Check if the charcter is a letter or digit.

    if (ch.isalpha ()):

# If it is a letter, check to see if it is upper or lower case

      if (ch.isupper ()):

# Create a new character by 'shifting' the ASCII value of the original
# the amount specified by the user, and then converting back to a
# character.

        newCh = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))

# Attach the new charcter to the new string being created by concatenating
# the newly created character with the previously created characters
# preceded by it.

        newSt = newSt + newCh

      else:

        newCh = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        newSt = newSt + newCh

# If the character is a digit, shift the digit by the specified amount,
# transform it to a string character, and attach it to the new string in
# the same way the letter characters were attached.

    elif (ch.isdigit ()):
      newCh = ((int(ch) + shift) % 10 )
      newCh = '%s' % (newCh)
      newSt = newSt + str(newCh)

# If the character is not a letter or digit, simple insert the character
# into the new string 'as is.'

    else:
      newCh = ch
      newSt = newSt + newCh
  return newSt  

# This function decrypts a string by reversing the operation of the encrypt
# function.  By 'shifting' the ASCII value back to the left the amount
# specified by the user, the function reverses the encrypt process of
# 'shifting' the ASCII value to the right the same amount.

def decrypt(st, shift):
  newSt = ""
  for ch in st:
    if (ch.isalnum()):
      if (ch.isalpha ()):
        if (ch.isupper ()):
          newCh = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
          newSt = newSt + newCh
        else:
          newCh = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
          newSt = newSt + newCh
      else:
        newCh = ((int(ch) - shift) % 10)
        newCh = '%s' % (newCh)
        newSt = newSt + str(newCh)
    else:
      newCh = ch
      newSt = newSt + newCh
  return newSt  


def main():

# Prompt the user to encrypt or decrypt, enter the input file, enter the
# output file, and the value to shift the function.

  userChoice = raw_input ('Do you want to encrypt or decrypt? (E / D): ')
  inFile = open (raw_input ('Enter name of input file: '))
  shift = input ('Enter shift parameter: ')
  oFile = raw_input ('Enter name of output file: ')
  outFile = open (oFile, "w")
  if ((userChoice == 'E') and (shift == int (abs(shift)))):
    for line in inFile:
      line = line.rstrip("\n")
      outFile.write (encrypt (line, shift) + "\n")
      newSt = encrypt(line, shift)  
    print 'Output written to %s' % (oFile)
  elif ((userChoice == 'D') and (shift == int (abs(shift)))):
    for line in inFile:
      line = line.rstrip("\n")
      outFile.write (decrypt (line, shift) + "\n")
      newSt = decrypt (line, shift)
    print 'Output written to %s' % (oFile)
  else:
    print 'Invalid Input'

# Close the files.

  inFile.close()
  outFile.close()
  

main()

  
