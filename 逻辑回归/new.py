import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,KFold
table=pd.DataFrame(index=range(4),columns=['A','B'])
table['A']=[1,2,3,4]
table['B']=[6,7,8,9]
#print(table)
fold=KFold(n_splits=4)
for interation,indices in enumerate(fold.split(table),start=1):
    print(indices[0])
