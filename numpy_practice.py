import numpy as np

my_list = np.array([1,2,3,5])
print(my_list)
my_list = my_list * 3
print(my_list)
my_list3 = np.array('Akshay')
# No. of dimensions i.e ndim
print(my_list3.ndim)
# 2 dimensional array
my_list4 = np.array([['A','B','C'],
                     ['D','E','F'],
                     ['G','H','I']])
print(my_list4.ndim)
print(my_list4.shape)
print(my_list4[2,0])
print(my_list4[::-1])
# 3 dimensional array
my_list5 = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                      [['J','K','L'],['M','N','O'],['P','Q','R']],
                      [['S','T','U'],['V','W','X'],['Y','Z',' ']]])
print(my_list5.shape)

# Chain Indexing
print(my_list5[0][2][2])
# Multidimensional indexing
print(my_list5[0,2,2])
# Slicing
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [12,14,15,16]])
# array [start:stop:step]
print(array[::3])
# accessing columns
print(array[:,1:4])
# column reverse
print(array[:,::-1])
print(array[0:2,0:2])


# Scalar Arithmetic
array2 = np.array([1,2,3,4])
print(array2 ** 5)
print(array2 % 2)
print(array2 / 2)
#Vectorized math funcs
radius = np.array([1,2,3])
print(np.pi * radius ** 2)

# Element-wise arithmetic
array4 = np.array([5,8,9])
array5 = np.array([2,99,3])
print(array4 + array5)
print(array5 - array4)
print(array4 ** array5)

# Comparison operators
scores = np.array([91,3,5,7,12])
print(scores >= 50)
scores[scores != 5] = 12
print(scores)

# broadcasting


 






