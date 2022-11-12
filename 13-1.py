import numpy as np

import random

 

matrix1 = [ [ random.randint(-100, 100) for j in range(10)] for i in range(10) ]

matrix2 = [ [ random.randint(-100, 100) for j in range(10)] for i in range(10) ]

matrix_sum = [[matrix1[i][j] + matrix2[i][j]  for j in range

(len(matrix1[0]))] for i in range(len(matrix1))]

print(matrix1)

print(matrix2)

print(matrix_sum)