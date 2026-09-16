# Dictionaries - key: value

person = {
    "name": "Alex",
    "age": 20,
    "has_job": True,
}

# Read
print(person["name"])
print(person.get("age"))
print(person.get("city"))

# Change and add
person["age"] = 22
person["city"] = "Oslo"
print(person)

# Remove
job = person.pop("has_job")
print(job)
print(person)

# Loop
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

print(person.keys())
print(person.values())

# List if dicts
people = [
    {"name": "Pete", "age": 20},
    {"name": "Hedda", "age": 22},
]

for p in people:
    if p["age"] >= 18:
        print(f"{p['name']} is an adult")

