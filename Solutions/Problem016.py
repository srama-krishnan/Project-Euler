'''
QUESTION: What is the sum of the digits of the number 2^1000?

ANSWER: 1366

EXPLANATION: The number 2^1000 is calculated and stored as a string.
The sum of the digits of the number is then calculated by iterating 
through the string and summing the digits.

'''

x = str(2**1000)
sum = 0
for i in x:
    sum+=int(i)
print(sum)