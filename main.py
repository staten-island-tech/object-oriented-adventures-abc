import json
import os
from shop import WeaponShop, ArmorShop
from save import save_character_info

class MainCharacter:
    def __init__(self, name, dungeon_level=1, armor=None, weapon=None, coins=100, health=100):
        self.name = name
        self.dungeon_level = dungeon_level
        self.armor = armor
        self.weapon = weapon
        self.coins = coins
        self.base_health = health

    def get_health(self):
        self.base_health = 100
        if self.armor:
            return self.base_health + self.armor.health
        else:
            return self.base_health

def view_profile():
    player = load_character_info()
    if player:
        print("Viewing Character Profile:")
        display_character_info(player)
    else:
        print("No character found. Please create a character first.")

def create_main_character():
    print("Welcome to The Dungeons!")
    name = input("What do you want to name your character? Enter: ")
    character = MainCharacter(name)
    save_character_info(character) 
    return character

def load_character_info():
    try:    # could be exceptions
        with open("character_info.json", "r") as f:
            character_info = json.load(f)
            if not character_info or all(value == "" for value in character_info.values()):
                return None  # if character info is empty don't return anything (except)
    except (FileNotFoundError, json.JSONDecodeError):
        return None 

    weapon_info = character_info.get('weapon')
    weapon = None
    if weapon_info and isinstance(weapon_info, dict):
        weapon = WeaponShop(weapon_info['name'], int(weapon_info['price']), int(weapon_info['damage']))

    armor_info = character_info.get('armor')
    armor = None
    if armor_info and isinstance(armor_info, dict):
        armor = ArmorShop(armor_info['name'], int(armor_info['price']), int(armor_info['health']))

    return MainCharacter(
        name=character_info.get('name', ''),
        dungeon_level=character_info.get('dungeon_level', 1),
        armor=armor,
        weapon=weapon,
        coins=character_info.get('coins', 100),
        health=character_info.get('health', 100)
    )

if not os.path.exists("character_info.json"): #if the file doesn't exist, then do this
    empty_character = {
        "name": None,
        "dungeon_level": 1,
        "armor": None,
        "weapon": None,
        "coins": 100,
        "health": 100
    }

    with open("character_info.json", "w") as f:
        json.dump(empty_character, f, indent=4)

def display_character_info(player):
    print(f"Character Name: {player.name}")
    print(f"Dungeon Level: {player.dungeon_level}")
    print(f"Coins: {player.coins}")
    print(f"Equipped Armor: {player.armor.name if player.armor else 'None'}")
    print(f"Equipped Weapon: {player.weapon.name if player.weapon else 'None'}")
    print(f"Health: {player.get_health()}")