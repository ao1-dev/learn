# Classes - class, self, objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, i am {self.name}")

    def is_adult(self):
        return self.age >= 18

    def birthday(self):
        self.age += 1

# Create objevts (instances)
alex = Person("Alex", 20)
hedda = Person("Hedda", 19)

alex.greet()
hedda.greet()

hedda.birthday()
print(hedda.age)

# Many objevts in a list
people = [alex, hedda, Person("ao", 15)]

for p in people:
    if p.is_adult():
        print(f"{p.name} is an adult")
    else:
        print(f"{p.name} is a minor")

# Inheritance - reuse and extend a class
class Employee(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def greet(self):
        print(f"Hello, I am {self.name}, I work as {self.job}")

emp = Employee("Alex", 20, "freelancer")
emp.greet()
print(emp.is_adult()) # inherited from Person