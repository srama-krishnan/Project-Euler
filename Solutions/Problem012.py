'''
QUESTION: What is the value of the first triangle number to have over five hundred divisors?

ANSWER: 76576500

EXPLANATION: This code finds the first triangular number 
with more than 500 divisors by generating triangular numbers 
in a loop and checking their divisor counts using a helper function.
'''

import math,time
start = time.time()
def factors(n):
    c = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            if n/i != i:
                c = c+2
                continue
            c = c+1
    return c
x,y=1,2
while(True):
    x += y
    if factors(x) >500:
        print (x)
        break
    y+=1
print (time.time()-start)