#problem 1
import numpy as np # NUMPY BCZ IT IS USED TO MATH OPERATION
import matplotlib.pyplot as plt

# DOT PRODUCT
a = np.array([1,2,3])
b = np.array([4,5,6])
dot = np.dot(a,b)
print("dot poroduct:", dot,"\n") # Output of dot product

# MATRIX MULTIPLAICATON 
A = np.array([[1,2],[3,4]])  
B = np.array([[5,6],[7,8]])
c = np.matmul(A,B)
print(c,"\n") # Output of MATRIX MULTIPLAICATON

# NORMALIZATION 
data = np.array([10,20,30,40,50])
normalization = (data - np.min(data))/(np.max(data) - np.min(data))
print(normalization,"\n") # Output of NORMALIZATION
