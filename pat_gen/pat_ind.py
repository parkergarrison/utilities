#!/usr/bin/env python

import sys

def nextperm(s):
    news = ""
    donext=1
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

def a2n(s):
    ''' returns the value of a string in base 26 where the digits are a=0, ..., z=25 '''
    total = 0

    for i in range(len(s)-1, -1, -1):
        exp = len(s)-1 - i
        c = s[i].lower()
        total += (ord(c) - ord('a')) * 26 ** exp

    return total

p = sys.argv[1]


d = 0 # location of the capital letter
for i in range(len(p)):
    if p[i].isupper():
        d = i
        break

#modified p
mp = p[d:] + nextperm(p[:d]) # get the group of 4 starting at the capital letter, regardless of location of capital
ans = 4*a2n(mp) - d # the given string starts d positions to the left of the location of mp

print(ans)

