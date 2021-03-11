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
