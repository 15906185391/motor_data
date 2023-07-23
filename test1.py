import numpy as np
import pandas as pd
file_name=str(7)+'.csv'
# data_ = np.loadtxt(file_name, dtype=str, delimiter=',')
data_ = pd.read_csv('7.csv', encoding='gb2312',delimiter=',',skiprows=1)
print(data_)
data_ =data_.to_numpy()
data = np.asarray(data_[0:(20*f), 0], dtype=float)
effective_value=np.sqrt(np.mean(data**2))
print(effective_value)