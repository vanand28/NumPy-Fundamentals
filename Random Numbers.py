import numpy as np

randomIntegers = np.random.default_rng(seed=0)                                  #GENERATING RANDOM INTEGERS
print(randomIntegers.integers(low=0, high=10, size=(3,3)))

randomFloat = np.random.uniform(low=-2.5, high=4.3, size=3)                     #GENERATING RANDOM FLOAT NUMBERS
print(randomFloat)

rng = np.random.default_rng()

numbers = np.array([1,2,3,4,5])                                                 #SHUFFLING THE NUMBERS WITHIN THE ARRAY
rng.shuffle(numbers)
print(numbers)

fruits = np.array(["apple", "banana", "cherry", "kiwi", "mango", "pineapple", "peach", "grape"])
fruit = rng.choice(fruits, size=2)                                              #RANDOM CHOICE MAKER
print(fruit)