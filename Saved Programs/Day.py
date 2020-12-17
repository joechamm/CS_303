#  File: Day.py

#  Description: Computes the day of the week for a given date

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number: 54510

#  Date Created: 09/11/09

#  Date Last Modified: 09/15/09

def main():

  # Prompt the user to enter a day
  day = input ("Enter day: ")
  print 'Day = ', day

  # Check to ensure the day entered is a proper value
  while ((day < 1) or (day > 31)):
    day = input ('Please enter a value between 1 and 31: ')
    print 'Day =', day
  
  # Prompt the user to enter a month
  month = input ('Enter the month: ')
  print 'Month =', month

  # Check to ensure the month entered is a proper value
  while ((month < 1) or (month > 12)):
    month = input ('Please enter a value between 1 and 12: ')
    print 'Month =', month

  # Prompt the user to enter a year
  year = input ('Enter the year: ')
  print 'Year =', year

  # Ensure the year entered is a proper value
  while ((year < 1900) or (year > 2100)):
    year = input ('Please enter a value between 1900 and 2100: ')
    print 'Year =', year
  
  # Adjust the month and year to align with the calendar being used
  if ((month == 1) or (month == 2)):
    month = month + 10
    year = year - 1
  else:
    month = month - 2

  # Assign values to the variables a, b, c, d for use in calculation
  a = month
  print 'a =', a
  b = day
  print 'b =', b
  c = (year % 100)
  print 'c =', c
  d = (year / 100)
  print 'd =', d

  # Calculate the weekday using Gauss's algorithm
  w = (13 * a - 1) / 5
  print 'w =', w
  x = c / 4
  print 'x =', x
  y = d / 4
  print 'y =', y
  z = w + x + y + b + c - 2 * d
  print 'z =', z
  r = z % 7
  print 'r =', r
  r = (r + 7) % 7

  # Convert years back to current calendar
  if ((month == 11) or (month == 12)):
    month = month - 10
    year = year + 1
  else:
    month = month + 2
           
  # Display the weekday to the user
  if (r == 0):
    print '%s %s %s Sunday' % (day, month, year)
  elif (r == 1):
    print '%s %s %s Monday' % (day, month, year)
  elif (r == 2):
    print '%s %s %s Tuesday' % (day, month, year)
  elif (r == 3):
    print '%s %s %s Wednesday' % (day, month, year)
  elif (r == 4):
    print '%s %s %s Thursday' % (day, month, year)
  elif (r == 5):
    print '%s %s %s Friday' % (day, month, year)
  elif (r == 6):
    print '%s %s %s Satuday' % (day, month, year)

main()

 
