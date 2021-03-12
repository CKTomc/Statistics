# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
n=int(input())
while n<5 or n>50:
    n=int(input())

array=[int(x) for x in input().split()[:n]]
array.sort()

def median(array):
    lg=len(array)
    if lg%2==0:
       return int((array[int(lg/2)]+array[int(lg/2)-1])/2)
    else:
       return array[int(lg/2)]
    
q2=median(array)
q1=median(array[:int(n/2)])
if n%2==0:
    q3=median(array[int(n/2):])
else:
    q3=median(array[int(n/2)+1:])
print(q1)
print(q2)
print(q3)
