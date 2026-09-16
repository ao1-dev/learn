# Conditionals - if/elif/else 

age = 25
has_job = True

# if
if age >= 18:
    print("Adult")
else:
    print("Minor")

# elif
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Combin with (and) / (or) / (not)

if age >= 18 and had_job:
    print("Can rent an apartment")
elif age >= 18 and not had_job:
    print("Adult, but no job yet")
else:
    print("Too young")

# Nested if inside if

if age >= 18:
    if has_jobb:
        print("Independent")
    else:
        print("Adult, still looking for work")

# Truthy / falsy

name = "ao"
if name:
    print(f"Hello, {name}")
else:
    print("No name given")

