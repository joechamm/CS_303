#  File: Integer.py

#  Description: Reverses the digits of an integer entered

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number: 54510

#  Date Created: 09/15/09

#  Date Last Modified: 09/15/09

def main():

  # Prompt the user to enter a positive integer
  integer = input ('Enter a positive integer: ')
  while (integer < 1):
    integer = input ('Enter a positive integer: ')
    
  # Determine how many digits there will be and assign them each to a variable
  if (integer < 9):
    print 'Reverse of integer is: ', integer
  if ((integer > 9) and (integer < 100)):
    a = integer % 10
    b = integer / 10
    print 'Reverse of integer is: ', a,b
  if ((integer > 99) and (integer < 1000)):
    a = integer % 10
    b = (integer % 100) / 10
    c = integer / 100
    print 'Reverse of integer is: ', a,b,c
  if ((integer > 1000) and (integer < 10000)):
    a = integer % 10
    b = (integer % 100) / 10
    c = (integer % 1000) / 100
    d = integer / 1000
    print 'Reverse of integer is: ', a,b,c,d
  if ((integer > 10000) and (integer < 100000)):
    a = integer % 10
    b = (integer % 100) / 10
    c = (integer % 1000) / 100
    d = (integer % 10000) / 1000
    e = integer / 10000
    print 'Reverse of integer is: ', a,b,c,d,e
  if ((integer > 100000) and (integer < 1000000)):
    a = integer % 10
    b = (integer % 100) / 10
    c = (integer % 1000) / 100
    d = (integer % 10000) / 1000
    e = (integer % 100000) / 10000
    f = integer / 100000
    print 'Reverse of integer is: ', a,b,c,d,e,f

main ()       
  
