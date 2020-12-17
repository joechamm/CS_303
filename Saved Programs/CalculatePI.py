#  File: CalculatePI.py

#  Description: Calculates PI by simulating random throws at a dartboard inscribed in a square

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number: 54510

#  Date Created: 10/07/09

#  Date Last Modified: 10/08/09

import math
import random

# Create the function to compute PI using random numbers
def computePI ( numThrows ):
  count = 0
# For each random value given inside a square with sides length = 2 check to see if
# it falls inside the circle with radius = 1, or outside.  The ratio of the area of the circle to
# the area of the square is PI / 4.  Increasing the count by 1 for each value falling inside the
# circle and taking the ratio of the count to the area of the square times the number of total
# iterations performed, will give values that approach PI as the number of iterations approaches infinity.

  for i in range (numThrows):
    xPos = random.uniform (-1.0, 1.0)
    yPos = random.uniform (-1.0, 1.0)
    if ((math.hypot (xPos, yPos)) < 1):
      count = count + 1
  calPi = 4.0 * (float(count) / numThrows)

  return calPi



def main ():

  print 'Computation of PI using Random Numbers'
  print

# Start with 100 iterations and compare the values of PI computed to the accepted value of PI, then
# show the difference as the number of iterations is increased by a factor of 10 up to 10000000.
  num = 100

  while (num <= 10000000):
    calculatedPi = float (computePI (num))
    difference = (float (calculatedPi)) - (float (math.pi))
    print 'num = %d \tCalculated PI = %f   Difference = %+f' % (num, calculatedPi, difference)
    num = num * 10
    
main()
