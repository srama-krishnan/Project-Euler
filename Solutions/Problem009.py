'''
QUESTION : A Pythagorean triplet is a set of three natural numbers, a < b < c, 
        for which, a^2 + b^2 = c^2
        For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2. There exists exactly one Pythagorean triplet
        for which a + b + c = 1000. Find the product abc.

ANSWER : 31875000

EXPLANATION : The code iterates through ranges for a, b, and c, 
    checking if they form a Pythagorean triplet and if their sum equals 1000. 
    Once found, it calculates the product of a, b, and c. The final product is printed.
'''
import time
start = time.time()
def pyth_trip(a,b,c):
    return a**2 + b**2 == c**2
prod = 1
for a in range(200,400):
    for b in range(200,400):
        for c in range(400,500):
            if pyth_trip(a,b,c):
                if a+b+c == 1000:
                    prod = a*b*c
                    break
print(prod)
print(time.time() - start)
