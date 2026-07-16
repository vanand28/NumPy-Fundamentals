import numpy as np

array = np.array([[1,2,3,4,5],                              #DEFINING A 2D ARRAY
                  [6,7,8,9,10]])

print(np.min(array))                                        #MINIMUM VALUE FROM THE ARRAY
print(np.argmin(array))                                     #INDEX OF THE MIN VALUE
print(np.max(array))                                        #MAXIMUM VALUE FROM THE ARRAY
print(np.argmax(array))                                     #INDEX OF THE MAX VALUE
print(np.sum(array))                                        #SUM OF ALL THE VALUE FROM THE ARRAY
print(np.mean(array))                                       #MEAN VALUE OF THE NUMBERS FROM THE ARRAY
print(np.std(array))                                        #STANDARD DEVIATION OF THE NUMBERS FROM THE ARRAY
print(np.var(array))                                        #VARIANCE OF THE NUMBERS FROM THE ARRAY

print(np.sum(array, axis=0))                                #ADDING THE NUMBERS COLUMNS-WISE
print(np.sum(array, axis=1))                                #ADDING THE NUMBERS ROW-WISE