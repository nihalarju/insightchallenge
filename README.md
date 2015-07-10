
How to run the program:

Open terminal
Go to the root directory (the directory in which this file is in.)
Type "chmod +x run.sh", without the quotes, press enter
Type "./run.sh", without the quotes, press enter

The run.sh file calls two python scripts: words_tweeted.py and median_unique.py.

The words_tweeted.py file creates an alphabetically sorted frequency table of words at tweet_output/ft1.txt

The median_unique.py file creates a rolling list of median number of unique words in a tweet at tweet_output/ft2.txt

The median_unique.py does not use the built-in (numpy) median function because there is a much faster way to do this. Here the number of unique words is populated in ascending order, and then the median is calculated using just the middle number(or two middle numbers). 

This method is about 5 times faster than built in median function.

