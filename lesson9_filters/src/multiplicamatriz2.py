import numpy as np
# Matriz 2x2 A = [1 2
#                 3 4]
A = np.array([[1, 2], [3, 4]])
# Matriz 2x2 B = [-1 3
#                 4 2]
B = np.array([[-1, 3], [4, 2]])

MultMatrizes = np.dot(A,B)
#Elemento a Elemento
Produto = A*B

print(MultMatrizes)
print(Produto)