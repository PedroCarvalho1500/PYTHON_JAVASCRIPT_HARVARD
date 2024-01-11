people = [
    {"name": "John", "country": "England"},
    {"name": "James", "country": "USA"},
    {"name": "Harry", "country": "USA"}
]

people.sort(key=lambda person: person["name"])

print(people)