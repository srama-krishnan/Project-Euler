'''
QUESTION: What is the millionth lexicographic permutation of the digits 0-9?

ANSWER: 2783915460

EXPLANATION: The itertools module in Python has a permutations function that
generates all the permutations of a given list. The permutations are generated
in lexicographic order. The permutations function returns a generator object
which can be converted to a list. The millionth permutation is the 999999th
permutation since the permutations are zero-indexed. 

'''

from itertools import permutations
ls = [0,1,2,3,4,5,6,7,8,9]
p = permutations(ls,10)
l = []
for i in p:
    l.append(i)
print(l[999999])