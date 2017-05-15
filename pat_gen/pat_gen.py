#!/usr/bin/env python

import time
import sys

def nextperm(s):
    ''' takes string of form aaaa and produces next permutation, eg. aazz -> abaa '''

    news = ""
    donext=1 # whether we need to advance the characters
    
    for i in range(len(s)-1, -1, -1):
        if not donext:
            news = s[i] + news
            continue

        if s[i] == 'z':
            news = 'a' + news
        
        else:
            news = chr(ord(s[i])+1) + news
            donext = 0
            continue
    
    return news


le = int(sys.argv[1])
ans = ""

cg = "a"*4 # current permutation
la=0 

while la < le: # generate next 4 characters until required length

    la+=4

    ans += cg[0].upper() + cg[1:]
    cg = nextperm(cg)
    

print ans[:le]
