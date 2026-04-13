# 10 April
import numpy as np

# 1D Array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# 2D Array
arr_2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(arr_2d)

# Array using tuple
tup1 = (100, 90, 80, 70, 60)
arr_tup1 = np.array(tup1)
print(arr_tup1)

# Forward Indexing
print("Element at row 0, column 1:", arr_2d[0][1])

#Backward Indexing
print("Last element:", arr_2d[-1][-1])

# Slicing in 2D
print("First two rows:\n", arr_2d[0:2])

print("First two columns:\n", arr_2d[:, 0:2])

print("Sub array:\n", arr_2d[1:2, 1:3])