# Strings - slicing and methods

text = "  Hello, python  "

print(text.strip()) # remove spaces at ends
print(text.upper()) # HELLO, PYTHON
print(text.lower()) # hello, python
print(text.replace("Python", "Javascript"))

# Index and slice (Same idea as lists)
name = "Python"
print(name[0]) # p
print(name[-1]) # n
print(name[0:3]) # pyt
print(name[:2]) # py
print(name[2:]) # thon

# Check / search
print("Py" in name) # True
print(name.startswith("Py"))
print(name.endswith("on"))
print(name.find("th"))

# Split / join
nac = "pete,22,london"
parts = nac.split(",")
print(nac)

# f-strings
age = 25
print(f"{name} is {age}")
print(f"{name} is {age + 1} next year")
print(f"{3.13159:.2f}") # 2f = 2 decimals

# Multi-line
bio = """Line one
line two"""
print(bio)

