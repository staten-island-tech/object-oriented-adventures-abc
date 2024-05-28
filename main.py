import json

class Armor:
    def __init__(self, name, price, health):
        self.name = name
        self.price = price
        self.health = health

class Weapon:
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage

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
            return self.base_health + self.armor.health
        else:
            return self.base_health

    @property
    def max_health(self):
        if self.armor:
            return 100 + self.armor.health
        else:
            return 100

    def to_dict(self):
        return {
            "name": self.name,
            "dungeon_level": self.dungeon_level,
            "armor": self.armor.__dict__ if self.armor else None,
            "weapon": self.weapon.__dict__ if self.weapon else None,
            "coins": self.coins,
            "base_health": self.base_health,
        }

def create_main_character():
    print("Welcome to The Dungeons!")
    name = input("What do you want to name your character? Enter: ")
    return MainCharacter(name)

def save_character_info(character):
    with open("character_info.json", "w") as f:
        json.dump(character.to_dict(), f)

def load_character_info():
    try:
        with open("character_info.json", "r") as f:
            character_info = json.load(f)
            armor = character_info.get("armor")
            weapon = character_info.get("weapon")
            if armor:
                armor = Armor(**armor)
            if weapon:
                weapon = Weapon(**weapon)
            return MainCharacter(
                name=character_info["name"],
                dungeon_level=character_info["dungeon_level"],
                armor=armor,
                weapon=weapon,
                coins=character_info["coins"],
                health=character_info["base_health"]
            )
    except FileNotFoundError:
        return None

def display_character_info(player):
    print(f"Character Name: {player.name}")
    print(f"Dungeon Level: {player.dungeon_level}")
    print(f"Coins: {player.coins}")
    print(f"Equipped Armor: {player.armor.name if player.armor else 'None'}")
    print(f"Equipped Weapon: {player.weapon.name if player.weapon else 'None'}")
    print(f"Health: {player.health}")

if __name__ == "__main__":
    from shop import shop_interaction
    from dungeon import dungeon_interaction

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
                dungeon_interaction(player)
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

    main_character_interaction()

