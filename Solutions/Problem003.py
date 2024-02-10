'''
QUESTION : The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

ANSWER : 6857

EXPLANATION : Using the logic that the largest Prime factor 
is always lesser tan the Square root of given Number.
'''


import time
start = time.time()
Number,count = 600851475143,0
Upper_limit = int((Number)**(0.5))
Factor_List , Prime_List = [ ] , [ ]
for i in range(1,Upper_limit):
    if Number%i ==0:
        for j in range(1,i+1):
            if i%j ==0:
                count+=1
        if count ==2:
            Prime_List.append(i)
        count=0   
print(max(Prime_List))    
print(time.time()-start)
