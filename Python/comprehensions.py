# Comprehensions - build list/dicts in one line

ages = [12, 16, 22, 44]

# Long form
adults = []
for age in ages:
    if age >= 18:
        adults.append(age)
print(adults)

# Same thing as a list
adults = [age for age in ages if age >= 18]
print(adults)

# Transform every item
labels = ["adult" if age >= 18 else "minor" for age in ages]
print(labels)

doubled = [n * 2 for n in range(4)]
print(doubled)

# Dict comprehension
people = ["Pete", "Remi", "John"]
lengths = {name: len(name) for name in people}
print(lengths)

# From a list of dicts
rows = [
    {"name": "Pete", "age": 22},
    {"name": "Remi", "age": 15},
    {"name": "John", "age": 33},
]

names = [p["name"] for p in rows]
adults_name = [p["name"] for p in rows if p["age"] >= 18]
print(names)
print(adults_name)

# Set comprehension - unique values
words = ["hi", "yo", "hey"]
unique_w = {w.upper() for w in words}
print(unique_w)

