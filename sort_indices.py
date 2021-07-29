import numpy as np

arr = np.array([1, 1, 0, 5, 2, 9, 7])

arr_upd = np.argsort(arr)
print ("indices in a rising order: ", arr_upd)