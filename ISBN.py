#  File: ISBN.py

#  Description: Checks to see if a number is a valid ISBN or not.

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number: 54510

#  Date Created: 10/29/09

#  Date Last Modified: 10/29/09

import string

# Create a function to check if a line is a valid ISBN.

def isbnCheck (st):
  
# Initialize 3 lists and 2 sums.

  digList = []
  s1 = []
  s2 = []
  sum1 = 0
  sum2 = 0

# Populate the digList list with the valid characters from each line.

  for ch in st:
    if ((ch.isdigit() == True) or (ch.lower() == 'x') or (ch == '-')):
      if ((ch.isdigit() == True)):
        digList.append(ch)

# Substitute 10 for X, as long as it is the last character.

      elif ((ch.lower() == 'x') and (len (digList) == 9)):
        digList.append(10)

# If the for loop encounters a character that is not a digit, an X at
# the end, or a '-' erase the list and break the loop.

    else:
      digList = []
      break

# First, check to see if the list is the correct length.

  if (len(digList) == 10):

# Populate the s1 and s2 lists with the sums of the digits.

    for item in digList:
      sum1 = sum1 + int (item)
      s1.append(sum1)
    for item in s1:
      sum2 = sum2 + int (item)
      s2.append(sum2)
        
# Return true if all preconditions have been met, and the last digit
# of the s2 list is divisible by 11.

  if (len(s2) == 10):
    if ((s2[-1] % 11 == 0)):
      return True

# Otherwise return False.

  else:
    return False
  

def main():

# Open the files.

  inFile = open ('isbn.txt', 'r')
  outFile = open ('isbnOut.txt', 'w')

# Go through each line in the isbn.txt file, and check if it
# is valid with the isbnCheck function.

  for line in inFile:
    line = line.rstrip('\n')

# If it is valid, write as such to the outfile.

    if (isbnCheck (line) == True):
      line = line +  '  valid \n'
      outFile.write (line)

# If not, write it as invalid.

    else:
      line = line + '  invalid \n'
      outFile.write (line)
  inFile.close()
  outFile.close()

main()
