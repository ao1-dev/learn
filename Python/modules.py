# Modules - import code from other files / libs

# Whole module
import math
print(math.sqrt(16))
print(math.pi)

# Rename
import random as rnd # short for random
print(rnd.randint(1, 6))

# Import only what you need
from datetime import date
print(date.today())

# Your own file - classes.py in the same folder
import classes

ao = classes.Person("ao", 20)
ao.greet()

from classes import Employee
emp = Employee("Hedda", 19, "Sales")
emp.greet()

# See what a module contains
print(dir(math)[:8])



###
class Person:
    pass

class Employee(Person):
    pass

if __name__ == "__main__":
    ao = Person("ao", 20)
    hedda = Person("hedda", 19)
###