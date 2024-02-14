'''
# LARGEST PALINDROME PRODUCT (004)

QUESTION : A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers 
    is 9009 = 91 * 99. Find the largest palindrome made from
    the product of two 3-digit numbers.

ANSWER : 906609

EXPLANATION : It uses nested loops to iterate over three-digit 
            numbers in reverse order, multiplies them, converts 
            the result to a string, and checks if it reads the same 
            backward as forward. When a palindrome is found, the loop breaks.
'''

def palindrome_3():
    for i in range(999,900,-1):
        for j in range(999,900,-1):
            x = str(i*j)
            if x[0]==x[-1] and x[1]==x[-2] and x[2]==x[-3] :
                break
    print(x)
palindrome_3()
