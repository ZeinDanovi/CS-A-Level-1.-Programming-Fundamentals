import numpy as np
import sys 

# create sample 32x32 pressure sensor data, stored in a numpy array 
array1 = np.random.randint(0,100, size= (32,32))

# allows array to be printed to terminal
np.set_printoptions(threshold=sys.maxsize)
print(np.array2string(array1, max_line_width= np.inf))


dataFrequency = np.size(array1)
dataSum = np.sum(array1)
dataMean = np.mean(array1)
dataVar = np.var(array1)
dataStd = np.std(array1)
dataCV = dataStd/dataMean 

print(f"the frequency of data points is {dataFrequency}")
print(f"the sum of the data is {dataSum}" )
print(f"the mean of the data is therefore {dataMean} ")
print(f"the variance of the data is {dataVar}")
print(f"the standard deviation of the data is {dataStd}")
print(f"the data Coefficient of variation is {dataCV}")
