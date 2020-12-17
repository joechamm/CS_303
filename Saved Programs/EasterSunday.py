#  File: EasterSunday.py

#  Description: Computes the date of Easter Sunday for given year

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number: 54510

#  Date Created: 09/09/09

#  Date Last Modified: 09/09/09

def main ():
  # Prompt the user to enter a year
  y = input ('Enter a year: ')

  # Compute Easter Sunday for that year
  a = y % 19 
  b = y / 100
  c = y % 100
  d = b / 4
  e = b % 4
  g = ((8 * b) + 13) / 25
  h = ((19 * a) + b - d - g + 15) % 30
  j = c / 4
  k = c % 4
  m = (a + (11 * h)) / 319
  r = ((2 * e) + (2 * j) - k - h + m + 32) % 7
  n = (h - m + r + 90) / 25
  p = (h - m + r + n + 19) % 32

  # Write out the date for Easter Sunday
  print 'In', y, 'Easter Sunday is on', 
  if (n == 3):
    print 'March',
    print p
  if (n == 4):
    print 'April',
    print p
    
main()
  
