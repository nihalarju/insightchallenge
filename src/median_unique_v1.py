#! /usr/bin/python

import sys
f=open(sys.argv[1],'r')
fout=open(sys.argv[2],'w')
uniquelist=[] # List of numbers- number of unique words in a tweet
writestr=str()
from numpy import median

for line in f:
    line_list=[] # list of words in a tweet
    # Read a tweet, make list of words
    line=line.strip() # Remove the redundant '\n' etc.
    linewords = line.split(" ") # Make a list of words from the line

    # Next we find out number of unique words
    numunique=0
    for word in linewords:
        if word not in line_list:
            numunique+=1
            line_list.append(word)
    uniquelist.append(numunique)

    # Find out and write the median in a list
    # THIS STEP TAKES MOST OF TIME!
    fout.write(   str( median(uniquelist) ) + '\n'   )

# Clean up
fout.close()
f.close()

