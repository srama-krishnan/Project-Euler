'''
QUESTION : By listing the first six prime numbers: 
    2,3,5,7,11, and 13, we can see that the 6th prime is 13.
    What is the 10,001st prime number?

ANSWER : 104743

EXPLANATION : It iterates through odd numbers starting from 1, 
    checks each number for primality by dividing it only by odd numbers 
    up to its square root, and counts the prime numbers. When it reaches 
    the 10,001st prime, it prints the result and breaks out of the loop. 
    The algorithm optimizes by skipping even numbers other than 2 and 
    efficiently identifies prime numbers in the given range.
'''
import time
start = time.time()
count = 0
for Var1 in range(1,1100000,2):
    flag = True
    for Var2 in range (3,(Var1//2)+1,2):
        if Var1%Var2 == 0:
           flag = False
           break
    if flag:
       count+=1
    if count==10001:
        print(Var1)
        break
print(time.time() - start)
