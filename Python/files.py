# Files - read and write
# Modus: "w" - write, "r" - read, "a" - append

path = "notes.txt"

# Write - creates the file (Will overwrites if it exists)
with open(path, "w", encoding="utf-8") as file:
    file.write("Hello from python\n")
    file.write("Second line\n")

# Append - add at the end, keep old content
with open(path, "a", encoding="utf-8") as file:
    file.write("Third line\n")

# Read everything as one string
with open(path, "r", encoding="utf-8") as file:
    text = file.read()
print(text)

# Read line by line
with open(path, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip()) # removes \n

# Read all lines into a list
with open(path, "missing.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
print(lines)

# Combine with try / except
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("That file does not exist")

