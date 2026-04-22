#docs.python.org -> tutorials
#what to learn (database access, SQLITE3, Object relational Mapper.

#OOP - OBJECT ORIENTED PROGRAMMING
#OOAD - OBJECT ORIENTED ANALYSIS AND DESIGN
#UML - UNIFIED MODELING LANGUAGE (create later as analysis before start a program to make it better)

#OOP - THEY ARE CALLED OBJECTS:
#Start on 1970 and updated by Alan Curtis Kay with the Dyna-book (that never release), he made the Smalltalk programing
#while working at XEROX, later on the technologies pirates APPLE and MICROSOFT got the idea and made the LAPTOPS.

#SOFTWARE CRISIS ON 1960
#lINEAR PROGRAMMING HAD FORCED GOTO

#REMEMBER THE WORD 'COMER NADA' actually is COMERN.
#CONFIABILITY
#OPPORTUNIST
#MANTAINABLE
#EXTENSIVE
#RE-USABLE
#NATURAL

#BOOKS - IRV KALB OBJET ORIENTED PYTHON MASTER OOP BY BUILDING GAMES AND GUIS

'''HARVARD
CLASSES AND OBJECTS

INHERITANCE - DEFINE A NEW OBJECT THAT CAN INHERIT PROPETTIR FROM AN EXISTING OBJECT

class MyList(list): (name is MyList) (the parenthesis is te inheritance in this case list)
this is a bi like fucntion definition, CLass statment is like a blueprint of the new class, a new type of pythn object
'''

class MyList (list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))



#USING NORMAL LIST
x = [5, 6, 4, 8, 5, 3, 2, 5, 7, 5, 4, 1, 2, 3, 6, 8, 8, 5, 2, 4, 6, 8]
print(min(x))
print(max(x))


#CHECKING
print(dir(list))
print(dir(MyList))

#USING MYLIST
y = MyList(x)
print(y)
y.remove_min()
print(y)
y.remove_max()
print(y)
