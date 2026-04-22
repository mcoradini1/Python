# (** potency - 4**2 -> four square)
# (// Complete Division)  (% Rest of Division)
# == Equal
## != Different
n = 2
m = 5
o = m**n
o1 = pow(m,n) #another for potency
p = m//n
q = m%n


print('The potency results by method 1 and 2 are: {}, {}\nThe complete division is {}\nThe rest of division is {} ' .format(o,o1,p,q))

#The order will be always (), potency, normal...