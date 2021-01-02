import numpy as np
import pandas as pd
import seaborn as ss

min=1
max=77
step=3
arr=np.array(min,max,step)

linspsize=10
arr2=np.linspace(min,max,linspsize)

arr3=np.random.rand(5,5) #shape -> (5,5)
arr4=np.random.randn(5,5) #normal
arr5=np.diag(arr4) # main diag
arr6=np.diag(arr4,1) # 1st superior diag
arr7=np.diag(arr4,-1) # 1st inferior diag

data=pd.read_csv(<location>,head=0)
data.describe() # picks numerical columns
data.iloc[2] #3d line using index
data.loc[<anid>] #line infos using unique info
data.iloc[0:4] 
