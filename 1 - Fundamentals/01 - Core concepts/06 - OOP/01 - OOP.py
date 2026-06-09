"""
OBJECT-ORIENTED PROGRAMMING (OOP) — Python Fundamentals

OOP is a programming paradigm based on the concept of "objects":
- Objects bundle data (attributes) and behavior (methods)
- Classes are blueprints 5.1 - For creating objects
- OOP improves structure, reusability, and maintainability

Key OOP concepts:
    - Classes
    - Objects (instances)
    - Attributes
    - Methods
    - Encapsulation
    - Inheritance
    - Polymorphism
    - Abstraction

Historical notes:
- OOP ideas began in the 1970s
- Alan Kay (Smalltalk, Xerox PARC) helped popularize the paradigm
- OOP became mainstream in modern languages (Python, Java, C++, etc.)
"""


# ---------------------------------------------------------
# BASIC CLASS & OBJECT
# ---------------------------------------------------------

class Animal:
    """Simple example of a class with attributes and methods."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.name} the {self.species} makes a sound.")

# Creating objects
dog = Animal("Rex", "dog")
cat = Animal("Mia", "cat")

dog.speak()
cat.speak()


# ---------------------------------------------------------
# ENCAPSULATION
# ---------------------------------------------------------
"""
Encapsulation = hiding internal details.
Python uses naming conventions:

    public:    attribute
    protected: _attribute
    private:   __attribute
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Marlon", 1000)
acc.deposit(500)
print(acc.get_balance())


# ---------------------------------------------------------
# INHERITANCE
# ---------------------------------------------------------
"""
Inheritance allows a class to extend another class.
Child classes inherit attributes and methods from the parent.
"""

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Moving...")

class Car(Vehicle):
    def honk(self):
        print("Beep!")

my_car = Car("Toyota")
my_car.move()
my_car.honk()


# ---------------------------------------------------------
# POLYMORPHISM
# ---------------------------------------------------------
"""
Polymorphism = same method name, different behavior.
"""

class Bird:
    def speak(self):
        print("Chirp!")

class Duck(Bird):
    def speak(self):
        print("Quack!")

class Chicken(Bird):
    def speak(self):
        print("Cluck!")

for animal in (Duck(), Chicken()):
    animal.speak()


# ---------------------------------------------------------
# CUSTOM CLASS INHERITING FROM BUILT-IN TYPES
# ---------------------------------------------------------
"""
Example from your notes:
Creating a custom list class that extends Python's built-in list.
"""

class MyList(list):
    """Extended list with convenience methods."""

    def remove_min(self):
        """Remove the smallest element."""
        self.remove(min(self))

    def remove_max(self):
        """Remove the largest element."""
        self.remove(max(self))


# Using normal list
x = [5, 6, 4, 8, 5, 3, 2, 5, 7, 5, 4, 1, 2, 3, 6, 8, 8, 5, 2, 4, 6, 8]
print(min(x))
print(max(x))

# Checking available methods
print(dir(list))
print(dir(MyList))

# Using MyList
y = MyList(x)
print(y)
y.remove_min()
print(y)
y.remove_max()
print(y)


# ---------------------------------------------------------
# CLASS VARIABLES vs INSTANCE VARIABLES
# ---------------------------------------------------------

class Counter:
    count = 0   # class variable (shared)

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print(Counter.count)   # 2


# ---------------------------------------------------------
# STATICMETHOD & CLASSMETHOD
# ---------------------------------------------------------

class MathTools:

    @staticmethod
    def square(n):
        return n * n

    @classmethod
    def description(cls):
        return f"This is the {cls.__name__} class."

print(MathTools.square(5))
print(MathTools.description())


# ---------------------------------------------------------
# MAGIC METHODS (DUNDER METHODS)
# ---------------------------------------------------------
"""
Magic methods allow custom behavior 5.1 - For built-in operations.
Examples:
    __str__   → string representation
    __len__   → len(obj)
    __add__   → obj1 + obj2
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 1)
print(p1)
print(p1 + p2)


# ---------------------------------------------------------
# GOOD PRACTICES
# ---------------------------------------------------------
"""
✔ Use clear, descriptive class names (CamelCase)
✔ Keep methods small and focused
✔ Prefer composition over inheritance when possible
✔ Use docstrings 5.1 - For classes and methods
✔ Avoid exposing internal attributes (use _ or __)
✔ Keep classes cohesive — one responsibility per class
"""
