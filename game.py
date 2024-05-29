from main import load_character_info, display_character_info, create_main_character
from save import save_character_info
from dungeon import dungeon_interaction
from shop import shop_interaction

def view_profile():
    player = load_character_info()
    if player:
        print("Viewing Character Profile:")
        display_character_info(player)
    else:
        print("No character found. Please create a character first.")

def main_character_interaction():
    while True:
        # Load player character information
        player = load_character_info()
        if player is None:
            # If no character found, create a new one
            player = create_main_character()
            save_character_info(player)

        # Display character information
        print("Welcome to The Dungeons!")
        display_character_info(player)

        # Prompt player for action
        action = input("What do you want to do? Dungeon, Shop, Profile, or Exit: ")
        if action.lower() == "dungeon":
            dungeon_interaction(player, save_character_info) 
        elif action.lower() == "shop":
            shop_interaction(player)
            save_character_info(player)
        elif action.lower() == "profile":
            view_profile()
        elif action.lower() == "exit":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid action. Please choose 'Dungeon', 'Shop', 'Profile', or 'Exit'.")

if __name__ == "__main__":
    main_character_interaction()
