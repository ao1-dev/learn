# Operators

x = 10
y = 5

# Aritmetic
print(x + y) # Add
print(x - y) # Subtract
print(x * y) # Multiply
print(x / y) # Division (float number)
print(x // y) # Division (floor number)
print(x % y) # Remainder
print(x ** y) # Power (in this case, 10^5)

# Comparison 
print(x > y) # True
print(x < y) # False
print(x == y) # False equal
print(x != y) # True
print(x >= 5) # False
print(x <= 10) # True

# Logical
age = 20
has_job = True

print(age >= 18 and has_job) # True, both must be True
print(age < 18 or has_job) # True, at least one True
print(not has_job) # False

# Mix (Useful later with if/else statments)
print(age >= 18 and not has_job) # False


# Assignment
score = 0 
score += 3 # Add 3 to score
score -= 2 # Subtract 2 from score
score *= 3 # Multiply 3 to score

print(score) # Score is now (1*3= 3)
