'''
Problem 10:
QUESTION: 
Summation of Primes - The sum of the primes below 10 is 2+3+5+7 = 17 
Find the sum of all the primes below two million.
EXPLANATION: Sieve of Eratosthenes is used to find all the prime numbers below 2 million.
'''
import time
start = time.time()
k = [True]*2000000
for i in range(2,2000000):
    if k[i]:
        for j in range(2*i,2000000,i):
            k[j] = False
print(sum([i for i in range(2,2000000) if k[i]]))
print(time.time()-start)
