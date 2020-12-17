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


def primeComponents(integer):
  a = 1
  b = 1
  while (a <= b):
    a = a + 1
    b = integer - a
    if ((isPrime (a) == True) and (isPrime (b) == True)):
      sumOfCount = '%d + %d' % (a, b)
      return sumOfCount
    else:
      return False
#      print integer,'= %d + %d' % (a,b)
      
def main():
  count = 4
  while (count <= 100):
    while (primeComponents (count) != False):
      Sums = primeComponents (count)
      print count, '=', Sums,
      count = count + 2
    count = count + 2

main()

  
