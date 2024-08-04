'''
QUESTION : 
    If we list all the natural numbers below 10 
    that are multiples of 3 or 5, we get 
    3,5,6 and 9.The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 
    below 1000.

ANSWER : 233168

EXPLANATION: 
    Loop through the numbers below 1000
    and add the number if it is divisible
    by either 5 or 3.
    
'''
#CODE - QUESTION 1 (PYTHON)
summation = 0
for i in range(1,1000):
    if (i%5==0 or i%3==0):
        summation+=i
print(summation)    