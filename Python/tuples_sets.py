# Tuples - ordered, but cannot change
point = (10, 20)
print(point[0])
print(len(point))

# point[0] = 99 # TypeError - tuples are read-only

# Useful for fixed pairs - (x, y), (lat, lon)

name, age = ("Alex", 20)
print(name, age)

# One-item tuple needs a comma
not_a_tuple = (42)
a_tuple = (42,)
print(type(not_a_tuple), type(a_tuple))

# Sets - unordered, unique values only
nums = {1, 2, 2, 3, 3, 3}
print(nums) # No duplicates, they are gone

nums.add(4)
nums.discard(2)
print(nums)

print(3 in nums)

# Unique from a list
names = ["Ida", "Alex", "Hedda", "Trine"]
unique = set(names)
print(unique)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b) # union
print(a & b) # intersection {3}
print(a - b) # difference {1, 2}





