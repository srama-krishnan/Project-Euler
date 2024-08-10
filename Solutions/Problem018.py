'''
QUESTION: Find the maximum total from top to bottom of the triangle below

ANSWER: 1074

EXPLANATION: The input string is split into a list of numbers. 
The list is then split into a list of lists. The maximum total is calculated by 
adding the maximum of the two numbers above the current number to the current number.
The maximum total of the last list is printed.

'''

import re
input_string = """75
95 64
17 47 82
18 35 87 10
20 4 82 47 65
19 1 23 75 3 34
88 2 77 73 7 63 67
99 65 4 28 6 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 4 68 89 53 67 30 73 16 69 87 40 31
4 62 98 27 23 9 70 98 73 93 38 53 60 4 23"""

numbers = list(map(int, re.findall(r'\d+', input_string)))
ls = []
start = 0
for i in range(1, len(numbers)+1):
    if i*(i+1)//2 == len(numbers[:i*(i+1)//2]):
        ls.append(numbers[start:i*(i+1)//2])
        start = i*(i+1)//2

for i in range(1,len(ls)):
    for j in range(len(ls[i])):
        if j==0:
            ls[i][j]+=ls[i-1][j]
        elif j==len(ls[i])-1:
            ls[i][j]+=ls[i-1][j-1]
        else:
            ls[i][j]+=max(ls[i-1][j-1],ls[i-1][j])
print(max(ls[-1]))