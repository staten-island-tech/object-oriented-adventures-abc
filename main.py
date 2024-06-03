import json
import os
from shop import WeaponShop
from save import save_character_info

class MainCharacter:
    def __init__(self, name, dungeon_level=1, armor=None, weapon=None, coins=100, health=100):
        self.name = name
        self.dungeon_level = dungeon_level
        self.armor = armor
        self.weapon = weapon
        self.coins = coins
        self.base_health = health

    @property
    def health(self):
        if self.armor:
            return min(self.base_health + self.armor.health, self.max_health)
        else:
            return self.base_health

    @property
    def max_health(self):
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
    return MainCharacter(name)

def load_character_info():
    try:
        with open("character_info.json", "r") as f:
            character_info = json.load(f)
            character_info.pop('base_health', None)
            weapon_info = character_info.get('weapon')
            weapon = WeaponShop(weapon_info['name'], weapon_info['price'], weapon_info['damage']) if weapon_info else None
            return MainCharacter(**character_info, weapon=weapon)
    except FileNotFoundError:
        return None

def display_character_info(player):
    print(f"Character Name: {player.name}")
    print(f"Dungeon Level: {player.dungeon_level}")
    print(f"Coins: {player.coins}")
    print(f"Equipped Armor: {player.armor if player.armor else 'None'}")
    print(f"Equipped Weapon: {player.weapon}")
    print(f"Health: {player.health}")  
