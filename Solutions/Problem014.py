'''
QUESTION: The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 
Which starting number, under one million, produces the longest chain?

ANSWER: 837799

EXPLANATION: This code uses a defaultdict to store the number of steps 
taken to reach 1 for each number. It then finds the number with the most 
steps and prints it.
'''

from collections import defaultdict
c = 1
d = defaultdict(int)
for i in range(1,1000001):
    n = i
    while n>=1:
        if n%2 != 0:
            n = 3*n+1
            c = c+1
        if n%2 ==0:
            n = n//2
            c= c+1
        if n==1:
             d[i] = c
             c=1
             break
maxsteps=0
for i in list(d.keys()):
    if d[i] > maxsteps:
        result = i
        maxsteps = d[i]
print(result)