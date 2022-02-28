#  File: DNA.py

#  Description: Finds the longest common sequence in two strands of DNA

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number:  54510

#  Date Created: 10/21/09

#  Date Last Modified: 10/22/09

# The compare function will compare strand1 and strand2.

def compare (str1, str2):

# Ensure that str1 is always equal or shorter to str2 in length, so as to
# increase efficiency of the program.  If it is not, switch the strings.

  if ((len (str1) >= len (str2))):
    tmpStr = str1
    str1 = str2
    str2 = tmpStr

# Initialize start to 0.

  start = 0

# Set the length of the string being search to start at the length of str1.

  length = (len (str1))

# Create the list cmnSubs.

  cmnSubs = []

# The outer while loop will examine each substring in str1, beginning
# with the largest substring (i.e. all of str1), and continue to reduce
# the length of the substring being searched by 1 if a common substring
# is not found.  The additional constraint that cmnSubs be empty to continue
# running prevents the program from searching any substrings smaller than
# length of the first one found.  

  while ((length >= 2) and (len (cmnSubs) == 0)):
    start = 0

# The inner while loop will slice str1, to obtain each substring.  For each
# successivly smaller substring being sliced in str1, the while loop will
# run once more, with the slice beginning at the index of each value of
# start given.

    while (start <= ((len (str1)) - length)):
      subStr = str1[start:(length + start)]
      end = (len (str1) - length + 1)

# If a common substring is found, the list cmnSubs will appended to include
# that common substring.  Since the inner while loop will run from 0 to the
# difference in str1's length and the length of the substring being searched
# each common substring of this length will be added to cmnSubs.

      if ((str2.find ((subStr))) != -1):
        cmnSubs.append (subStr)
      start = start + 1
    length = length - 1

# If no common substrings exist, display that message.  Otherwise, print
# each item in the list cmnSubs, which will be all the common substrings of
# the length of the longest common substring found.

  if (len (cmnSubs) == 0):
    print 'No Common Sequence Found'
  else:
    print 'Common Subsequence(s): '
    for item in cmnSubs:
      print item
    
      
def main():

# Prompt the user to enter two strings/strands to be compared.

  strand1 = raw_input ('Enter first strand: ')
  strand2 = raw_input ('Enter second strand: ')
  compare (strand1, strand2)
      
main ()

