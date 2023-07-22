import numpy as np
import pandas as pd
import math

frequency=1024
effective=[]
for i in range(6):
    print(i+1)
    file_name=str(i+1)+'.csv'
    # data_ = np.loadtxt(file_name, dtype=str, delimiter=',')
    data_ = pd.read_csv(file_name, encoding='gb2312',skiprows=4,low_memory=False)
    print(data_)
    data_ =data_.to_numpy()
    data = np.asarray(data_[:, 0], dtype=float)
    effective_value=np.sqrt(np.mean(data**2))
    print(effective_value)
    effective.append(effective_value)

print(effective)