#I WILL ATTRIBUTE A VARIABLE

filename = 'test.txt'
for line in open(filename):
    print(line)
    print(line.rstrip())
    line_stored = line.rstrip() #If i want to keep it, I should add it to a variable.

    line_stored_split = line.rstrip().split(" ") #I will use ' ' to determine where it will be split

open('output.txt', 'w')  #telling python i am writing the file (I tipically add it to a variable)

open_variable = open('output.txt', 'w')
open_variable.write("Hello World")
open_variable.close()

#Just Imagine the document bellow.

#First line \n
#Second line \n
#Third line \n

#rstrip method


'''

pwd - Check directory where python will read the document...
pwd -> C:\\Programacao\\Python\\Jupyter Notebooks

cd python_case_studies\
pwd -> C:\\Programacao\\Python\\Jupyter Notebooks\\python_case_studies

cd translation\
pwd -> C:\\Programacao\\Python\\Jupyter Notebooks\\python_case_studies\\translation

'''
