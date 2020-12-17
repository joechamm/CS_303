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

def primePair (num1, num2):
  pPair = '= %d + %d' % (num1, num2)
  return pPair
  

# This function finds all the pairs of prime numbers whose sum equals a given even integer
def primeComponents(integer):
  a = 1
  b = integer - a
  pPair = 0
  while (a < b):
    a = a + 1
    b = integer - a
    # Check if the components a and b are prime numbers
    if ((isPrime (a) == True) and (isPrime (b) == True)):
      pPair = primePair (a, b)
      return pPair
      newA = a + 2
      newB = (integer - newA)
      for a in range (newA, newB):
        if ((isPrime (newA) == True) and (isPrime (newB) == True)):
          primePair (newA, newB)
          newPair = primePair (newA, newB)
          if (newPair != pPair):
            return newPair

    
def main():
  count = 4
  while (count <= 100):
    primeComponents (count)
    print count, primeComponents (count) 
    count = count + 2

main()
