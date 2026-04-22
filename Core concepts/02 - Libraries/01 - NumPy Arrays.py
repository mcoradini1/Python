#NUMPY -----------------------------------------------------------------------------------------------------------------

'''
Numpy is a designed for scientific computation (can generate n-dimensional array objects and can be itegrated with C,
C++, Fortran)

For more information: numpy.org

numpy array: additional data type provided by NumPy. They are used to represent vectors(1d)and matrices(2d+)
by default the elements are floating point numbers (to make it efficient and simpler).
'''

#NP.ZERO----------------------------------------------------------------------------------------------------------------

import numpy as np

zero_vector = np.zeros (5)             #1d array with 5 numbers 0.
zero_matrix = np.zeros ((5,3))         #2d array with 5 rows and 3 columns, filled with numbers 0.

print(zero_vector)
print(zero_matrix)

#np.empty another way to do np.zero, to save computing process (requires care)


#NP.ARRAY(1 DIMENSION)--------------------------------------------------------------------------------------------------
#----------------------------------------------shape and size attributes------------------------------------------------

x = np.array([1,2,3])
y = np.array([2,4,6])
print(x)
print(y)

#shape and size of arrays are data attributes, not methods [method needs ()]
print(f'{x.shape} SHAAPE')
print(f'{x.size} SIZE')

#NP.ARRAY(2 DIMENSION)--------------------------------------------------------------------------------------------------
print('\n\n')
z = np.array([[1,3], [5,9]])
print(z)


#TRANSPOSE -------------------------------------------------------------------------------------------------------------
print('\n\n')
z1 = z.transpose()
print(z1)

#transpose matrix (first row become first column) (second row become second column)


#SLICING 1 DIMENSION ---------------------------------------------------------------------------------------------------

print('\nSLICING ONE DIMENSION')
print(x[0])
print(x[0:2])
a = x + y
print(f'{x} + {y} = {a}')


#SLICING TWO DIMENSION COLUMNS------------------------------------------------------------------------------------------

x2 = np.array([[1,2,3], [4,5,6]])
y2 = np.array([[2,4,6], [8,10,12]])


print('\nSLICING TWO DIMENSION - COLUMNS')
print(x2[:,1])   #get all numbers from column 1 (0 is the first column)
print(y2[:,1])   # get all number from column 1 (0 is the first column)
print(x2[:,1] + y2[:,1])   #sum them together term by term

#SLICING TWO DIMENSION ROWS --------------------------------------------------------------------------------------------

print('\nSLICING TWO DIMENSION - ROWS')
print(x2[1,:])
#print(x2[1,:]) = print(x2[1])
print(y2[1,:])
print(x2[1,:] + y2[1,:])


#INDEXING --------------------------------------------------------------------------------------------------------------
#Can be done by the use of LISTS or ARRAYS
print('\nINDEXING')

index_array = np.array([0,2,3])
index_list = [0,2,3]


z1 = np.array([1,3,5,7,9])
z2 = z1 + 1

print(z1[index_array]) #Both will give me the term 0,2,3 of Z1
print(z1[index_list])

print(z1 > 6)     #Show True or False each term

print(z1[z1>6])    #Show just the TRUE terms of Z1

z3 = z1 > 6     #[False False False  True  True]
z4 = np.array([8,16,32,33,0])

print(z1[z3])   #[7 9]
print(z2[z3])   #[8 10]
print('8: ',z4[z3])  #[33  0]

#When z3 is created it will be a boolean array, the examples bellow demonstrate that it will always show terms 3 and 4
# (no matter the value there)

#COPYING ---------------------------------------------------------------------------------------------------------------
#To work with arrays it's important to note that different from lists slicing will create a bond between them,
# to sort it out we use INDEXING.

#INCORRECTLY -----------------------------------------------------------------------------------------------------------
print(z1)
w = z1[0:3]
w[0] = 8
print(w)
print(z1)

#CORRECTLY -------------------------------------------------------------------------------------------------------------

index_z1 = [0,1,2]  #could do by np.array([0,1,2])
w = z1[index_z1]
w[0] = 43
print(w)
print(z1)



#LINSPACE --------------------------------------------------------------------------------------------------------------
np.linspace(0,100,10) #first, end and how many in the array. (ill create an array linearly spaced...


#LOGSPACE --------------------------------------------------------------------------------------------------------------
np.logspace(1,2,10) #log of the starting point (log of 10 is 1, log of 100 is 2,   we want 10 elements

#LOGSPACE SPECIF LOG BASE ----------------------------------------------------------------------------------------------
print(np.logspace(np.log10(250),np.log10(500),10))


#RANDOM ARRAYS ---------------------------------------------------------------------------------------------------------
#.any()
#.all()

random_np = np.random.random(10)
print('\n\n', random_np)
print(np.any(random_np>0.9))
print(np.all(random_np>=0.1))

