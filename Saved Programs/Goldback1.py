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
    if (n % count == 0):
      return False
    count = count + 1

  return True

#def primeComponents (x):
#  a = 2
#  b = 2
#  count = 4
#  while (a <= b):
#    if (n == (a + b)):
#      print n '= %d + %d.' % (a, b)
#      break

def main():
  count = 2
  limit = input ("Enter upper limit: ")
  while (count <= limit):
    if (isPrime(count)):
      print count
    count = count + 1

main()

  
