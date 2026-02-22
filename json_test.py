import json

person = {
    "name" : "Asim",
    "age" : 28,
    "email" : ["asimkonar@gmail.com", "konarasim@gmail.com"],
    "married" : False
}
with open("person.json", "w") as file:
    json.dump(person, file, indent= 4)