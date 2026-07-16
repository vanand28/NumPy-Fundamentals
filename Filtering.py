import numpy as np

ages = np.array([[27, 16, 48, 44, 41, 30, 26, 24, 67, 17],           #SAMPLE DATA SET OF AGES OF 20 PEOPLE
                [16, 24, 40, 42, 77, 16, 38, 66, 41, 70]])

teenagers = ages[ages <= 19]                                         #FILTERING THE AGES INTO THE RESPECTIVE CATEGORIES
adults = ages[(ages > 19) & (ages < 60)]
seniors = ages[ages > 60]

print("Teenagers:",teenagers)                                        #PRINTING THE ARRANGED DATA
print("Adults:",adults)
print("Seniors:",seniors)