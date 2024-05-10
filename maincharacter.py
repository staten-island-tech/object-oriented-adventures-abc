import json
import os
## Create Class for creating new dictionaries here

class Main_Character:
    def __init__(self, name, level, coins, weapon, armor):
        self.name = name
        self.level = level
        self.coins = coins
        self.weapon = weapon 
        self.armor = armor
    def __str__(self):
        return f"{self.name}, {self.level}, {self.coins}, {self.weapon}, {self.armor}"
    
with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

    def maincharacter(name, level, coins, weapon, armor):
        main = Main_Character(name, level, coins, weapon, armor)
        data.append(cat.__dict__)
        for i in data:
            print(i)

user = input("Do you want to enter a catbreed to the file? Y or N").lower()
while user in "y":
    breed = input("What's the name of the cat breed?").lower()
    hair_length = input("How long is the cat's hair normally? Short/Medium/Long").lower()
    origin = input("What country the cat originate from?").lower()
    size = input("How big is the cat breed? Small/Medium/Large").lower()

    catbreed(breed, hair_length, origin, size)

    user = input("Enter another catbreed by saying Y, N if not.")


#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")