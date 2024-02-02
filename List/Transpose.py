"""================================================
Created by 
        Shanmugam Machaa[15/07/2023-21:42]
================================================
"""
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# Transpose using loop
tmatrix = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(3):
    for j in range(3):
        tmatrix[j][i] = matrix[i][j]
print(tmatrix)

# Transpose using one list comprehension
tmatrix = []
for i in range(3):
    tmatrix.append([row[i] for row in matrix]) 
print(tmatrix)

# Transpose using list comprehension
tmatrix = [[row[i] for row in matrix]for i in range(3)]
print(tmatrix)