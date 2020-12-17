#  File: Goldbach.py

#  Description:

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number: 54510

#  Date Created: 09/03/09

#  Date Last Modified: 09/03/09


# This function determines if a given number is prime or not
def isPrime (n):
  limit = int (n**0.5)
  count = 2
  while (count <= limit):
    if ((n % count == 0) or (n == 1)):
      return False
    count = count + 1
  return True


# This function finds all the pairs of prime numbers whose sum equals a given even integer
def primeComponents(integer):
  a = 1
  b = integer - a
  print '%d =' % (integer),
  while (a < b):
    a = a + 1
    b = integer - a
    # Check if the components a and b are prime numbers
    if ((isPrime (a) == True) and (isPrime (b) == True)):
      printSum = '= %d + %d' % (a, b)
      # Check to see if there are any other pairs of a and b for the integer
      for a in range (a, b, 2):
        if ((isPrime (a + 2) == True) and (isPrime (integer - a - 2) == True)): break
        else:
          print printSum
        print printSum,
     
def main():
  count = 4
  while (count <= 100):
    primeComponents (count)
    count = count + 2

main()
