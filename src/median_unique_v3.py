#! /usr/bin/python

import sys
f=open(sys.argv[1],'r')
fout=open(sys.argv[2],'w')
uniquelist=[] # List of numbers- number of unique words in a tweet
writestr=str()
numlines=0

for line in f:
    line_list=[] # list of words in a tweet
    numlines+=1
    # Read a tweet, make list of words
    line=line.strip() # Remove the redundant '\n' etc.
    linewords = line.split(" ") # Make a list of words from the line

    # Next we find out number of unique words
    numunique=0
    for word in linewords:
        if word not in line_list:
            numunique+=1
            line_list.append(word)

    # The numpy median function is not the best in this case.
    # Since we populate the list of numbers, we can populate it
    # to be in ascending order. Therefore reducing the
    # computational load.

    if numlines==1 or numunique>max(uniquelist):
        uniquelist.append(numunique)
    else:
        for i, unique in enumerate(uniquelist):
            if numunique < unique:
                uniquelist.insert(i,numunique)
                break
        
    # Find out and write the median in a list
    # uniquelist.sort()
    if numlines %2 == 1:
        median=float(uniquelist[((numlines+1)//2)-1])
    else:
        median=sum(uniquelist[(numlines//2)-1:(numlines//2)+1])/2.

    fout.write(  str(median) + '\n'  )
print uniquelist
# Clean up
fout.close()
f.close()

