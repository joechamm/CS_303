#  File: Books.py

#  Description: Analyzes the frequency of distinct and unique words in two works of literature.

#  Student Name: Joseph Cunningham

#  Student UT EID: jsc2539

#  Course Name: CS 303E

#  Unique Number: 54510

#  Date Created: 11/11/09

#  Date Last Modified: 11/12/09

import string

# Removes punctuation marks from a string
def parseString (st):
  newSt = ''
  st1 = st
  st1 = st1.rstrip('\n')
  for ch in st1:
    if (ch == '-'):
      newSt = newSt + ' '
    elif ((ch.isalpha() == True) or (ch.isspace() == True)):
      newSt = newSt + ch
  return (newSt)
    
# Returns a dictionary of words and their frequencies.
def getWordFreq (textFile):
  inFile = open (textFile, 'r')

# Create an empty dictionary, a list for capital words
  wordDic = {}
  capitalList = []
  lowerList = []

# Go line by line through the text document, and create a string with all
# punctuation removed. Then empty the words of the line into a temporary
# list, and then put them into the dictionary. Each time a word is encountered
# that is new, it is added to the dictionary with a frequency value of 1, and if
# it already exists there, the frequency is increased by 1.

  for line in inFile:
    st1 = parseString (line)
    tempList = st1.split()
    for item in tempList:
      if (item in wordDic):
        freq = wordDic[item] + 1
        wordDic[item] = freq
      else:
        wordDic[item] = 1
   
# Close the infile.
  inFile.close()

# Go word by word through the dictionary keys, and look for capitalized words.
# If the capitalized word is found in the dictionary in lower case, it is assumed
# to have been capitalized because it came at the beginning of a sentence, not
# because it is a proper noun. If it is assumed to not be a proper noun, the
# the frequency of the capitalized version of the word is added to the frequency
# of the lower case version, and the capitalized word is added to a list to be
# removed from the dictionary later. If the capitalized word is assumed to be a
# proper noun, it is put into a list for removal from the dictionary.

  for word in wordDic:
    tempWord = word
    if (tempWord.capitalize() == tempWord):
      lowerCase = tempWord.lower()
      if (lowerCase in wordDic):
        lowFreq = wordDic[word] + wordDic[tempWord]
        capitalList.append(tempWord)
      else:
        capitalList.append(tempWord)

# Remove proper nouns and now redundant words in the dictionary.
  for item in capitalList:
    del wordDic[item]

  return wordDic
    
# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):

# Create a list of all the words that are not proper nouns for each author, and
# then determine all of the distinct words used by the author.

  auth1Keys = freq1.keys()
  set1 = set(auth1Keys)
  auth2Keys = freq2.keys()
  set2 = set(auth2Keys)

# Turn the sets back into lists.

  auth1 = list(set1)
  auth2 = list(set2)

# Determine the number of distinct words used by each author.

  nDistWords1 = len(auth1)
  nDistWords2 = len(auth2)

# For each word in the dictionary, add the frequency of the word the the
# frequencies of all the others to obtain a total word count.

  wordSum1 = 0
  wordSum2 = 0
  for word in freq1:
    wordSum1 = wordSum1 + freq1[word]
  for word in freq2:
    wordSum2 = wordSum2 + freq2[word]

# Calculate the ratio of distinct words to total words.

  ratio1 = 100 * (float(nDistWords1)/float(wordSum1))
  ratio2 = 100 * (float(nDistWords2)/float(wordSum2))

# Create a set of words unique to each particular author, and determine
# the number of words in each disjoint set.

  uniqSet1 = set1 - set2
  uniqSet2 = set2 - set1
  numInUniq1 = len(uniqSet1)
  numInUniq2 = len(uniqSet2)

# Create a list of unique words for each author, and determine the total amount
# of these words for each author by adding all their frequencies together.

  uniqList1 = list(uniqSet1)
  uniqList2 = list(uniqSet2)
  uniqFreq1 = 0
  for word in uniqList1:
    uniqFreq1 = uniqFreq1 + freq1.get(word)

  uniqFreq2 = 0
  for word in uniqList2:
    uniqFreq2 = uniqFreq2 + freq2.get(word)

# Calculate the relative frequency of words used by each author that are unique
# to each work by taking the total number of unique words and finding its ratio
# to the total number of words in each work.

  relFreqRatio1 = 100 * (float(uniqFreq1)/float(wordSum1))
  relFreqRatio2 = 100 * (float(uniqFreq2)/float(wordSum2))

# Display the data.

  print '%s' % (author1)
  print 'Total distinct words = ', nDistWords1
  print 'Total words (including duplicates) = ', wordSum1
  print 'Ratio (% of total distinct words to total words) = ', ratio1
  print
  print '%s' % (author2)
  print 'Total distinct words = ', nDistWords2
  print 'Total words (including duplicates) = ', wordSum2
  print 'Ratio (% of total distinct words to total words) = ', ratio2
  print
  print '%s used %d words that %s did not use.' % (author1, numInUniq1, author2)
  print 'Relative frequency of words used by %s not in common with %s = %.7f' % (author1, author2, relFreqRatio1)
  print 
  print '%s used %d words that %s did not use.' % (author2, numInUniq2, author1)
  print 'Relative frequency of words used by %s not in common with %s = %.7f' % (author2, author1, relFreqRatio2)
  
  
def main():

# Prompt the user to enter the file name of the books to be analyzed.
  book1 = raw_input ("Enter name of first book: ")
  book2 = raw_input ("Enter name of second book: ")
  print
  
# Enter names of the two authors.
  author1 = raw_input ("Enter last name of first author: ")
  author2 = raw_input ("Enter last name of second author: ")
  print
   
# Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)
  
# Compare the two works by their word frequencies.
  wordComparison (author1, wordFreq1, author2, wordFreq2)
  

main()
