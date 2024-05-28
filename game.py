from main import create_main_character, load_character_info, save_character_info, display_character_info
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
            # Implement leaderboard interaction here
        elif action.lower() == "exit":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid action. Please choose 'Dungeon', 'Shop', 'Profile', 'Leaderboard', or 'Exit'.")

if __name__ == "__main__":
    main_character_interaction()

