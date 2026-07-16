import numpy as np

array0 = np.array('A')
print(array0)
print("The shape of the array above is: " + str(array0.shape))
print("It is a " + str(array0.ndim) + "-Dimensional Array\n")

array1 = np.array(['A', 'B', 'C'])
print(array1)
print("The shape of the array above is: " + str(array1.shape))
print("It is a " + str(array1.ndim) + "-Dimensional Array\n")

array2 = np.array([['A', 'B', 'C'],
                  ['D', 'E', 'F'],
                  ['G', 'H', 'I']])
print(array2)
print("The shape of the array above is: " + str(array2.shape))
print("It is a " + str(array2.ndim) + "-Dimensional Array\n")

array3 = np.array([[['A', 'B'],['C', 'D'],['E', 'F']],
                   [['G', 'H'],['I', 'J'],['K', 'L']],
                   [['M', 'N'], ['O', 'P'], ['Q', 'R']]])
print(array3)
print("The shape of the array above is: " + str(array3.shape))
print("It is a " + str(array3.ndim) + "-Dimensional Array\n")
