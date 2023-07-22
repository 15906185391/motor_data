import numpy as np

# data=np.loadtxt('4.csv',skiprows=5,dtype=str,delimiter=',',encoding='GB2312')
data=np.loadtxt('0.csv',dtype=str,skiprows=5,delimiter=',',encoding='GB2312')

print(data)
data=np.asarray(data[:,0],dtype=float)
print(data)
data=np.loadtxt('2.csv',dtype=str,skiprows=5,delimiter=',',encoding='GB2312')

print(data)
data=np.asarray(data[:,0],dtype=float)
print(data)