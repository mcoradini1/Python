import numpy as np

# NumPy Random Random --------------------------------------------------------------------------------------------------
np.random.random(5) #generate 1d array with 5 randoms

np.random.random((5,5)) #generate a 2d array full of randoms

# NumPy Random Normal --------------------------------------------------------------------------------------------------

#np.random.normal(a,b,x)
#a = mean = 0 (usual)
#b = standard deviation = 1 (normal distribution)
#x = array (for more than 1d it's necessary to use x as a tuple)

np.random.normal(0,1, 5) # will generate a vector of 5 randoms with normal mean and normal distribution

np.random.normal(0,1, (2,5))# will generate a 2d matrix with 2 rows and 5 columns. (same config as above)


# NumPy Random Integer -------------------------------------------------------------------------------------------------
x = np.random.randint(1,7, (10,3))
print(x)
print(x.shape)

# NumPy Sum ------------------------------------------------------------------------------------------------------------
#np.sum(array, axis = x)
#x = 0 (first term) = Rows
#x = 1 (second term) = Columns
#x = 2+ (cases of arrays with more dimensions)

print('array sum:',np.sum(x))
print('rows sum:',np.sum(x, axis=0)) # sum of all rows of the array
print('columns sum:',np.sum(x, axis=1)) #2 sum of all columns array



