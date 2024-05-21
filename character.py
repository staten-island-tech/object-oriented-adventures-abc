import json

class MainCharacter:
    def __init__(self, name, dungeon_level=1, armor=None, weapon=None, coins=100, health=100):
        self.name = name
        self.dungeon_level = dungeon_level
        self.armor = armor
        self.weapon = weapon
        self.coins = coins
        self.health = health
def create_main_character():
    print("Welcome to The Dungeons! Open readME to learn about the game!")
    name = input("What do you want to name your character? Enter:")
    return MainCharacter(name)

def save_character_info(character):
    with open("character_info.json", "w") as f:
        json.dump(character.__dict__, f)

def load_character_info():
    try:
        with open("character_info.json", "r") as f:
            character_info = json.load(f)
            return MainCharacter(**character_info)
    except FileNotFoundError:
        return None
create_main_character()