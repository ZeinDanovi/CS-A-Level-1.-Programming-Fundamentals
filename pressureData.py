import numpy as np
import sys 

fhand = open("pressureData.txt","w")

array1 = np.random.randint(0,100, size= (32,32))

np.set_printoptions(threshold=sys.maxsize)

print(np.array2string(array1, max_line_width= np.inf))

print(np.sum(array1))
# for i in range(32):
#     array1 = np.random.randint(0,100, size= (32))
#     fhand.write(f"{np.array2string(array1, max_line_width = np.inf)} \n")