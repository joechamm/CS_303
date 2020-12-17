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



def primeComponent(x):
  count = 2
  limit = 100
  while (count <= limit):
    if (isPrime(count)):
      print count
    count = count + 1

def main():
  count = 4
  a = 2
  b = 2
  for count in range (4, 101, 2):
    while ((a + b) <= count):
      for a in range (2, (count - b)):
        if (isPrime (a) == True):
          for b in range ((a), (count - a)):
            if (isPrime (b) == True):
              if (count == (a + b)):
                print count,'= %d + %d' %d (a,b)
            
            b = b + 1
        
        a = a + 1
    

main()

  
