'''
QUESTION: Starting in the top left corner of a 2 x 2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a grid?

ANSWER: 137846528820

EXPLANATION: Non-programmatic Approach Using Combinatorics:
The objective is to determine the number of ways to choose 20 steps out of a 
total of 40 steps. This corresponds to a binomial coefficient calculation, 
expressed as 40!/(20!)^2. The problem is thus reduced to simple arithmatic. 

'''

import math
n = 20
print(math.factorial(2*n)//(math.factorial(n)**2))