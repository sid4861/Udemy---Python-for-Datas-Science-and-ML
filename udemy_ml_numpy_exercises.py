import numpy as np

arr = np.zeros(10)
print(arr)
arr_ones = np.ones(10)
print(arr_ones)
arr_fives = np.ones(10)*5
print(arr_fives)

arr_integers = np.arange(10,51)
print(arr_integers)

arr_0to8 = np.arange(9).reshape(3,3)
print(arr_0to8)

print(np.random.rand(1))
print(np.linspace(0,1,100).reshape(10,10))
print("/n/n/n/n")

mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat[2:, 1:])
print(mat[3,4])
print("\n\n")
print(mat[0:3, 1].reshape(3,1))
print(mat[4])
print(mat[3:])
print("\n\n\n\n")
print("sum is = {}".format(np.sum(mat)))
print("SD is = {}".format(np.std(mat)))
print(mat.sum(axis=0))

