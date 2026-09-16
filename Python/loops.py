# Loops - for and while

# for - repeat for each item
names = ["Pete", "John", "Alex"]

for name in names:
    print(f"Hello, {name}")

# Range
for i in range(5):
    print(i)

# Range - (Start, stop)
for i in range(1, 4):
    print(i)

# While - repeat as long as the codition is True

count = 0
while count < 3:
    print(f"count is {count}")
    count += 1 # without this: infinite loop!

# Break - stop the loop now
for n in range(10):
    if n == 3:
        break
    print(n)

# Continue - Skip this round, go to the next
for n in range(5):
    if n == 2:
        continue
    print(n) # 0, 1, 3, 4 (2 skipped)

# Combine - with if
ages = [15, 20, 17, 25]
for age in ages:
    if age >= 18:
        print(f"{age}: Adult")
    else:
        print(f"{age}: Minor")

