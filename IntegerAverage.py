#  File: Integer.py

#  Description: Averages Integers Entered by User

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number: 54510

#  Date Created: 09/15/09

#  Date Last Modified: 09/15/09

def main():

  # Prompt the user to enter a positive integer
  integer = input ("Enter a positive integer: ")

  # Prevent division by 0
  if (integer > 0):
    sum = integer
    count = 0
  # Start loop by asking user to input positive integer, then proceed to sum them all.
    while ((integer > 0)):
      integer = input ("Enter a positive integer: ")
      sum = sum + integer
      count = count + 1   
      print 'Sum = ', sum
      average = float (sum) / count
    print 'Sum = ', sum
    print 'Number of integers entered = ', count
    print 'Average = ', average
  else:
    print 'Done.'

main ()


       
  
