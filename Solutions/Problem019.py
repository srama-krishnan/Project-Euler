'''
QUESTION: How many Sundays fell on the first of the month during 
the twentieth century (1 Jan 1901 to 31 Dec 2000)?

ANSWER: 171

EXPLANATION: The number of days in each month is calculated by 
adding the number of days in each month to the day of the week.

'''
k = 2  
ans = 0
for y in range(1900, 2001):
    for m in range(1, 13):
        if k % 7 == 0 and y > 1900:  
            ans += 1
        if m == 2:
            if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                k += 29 
            else:
                k += 28
        elif m in [4, 6, 9, 11]:
            k += 30
        else:
            k += 31
print(ans)