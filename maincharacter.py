import json

class MainCharacter:
    def __init__(self, name, dungeon_level=1, armor=None, weapon=None, coins=100):
        self.name = name
        self.dungeon_level = dungeon_level
        self.armor = armor
        self.weapon = weapon
        self.coins = coins

def create_main_character():
    name = input("Welcome to the game! Please enter your character's name: ")
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

def main():
    player = load_character_info()
    if player is None:
        player = create_main_character()
        save_character_info(player)

    print(f"Welcome back, {player.name}!")
    print(f"You are currently at Dungeon Level {player.dungeon_level}.")
    print(f"You have {player.coins} coins, {player.armor} armor, and {player.weapon} equipped.")

if __name__ == "__main__":
    main()