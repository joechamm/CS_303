#  File: CalcSqrt.py

#  Description: Calculates the square root of a number entered

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number: 54510 

#  Date Created: 20 September, 2009

#  Date Last Modified: 24 September, 2009


def main():
  #Prompt the user to enter a positive number, and ensure it is greater than zero
  n = input ('Enter a number greater than zero: ')
  while (n <= 0):
    n = input ('Error! Please enter a value greater than zero: ')
  print 'Number: ', n
    
  #Define variable oldGuess and newGuess and evaluate the difference
  oldGuess = n / 2.0
  newGuess = ((n / oldGuess) + oldGuess) / 2.0
  difference = abs (oldGuess - newGuess)

  #Using the given variables, compute given algorithm until difference is less than 1.0e-06
  while (difference > 1.0e-06):
    oldGuess = newGuess
    newGuess = (( n / oldGuess) + oldGuess) / 2.0
    difference = abs (oldGuess - newGuess)
      
  #Calculate and display the difference
  print 'Square root is: ', newGuess
  diff = newGuess - (n ** 0.5)
  print 'Difference is: ', diff

main()
  
