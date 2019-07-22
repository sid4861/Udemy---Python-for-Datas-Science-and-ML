import numpy as np

############### numpy arrays ################

my_list = [1,2,3,4,5]
print(np.array(my_list))

my_mat = [[1,2,3], [4,5,6], [7,8,9]]
print(np.array(my_mat))

print(np.arange(0,10))
print(np.arange(1,11,2))

print(np.zeros(5))
print(np.zeros((3,3)))

print(np.ones(5))
print(np.ones((3,3)))

print(np.eye(3))

print(np.linspace(0,2,5))


############### numpy random numbers ################

#uniform distribution between 0 and 1

print(np.random.rand(5))
print(np.random.rand(3,3))

#normal distribution around 0

print(np.random.randn(5))
print(np.random.randn(3,3))

#between integers

print(np.random.randint(1,100)) #one number
print(np.random.randint(1,100,5)) #5 numbers

#reshape

arr = np.arange(25)
print(arr)
print(arr.reshape(5,5))
print(arr)

randarr = np.random.randint(1,100,10)

print(randarr)
print(randarr.max())
print(randarr.min())
print(randarr.argmax())
print(randarr.argmin())
randarr = randarr.reshape(2,5)
print(randarr.shape)
print(randarr.dtype)
print(randarr)


############### numpy array indexing and selection ################

print("\n\n\n\n")
arr = np.arange(11)
print(arr[:])
print(arr[0:8])
print(arr[:6])
print(arr[1:8])

"""
    SLICING AN ARRAY REFERS TO THE ORIGINAL ARRAY, USE .copy() METHOD
    FOR WORKING ON COPY
"""

arr_slice = arr[1:6]
print(arr)
arr_slice[:] = 100
print(arr_slice)
print(arr)
print('\n\n\n\n')
arr = np.arange(11)
arr_slice = arr[1:6].copy()
arr_slice[:] = 100
print(arr_slice)
print(arr)

# indexing 2D arrays
print("\n\n\n\n")
arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr_2d)

print(arr_2d[1][1])
print(arr_2d[2][1])
print(arr_2d[1][2])
print(arr_2d[0][2])

print(arr_2d[0, 2])
print(arr_2d[1,1])
print(arr_2d[2,0])
print("\n\n\n\n")
print(arr_2d[0:2, 1:])
print(arr_2d[1:, 1:])
print(arr_2d[1:])
print(arr_2d[:, 0:2])
print(arr_2d[:, 1:])
print("\n\n\n\n")
arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)

print(arr_2d[1:3, 5:7])
print(arr_2d[1:4, 2:5])

arr = np.arange(1,11)
print(arr[arr>5])


############### numpy operations ################

arr = np.arange(11)
print(arr)
print(arr+arr)
print(arr+10)
print(arr-arr)
print(arr-10)
print(arr/arr)
print(arr/0)


