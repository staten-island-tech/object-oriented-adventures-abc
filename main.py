from character import MainCharacter, create_main_character, save_character_info, load_character_info
from shop import WeaponShop, ArmorShop, shop_interaction
from dungeon import dungeon_interaction

def main_character_interaction():
    while True:
        player = load_character_info()
        if player is None:
            player = create_main_character()
            save_character_info(player)

        print(f"Unfortunately you're here again, {player.name}.")
        print(f"Dungeon Level {player.dungeon_level}.")
        print(f"You have {player.coins} coins, {player.armor} armor, and {player.weapon} equipped.")

        action = input("What do you want to do? Shop or Dungeon: ")
        if action.lower() == "shop":
            shop_interaction(player)
