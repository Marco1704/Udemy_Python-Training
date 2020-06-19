import numpy as np

'''arr = np.arange(0,11)

slice_of_arr = arr[0:6]

slice_of_arr[:] = 99

print(arr)

note = if you alter the slice of the array it will alter the original array
to prevent the modification you should create a copy of the array

e.g. arr_copy = arr.copy()

'''

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))

arr_2d[:2,1:] # index slicing

arr_2d[2] #slicing a row

arr2d = np.zeros([10,10])
arr_length = arr2d.shape[1]

for i in range(arr_length):
    arr2d[i]=i

arr2d[[2,4,6,8]]




print(arr2d[[2,4,6,8]])