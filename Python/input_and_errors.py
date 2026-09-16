# Input and errors

name = input("What is your name? ")
print(f"Hello, {name}")

# input() always returns str - convert if you need a number
age_text = input("How old are you? ")

try:
    age = int(age_text)
    print(f"Next year you will be {age + 1}")
except ValueError:
    print("That was not a number")


# Specific errors
try:
    numbers = [10, 20, 30]
    index = int(input("Index 0-2: "))
    print(numbers[index])
except ValueError:
    print("Need a whole number")
except IndexError:
    print("That index does not exist")


# Else runs if no error, finally always run
try:
    n = int(input("Number: "))
except ValueError:
    print("Not a number")
else:
    print(n * 2)
finally:
    print("Done")


# Raise - make your own error
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

print(set_age(20))
# print(set_age(-1)) - Will cause ValueError