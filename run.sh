#! /bin/bash

# This script calls the two python functions to find word frequency
# and median number of unique words in a tweet.
# Right now the algorithm scales as n
# The third and fourth items are the input and output files, viz:
# python python_script.py input_file output_file



res1=$(date +%s.%N)


#inputfile='./bup/tweets.txt'
inputfile='./tweet_input/tweets.txt'
output1='./tweet_output/ft1.txt'
output2='./tweet_output/ft2.txt'

# One for finding tweeted word frequency
python ./src/words_tweeted.py $inputfile $output1 >> err1.log
res2=$(date +%s.%N)
echo "Elapsed1:    $(echo "$res2 - $res1"|bc )"
echo "Frequency of words in: $output1"
echo "Log file in err1.log"


# One for finding statistics of tweets
python ./src/median_unique.py $inputfile $output2  >> err2.log
res3=$(date +%s.%N)
echo "Elapsed2:    $(echo "$res3 - $res2"|bc )"
echo "Median number of unique words per tweet in:  $output2"
echo "Log file in err2.log"
