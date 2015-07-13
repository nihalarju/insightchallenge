#! /usr/bin/python

# This program reads in a text file line by line, and finds the median
# number of unique words per line. 

# We do not use numpy's median function because that's not the fastest way
# to do this. Instead we populate list of numbers in ascending order.
    
import sys
f=open(sys.argv[1],'r')
fout=open(sys.argv[2],'w')

#=============================================================================
def insertInOrder(sortedlist,num):
    # Given an sorted list (sortedlist), and a number (num), this subroutine
    # will insert the number in ascending order.
    # To achieve heighest possible speed, the program does not check the 
    # sortedlist for its ordering. Careful.
    
    # How it works:
    # The program tries to locate the place to put the number (num) by
    # trying to find smaller and smaller pieces that bound the value (num)
    # Once the piece is small enough, just a brute force search is used.    
    length=len(sortedlist)
    l=1
    r=length-2
    if length<1 or num>=sortedlist[length-1]:
        sortedlist.append(num)
    elif num<=sortedlist[0]:
        sortedlist.insert(0,num)
    else:
        inc=length//8+1
        while inc>3: # Find piece of size about 4*2=8 numbers
            # Find the left horizon
            while l+inc < length-1 and num >= sortedlist[l+inc]: 
                l+=inc 
            if sortedlist[l]==num:
                sortedlist.insert(l,num)
                break
            # Find the right side horizon
            while r-inc > 0 and num <= sortedlist[r-inc]:
                r-=inc
            if sortedlist[r]==num:
                sortedlist.insert(r,num)
                break
            inc=inc//2+1
    # Now, unless the left and right horizon included (num), we still need
    # to insert num. Now the task is much simpler, because we only have about
    # 8 numbers to go through.
    if len(sortedlist)==length:
        i=l
        while num > sortedlist[i]:
                i+=1
        sortedlist.insert(i,num)
    return sortedlist
#=============================================================================

sortedlist=[] # List of numbers- number of unique words in a tweet
numlines=0
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
    insertInOrder(sortedlist,numunique)

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

