"""using predefined functions"""
from random import randrange
import numpy as np
from scipy import stats

n=randrange(10,2501)
array=np.random.randint(10001, size=n)
array=np.sort(array)
mean=round(np.mean(array),1)
median=round(np.median(array),1)
mode=stats.mode(array)[0][0]
print(mean)
print(median)
print(mode)

"""using test cases"""
from random import randrange
import numpy as np
from collections import defaultdict
n=randrange(10,2501)
array=np.random.randint(10001, size=n)
array=np.sort(array)
lg=len(array)
mean=round(sum(array)/lg,1)


if lg%2==0:
  median=round((array[lg/2]+array[lg/2-1])/2,1)
else:
  median=array[round(lg/2)]
  
unique, counts = np.unique(array, return_counts=True)
mode=unique[np.argmax(counts)]

print(mean)
print(median)
print(mode)
