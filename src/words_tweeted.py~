#! /usr/bin/python

import sys
f=open(sys.argv[1],'r')
fout=open(sys.argv[2],'w')
from collections import OrderedDict

dictt=dict()

for line in f:
    line_dictt=dict() # dictionary of words in a tweet

    # Read a tweet, make list of words
    line=line.strip() # Remove the redundant '\n' etc.
    line_words = line.split(" ") # Make a list of words from the line
    
    # Count frequency of words in a tweet
    # The benefit of doing this is that common words (like `the')
    # won't have to be looked up multiple times for the main list,
    # which is much bigger
    for word in line_words:
        if word in line_dictt:
            line_dictt[word]+=1
        else:
            line_dictt[word]=1

    # Make a new dictt of words with the number of occurances
    for word in line_dictt:
        if word in dictt:
            dictt[word]+=line_dictt[word]
        else:
            dictt[word]=1

    del line_dictt # reset the line dictionary

# Now alphabetically sort the collected dictionary, and write frequency
# of occurance.
word_list = sorted(dictt)
max_len=len(max(word_list, key=len))
for word in word_list:
    (word, ' '*8, str(dictt[word]), '\n')
    fout.write( word + ' '*(max_len-len(word)+6) + str(dictt[word]) + '\n' )

# Clean up
f.close()
fout.close()
