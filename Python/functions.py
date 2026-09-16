# Functions - def, parameters, return

def greet():
    print("Hello, world")

greet()

# Parameters (input)
def greet_name(name):
    print(f"Hello, {name}")

greet_name("Alex")

# Default value
def greet_city(name, city="Oslo"):
    print(f"{name} lives in {city}")

greet_city("Alex")
greet_city("Alex", "Bergen")

# Return
def add(a, b):
    return a + b # without return you get None

result = add(5, 10)
print(result)
print(add(5, 5))

# Combine with (if) / (lists) / (dicts)

def is_adult(age):
    return age >= 18

print(is_adult(20)) # True
print(is_adult(15)) # False

def describe(person):
    name = person["name"]
    age = person["age"]
    if is_adult(age):
        return f"{name} is an adult"
    return f"{name} is minor"

people = [
    {"name": "Alex", "age": 20},
    {"name": "Hedda", "age": 22},
]

for p in people:
    print(describe(p))

