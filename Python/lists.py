# Lists - ordered, changeable, mixed

names = ["Pete", "John", "Alex"] # [0] - [1] - [2]
numbers = [10, 20, 30, 40]
mixed = ["Alex", 25, True]

# Index - first item is 0
print(names[0])
print(names[-1])

# Slice - [start:stop]
print(numbers[1:3])
print(numbers[:2])
print(numbers[2:])

# Change an item
names[1] = "Ida"
print(names) # [1] john is now [1] ida

# Add
names.append("Sam") # Added to the end of the list
names.insert(0, "Hedda") # Added to the [0] index
print(names)

# Remove
names.remove("Hedda") # Remove first match
last = names.pop() # remove and return last item
print(last)
print(names)

# Useful helpers
print(len(names)) # How many items 
print("Hedda" in names) # True or False
print(sorted(numbers)) # New sorted list (original unchanged)
numbers.sort() # Sorts the list itself
print(numbers)

# Loop
for name in names:
    print(name)

# Loop with index
for i, name in enumerate(names):
    print(i, name)

