import numpy as np                                                                    #IMPORTING THE NUMPY LIBRARY TO USE IT IN THE CODE

array3 = np.array([[['A', 'B'], ['C', 'D'], ['E', 'F']],
                   [['G', 'H'], ['I', 'J'], ['K', 'L']],
                   [['M', 'N'], ['O', 'P'], ['Q', 'R']],
                   [['S', 'T'], ['U', 'V'], ['W', 'X']]])

india = array3[1,1,0] + array3[2,0,1] + array3[0,1,1] + array3[1,1,0] + array3[0,0,0]
print(india)

print(array3[3][0][1])                                                                 #CHAIN INDEXING

print(array3[2,1,0])                                                                   #MULTIDIMENSIONAL INDEXING

canada = array3[0,1,0] + array3[0,0,0] + array3[2,0,1] + array3[0,0,0] + array3[0,1,1] + array3[0,0,0]
print(canada)