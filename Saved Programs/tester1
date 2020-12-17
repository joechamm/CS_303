#  File: Goldbach.py

#  Description: Demonstrates Goldbach's conjecture for even integers between 4 and 100

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number: 54510

#  Date Created: 10/01/09

#  Date Last Modified: 10/01/09


# This function determines if a given number is prime or not
def isPrime (n):
  limit = int (n**0.5)
  count = 2
  while (count <= limit):
    if ((n % count == 0) or (n == 1)):
      return False
    count = count + 1
  return True

# This function creates a string from the pair of primes found, and then returns that string
def primePair (num1, num2):
  placeHolderA = '= %d + %d ' % (num1, num2)
  return placeHolderA
  

# This function finds all the prime number pairs that add to the input integer
def primeComponents(integer):
  a = 1
  b = integer - a
# Create two place holders for the string containing the integer's prime pairs
  oldPair = ''
  newPair = ''
  while (a < b):
    a = a + 1
    b = integer - a
    # Check if the components a and b are prime numbers
    if ((isPrime (a) == True) and (isPrime (b) == True)):
      # Use the primePair function to return a string value
      oldPair = primePair (a, b)
      # Ensure that the correct string is returned for integers with only one pair of primes
      if (newPair == ''):
        newPair = oldPair
      # Combine the strings into one element
      if (newPair != oldPair):
        newPair = newPair + oldPair
      # For value less than eight ensure that some string is returned
      if (integer < 8):
        return oldPair
  # Return the value of primeComponents function for each value of count
  return newPair

    
def main():
  count = 4
  while (count <= 100):
    print count, \
          primeComponents (count) 
    count = count + 2

main()
