'''
QUESTION: Find the sum of all the positive integers which cannot 
be written as the sum of two abundant numbers.

ANSWER: 417987

EXPLANATION: The first step is to find all the abundant numbers.
An abundant number is a number whose sum of factors is greater than
the number itself. The next step is to find all the numbers that can
be written as the sum of two abundant numbers. The numbers that cannot
be written as the sum of two abundant numbers are the numbers that we
are looking for. 

'''

from collections import defaultdict
import math
def facsum(num):
    if num==1:
        return 1
    n = math.ceil(math.sqrt(num))
    total = 1
    divisor = 2
    while (divisor < n):
        if (num%divisor == 0):
            total += divisor
            total += num//divisor
        divisor+=1
    if n**2==num:
        total+=n
    return total
ls = []
for i in range(12,28124):
    x = facsum(i)
    if x>i:
        ls.append(i)
d = defaultdict(int)
for i in range(len(ls)):
    for j in range(i,len(ls)):
        d[ls[i]+ls[j]]+=1
c = 0
for i in range(1,28124):
    if d[i]==0:
        c+=i
print(c)