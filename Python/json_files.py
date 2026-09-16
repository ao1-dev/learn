# JSON - save and load dicts / lists

import json

person = {
    "name": "alex",
    "age": 20,
    "has_job": True,
    "skills": ["python", "pandas"],
}

# dict - JSON string
text = json.dumps(person, indent=2)
print(text)

# JSON string - dict
data = json.loads(text)
print(data["name"])
print(data["skills"][0])

# Write to a file
with open("person.json", "w", encoding="utf-8") as file:
    json.dump(person, file, indent=2)

# Read from a file
with open("person.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded)
print(loaded["age"])

# List of dicts
people = [
    {"name": "Pete", "age": 20},
    {"name": "Hedda", "age": 22},
]

with open("people.json", "w", encoding="utf-8") as file:
    json.dump(people, file, indent=2)

with open("people.json", "r", encoding="utf-8") as file:
    everyone = json.load(file)

for p in everyone:
    print(f"{p['name']} is {p['age']}")


