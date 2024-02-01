'''
QUESTION :  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

ANSWER : 232792560

EXPLANATION : It uses a simple approach by iterating through multiples of 
a common multiple of the numbers 20 and 19 (Larger step size and product must be a factor)
and checking for divisibility. The code efficiently breaks the loop when a non-divisible 
case is encountered. It calculates and prints the result.

'''


import time
start = time.time()
n = 20

def maxp(n):
    p = 1
    for i in range(1,n+1):
        p = p*i
    return p

maxval = maxp(n)
lst = [i for i in range(1,21)]

def lcm(n):
    counter = 0
    for i in range(380,maxval,20*19):
        for j in lst:
            if i%j==0:
                counter = counter + 1
            else:
                break
        if counter == n:
            print(i)
            break
        else:
            counter = 0
lcm(n)
print(time.time() - start)