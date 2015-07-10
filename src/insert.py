# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 06:21:14 2015

@author: nihal
"""
from numpy import median



newnum=6

n=range(1,6)
print n
medval=median(n)
print("Median", medval)


sortedlist=n
length=len(sortedlist)
if newnum==medval:
    sortedlist.insert( (length)//2, newnum)
else:
    if newnum>medval:
        indices=range(length//2,length)
        for i in indices:
            if newnum<sortedlist[i]:
                sortedlist.insert(i,newnum)
                break
    else:
        indices=range(0,length//2)
        indices.reverse()
        for i in indices:
            if newnum>sortedlist[i]:
                sortedlist.insert(i+1,newnum)
                break


print n
print sortedlist