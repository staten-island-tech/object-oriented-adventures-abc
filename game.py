from main import load_character_info, display_character_info, create_main_character, view_profile
from shop import shop_interaction
from dungeon import dungeon_interaction
from save import save_character_info

def main_character_interaction():
    while True:
        player = load_character_info()
        if player is None:
            player = create_main_character()
            save_character_info(player)
        if player.name is None:
            player = create_main_character()
            save_character_info

        print("Welcome to The Dungeons! Open the readME.md to learn about the game, however, it is simple, all you have to do is get through dungeons and level up your character.")
        display_character_info(player)

        action = input("What do you want to do in the game, there are four options. Type 'Dungeon', 'Shop', 'Profile', or 'Exit': ").lower()
        if action == "dungeon":
            dungeon_interaction(player)
        elif action == "shop":
            shop_interaction(player, save_character_info)
        elif action == "profile":
            view_profile()
        elif action == "exit":
            print("Why don't you want to play the game? Press play again please.")
            break
        else:
            print("Invalid action. Please choose 'Dungeon', 'Shop', or 'Profile'. Do not type 'Exit'.")

if __name__ == "__main__":
    main_character_interaction()
