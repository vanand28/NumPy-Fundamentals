import numpy as np
                                     #BROADCASTING ALLOWS TO PERFORM ARITHMETIC OPERATIONS ON ARRAYS OF DIFFERENT SHAPES
array1 = np.array([[1,2,3,4],])
array2 = np.array([[5],
                   [6],
                   [7],
                   [8]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)

print(array1 + array2)
