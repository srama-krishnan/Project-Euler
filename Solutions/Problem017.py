'''
QUESTION: If all the numbers 1 to 1000 (inclusive) were written out in words, 
how many letters would be used?

ANSWER: 21124

EXPLANATION: The numbers 1 to 19 are stored in a list. The numbers 20 to 99 are
calculated by concatenating the tens place with the ones place. The numbers 100 to 999
are calculated by concatenating the hundreds place with the tens place and ones place.
The sum of the lengths of the numbers 1 to 999 is calculated. The length of the word "and"
is added to the sum. The length of the word "OneThousand" is added to the sum. The final sum
is printed.
'''


lst1 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
        'twelve', 'thirteen','fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
lst3 = ["","Hundred"]
def lc(str1):
    c = 0
    for i in str1:
        c = c+1
    return c
def itw1():
    s2 = s1 = 0
    for i in range(1,100):
        if i<20:
            s1 = s1+lc(lst1[i])
        if 19<i<30:
            x = "Twenty"+lst1[i-20]
            s2 = s2+lc(x)
        if 29<i<40:
            x = "Thirty"+lst1[i-30]
            s2 = s2+lc(x)        
        if 39<i<50:
            x = "Forty"+lst1[i-40]
            s2 = s2+lc(x)        
        if 49<i<60:
            x = "Fifty"+lst1[i-50]
            s2 = s2+lc(x)        
        if 59<i<70:
            x = "Sixty"+lst1[i-60]
            s2 = s2+lc(x)        
        if 69<i<80:
            x = "Seventy"+lst1[i-70]
            s2 = s2+lc(x)        
        if 79<i<90:
            x = "Eighty"+lst1[i-80]
            s2 = s2+lc(x)
        if 89<i<100:
            x = "Ninety"+lst1[i-90]
            s2 = s2+lc(x)        
    return s1+s2
k = lc("Hundred")
result=0
for i in range(1,10):
    result+=100*(k+lc(lst1[i]))+854
print(result+854+891*lc("and")+lc("OneThousand"))