#  File: GuessingGame.py

#  Description: Attempts to guess a number chosen by the user, by looking above or below the previous attempt.

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number: 54510

#  Date Created: 11/18/09

#  Date Last Modified: 11/20/09

# Import the list of numbers in the range and reduce the list in half by creating a new list from either
# the upper or lower half.

def numberList (numRange, hiOrLow, guessIdx):
# Initialize the temporary list to start empty.

  newList = []

# If the number guessed was not correct proceed with appending the temp list.

  if (hiOrLow != 0):

# If the guess was high, the search will be in the numbers less than the guess, so it will start at
# the index 0 and go through to the entry right before the guess.

    if (hiOrLow == 1):
      lo = 0
      hi = guessIdx

# If the guess was low, the the search will be in the numbers greater than the guess, so it will start at
# the index of the guess plus 1 and go through to the end of the list.

    elif (hiOrLow == -1):
      lo = guessIdx + 1
      hi = len(numRange)

# Populate the temp list with the new range.

    for i in range (lo, hi):
      newList.append(numRange[i])

# Find the size of the new list created.  If it only has 1 element, then that entry must be the number.
# Setting the guessIdx to -1 ensures that the while loop in guessingGame() is not completed again.

    length = len(newList)
    if (length == 1):
      number = newList[0]
      print
      print 'Your number is:  %s!' % (number)
      newList = 'Thanks for playing the Guessing Game'
      guessIdx = -1
      return (newList, length, guessIdx)
    else:
      return (newList, length, guessIdx)

# If the guess was correct, thank the user for playing and exit the while loop.

  else:
    newList = 'Thanks for playing the Guessing Game'
    guessIdx = -1
    length = 1
    return (newList, length, guessIdx)
    
def guessingGame():

# Set the list of numbers from 1 to 100.

  numList = []
  for i in range(1,101):
    numList.append(i)

# Initialize the lo, hi, count, and mid variables.  Also initialize the oldGuessIdx variable to 1 in order to
# enter the while loop.  Choose the first guess based on the mid point of the number list.  The hiOrLow variable
# determines if the guess was high, low, or correct.  Initializing it to 1 does not affect the outcome, as
# the only decisions based on the variable will come after the user has changed it.

  lo = 0
  hi = 100
  length = hi
  mid = ((lo + hi)/2) - 1
  guessIdx = mid
  oldGuessIdx = 1
  hiOrLow = 1
  guess = numList[mid]
  count = 1
  while ((hiOrLow != 0) and (count < 8) and (oldGuessIdx > 0)):
    print 'Guess  %d :  The number you thought was %d' % (count, guess)
    count = count + 1
    hiOrLow = int(input('Enter 1 if my guess was high, -1 if low, and 0 if correct: '))
    (numList, length, oldGuessIdx) = numberList (numList, hiOrLow, guessIdx)

# If the length of the number list is less than 2 at this point, either the number guessed originally is not
# the number being thought of now, or the user has indicated the guess was in the wrong direction of the answer.

    if (len(numList) < 2):
      print 'You cannot change numbers during the game!'
      oldGuessIdx = -2

# The mid variable is the mid point of the new list.  If the length of the new list is odd, the mid point
# will be rounded down to the nearest integer.  If it is even, the mid point will be 1 less than half the length
# since the index starts at 0.  This will be the index of the next guess in the new list.

    else:
      mid = (length/2)
      if ((int(mid) == float(length)/2.0) and (mid != (0 or 1))):
        mid = mid - 1
      guessIdx = mid
      guess = numList[mid]  

# The oldGuessIdx variable will only be -1 if the number has been found.

  if (oldGuessIdx == -1):
    print
    print numList

# If the number is not found within 7 guesses, the number is not in the range of 1 to 100 ([2**7 = 128] > 100)

  else:
    print 'The number you thought of was not in the correct range. Please try again. '

def main():
  print 'Guessing Game\n'
  print
  print 'Think of a number between 1 and 100 inclusive.'
  print 'And I will guess what it is in 7 tries or less.'
  print
  ready = raw_input('Are you ready? (y/n): ')
  ready = ready.lower()
  while (ready != 'y'):
    ready = raw_input('Are you ready? (y/n): ')
    ready = ready.lower()
  guessingGame()

  
main()
