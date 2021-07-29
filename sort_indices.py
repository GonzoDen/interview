#show the indeces of the sorted array in a rising order
## print the sorted array

import numpy as np

arr = np.array([1, 1, 0, 5, 2, 9, 7])

arr_upd = np.argsort(arr)
print("indices in a rising order: ", arr_upd)

print("sorted array: ", arr[arr_upd])