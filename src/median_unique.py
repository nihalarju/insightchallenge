#! /usr/bin/python

import sys
f=open(sys.argv[1],'r')
fout=open(sys.argv[2],'w')

#f=open('../bup/book1.txt','r')
#fout=open('../tweet_output/ft2_new.txt','w')

sortedlist=[] # List of numbers- number of unique words in a tweet
writestr=str()
numlines=0
medval=0
#from numpy import median

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
    # THIS LOOKS AWFUL, but THIS IS FAST!
    if numlines<10:
        sortedlist.append(numunique)
        sortedlist.sort()
    else:
        length=len(sortedlist)
        if numunique==medval:
            sortedlist.insert( (length)//2, numunique)
        else:
            if numunique>medval:
                if numunique>=sortedlist[length-1]:
                    sortedlist.append(numunique)
                else:
                    indices=range(length//2,length)
                    for i in indices:
                        if numunique<sortedlist[i]:
                            sortedlist.insert(i,numunique)
                            break
            else:
                if numunique<=sortedlist[0]:
                    sortedlist.insert(0,numunique)
                else:
                    indices=range(0,length//2)
                    indices.reverse()
                    for i in indices:
                        if numunique>sortedlist[i]:
                            sortedlist.insert(i+1,numunique)
                            break

    # After populating the list of number of unique words, we find the median
    if numlines %2 == 1:
        medval=float(sortedlist[((numlines+1)//2)-1])
    else:
        medval=sum(sortedlist[(numlines//2)-1:(numlines//2)+1])/2.

    # Find out and write the median in a list
    fout.write(  "%0.2f" % medval + '\n'  )

# Clean up
fout.close()
f.close()

