def main():
  infile = raw_input('Enter text file 1: ')
  infile2 = raw_input('Enter text file 2: ')
  inFile = open (infile,'r')
  inFile2 = open (infile2,'r')
  l1 = []
  l2 = []
  for line in inFile:
    st = line
    st = st.rstrip('\n')
    tempList = st.split()
    for item in tempList:
      l1.append(item)

  for line in inFile2:
    st = line
    st = st.rstrip('\n')
    tempList = st.split()
    for item in tempList:
      l2.append(item)

  l1.sort()
  l2.sort()

  for item in l1:
    if item in l2:
      print '%s in both l1 and l2' % (item)
    else:
      print '%s in l1 not in l2' % (item)

  for item in l2:
    if (not(item in l1)):
      print '%s in l2 not in l1' % (item)
  set1 = set(l1)
  set2 = set(l2)
  disJoint1 = set1 - set2
  disJoint2 = set2 - set1
  newList1 = list(disJoint1)
  newList2 = list(disJoint2)
  newList1.sort()
  newList2.sort()
  length = len(newList2)
  if (len(newList1) > len(newList2)):
    lenght = len(newList1)

  for i in range(length):
    if (i < (len(newList1))):
      temp1 = newList1[i]
      print 'list 1 item is: %s' % (temp1)
    if (i < (len(newList2))):
      temp2 = newList2[i]
      print 'list 2 item is: %s' % (temp2)
      

  inFile.close()
  inFile2.close()

main()
