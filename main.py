import json
from shop import shop_interaction
from dungeon import dungeon_interaction
from save import save_character_info

class MainCharacter:
    def __init__(self, name, dungeon_level=1, armor=None, weapon=None, coins=100, health=100):
        self.name = name
        self.dungeon_level = dungeon_level
        self.armor = armor
        self.weapon = weapon
        self.coins = coins
        self.base_health = health  # Store the base health

    @property
    def health(self):
        """Calculate current health considering armor."""
        if self.armor:
            return min(self.base_health + self.armor.health, self.max_health)
        else:
            return min(self.base_health, self.max_health)

    @property
    def max_health(self):
        """Calculate maximum health considering armor."""
        if self.armor:
            return self.base_health + self.armor.health
        else:
            return self.base_health

def create_main_character():
    print("Welcome to The Dungeons!")
    name = input("What do you want to name your character? Enter: ")
    return MainCharacter(name)

def load_character_info():
    try:
        with open("character_info.json", "r") as f:
            character_info = json.load(f)
            # Exclude the 'base_health' attribute if present
            character_info.pop('base_health', None)
            return MainCharacter(**character_info)
    except FileNotFoundError:
        return None

def display_character_info(player):
    print(f"Character Name: {player.name}")
    print(f"Dungeon Level: {player.dungeon_level}")
    print(f"Coins: {player.coins}")
    print(f"Equipped Armor: {player.armor.name if player.armor else 'None'}")
    print(f"Equipped Weapon: {player.weapon}")
    print(f"Health: {player.health()}")  # Call health() as a method

def main_character_interaction():
    while True:
        player = load_character_info()
        if player is None:
            player = create_main_character()
            save_character_info(player)

        print("Welcome to The Dungeons!")
        display_character_info(player)

        action = input("What do you want to do? Dungeon, Shop, Profile, Leaderboard, or Exit: ")
        if action.lower() == "dungeon":
            dungeon_interaction(player, save_character_info)  # Updated call to dungeon_interaction function
        elif action.lower() == "shop":
            shop_interaction(player)
        elif action.lower() == "profile":
            print("Viewing Character Profile:")
            display_character_info(player)
        elif action.lower() == "leaderboard":
            print("Viewing Leaderboard:")
        elif action.lower() == "exit":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid action. Please choose 'Dungeon', 'Shop', 'Profile', 'Leaderboard', or 'Exit'.")

if __name__ == "__main__":
    main_character_interaction()
