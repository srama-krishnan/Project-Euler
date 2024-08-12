'''
QUESTION: n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 27.
Find the sum of the digits in the number 100!

ANSWER: 648

EXPLANATION: The factorial of 100 is calculated using the math module.
The sum of the digits is calculated by taking the modulo of 10 and
dividing by 10 until the number is 0.

'''

import math
def factorial_sum(n):
    k = (math.factorial(n))
    sum1 = 0
    while k>0:
        sum1+=k%10
        k = k//10
    print("Sum : ",sum1)
factorial_sum(100)
