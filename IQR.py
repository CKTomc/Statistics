import sys
n=int(input())
while n<5 or n>50:
    n=int(input())

array=[int(x) for x in input().split()[:n]]
freq=[int(x) for x in input().split()[:n]]
for i,f in enumerate(freq):
    array.extend([array[i]]*(f-1))
array.sort()
lg=len(array)
def median(array):
    lg=len(array)
    if lg%2==0:
       return float(array[int(lg/2)]+array[int(lg/2)-1])/2
    else:
       return float(array[int(lg/2)])
    
q1=median(array[:int(lg/2)])
if lg%2==0:
    q3=median(array[int(lg/2):])
else:
    q3=median(array[int(lg/2)+1:])

print(q3-q1)
