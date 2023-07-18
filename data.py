import csv
import numpy as np
with open('0.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# data=np.loadtxt('0.csv',skiprows=5,dtype=str)
# data=np.frombuffer(data,dtype=float)
# print(data)