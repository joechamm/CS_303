def main ():
  # Prompt the user to enter a year
  y = input ('Enter a year: ')
  print 'y =', y

  # Compute Easter Sunday for that year
  a = y % 19
  print 'a =', a
  b = y / 100
  print 'b = ', b
  c = y % 100
  print 'c = ', c
  d = b / 4
  print 'd = ', d
  e = b % 4
  print 'e = ', e
  g = ((8 * b) + 13) / 25
  print 'g = ', g
  h = ((19 * a) + b - d - g + 15) % 30
  print 'h = ', h
  j = c / 4
  print 'j = ', j
  k = c % 4
  print 'k = ', k
  m = (a + (11 * h)) / 319
  print 'm = ', m
  r = ((2 * e) + (2 * j) - k - h + m + 32) % 7
  print 'r = ', r
  n = (h - m + r + 90) / 25
  print 'n = ', n
  p = (h - m + r + n + 19) % 32
  print 'p = ', p

  # Write out the date for Easter Sunday
  print 'In', y, 'Easter Sunday is on', 
  if (n == 3):
    print 'March'
  if (n == 4):
    print 'April',
    print p
    
main()
  
