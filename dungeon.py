import random
from save import save_character_info

def dungeon_interaction(player, save_character_info):
    print("Entering the dungeon...")

    # Initialize player health
    player.base_health = 100

    # Define dungeon levels
    dungeon_levels = [
        {"level": 1, "name": "Trainer", "health": 100, "damage": 5, "unlocked": False},
        {"level": 2, "name": "Dog", "health": 125, "damage": 15, "unlocked": False},
        {"level": 3, "name": "Tiger", "health": 150, "damage": 20, "unlocked": False},
        {"level": 4, "name": "Zombie", "health": 175, "damage": 25, "unlocked": False},
        {"level": 5, "name": "Spider", "health": 200, "damage": 30, "unlocked": False},
        {"level": 6, "name": "Alien", "health": 225, "damage": 35, "unlocked": False},
        {"level": 7, "name": "T-Rex", "health": 250, "damage": 40, "unlocked": False},
        {"level": 8, "name": "Witch", "health": 275, "damage": 45, "unlocked": False},
        {"level": 9, "name": "Ghost", "health": 300, "damage": 50, "unlocked": False},
        {"level": 10, "name": "Demon", "health": 325, "damage": 80, "unlocked": False}
    ]

    # Unlock levels based on player progress
    for level in dungeon_levels:
        if level["level"] <= player.dungeon_level:
            level["unlocked"] = True

    # Display unlocked levels
    print("Unlocked Levels:")
    for level in dungeon_levels:
        print(level)

    # Choose a dungeon level
    while True:
        print("Available Dungeons:")
        for level in dungeon_levels:
            if level["unlocked"]:
                print(f"Dungeon Level {level['level']}: {level['name']}")
        try:
            chosen_dungeon = int(input("What dungeon do you want to do? Enter the number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        chosen_level = next((level for level in dungeon_levels if level["level"] == chosen_dungeon), None)
        if chosen_level is None:
            print("Invalid choice. Try again.")
        elif chosen_level["unlocked"]:
            break
        else:
            print("This dungeon is locked. Complete the previous dungeons first.")

    # Combat loop
    while chosen_level["health"] > 0 and player.base_health > 0:
        print(f"Your Health: {player.base_health}")
        print(f"Monster Health: {chosen_level['health']}")
        action = input("Do you want to hit or block? (hit/block): ").lower()

        if action == "hit":
            if random.random() < 0.5:
                print("You got hit by the monster!")
                player.base_health -= chosen_level["damage"]
            else:
                damage = chosen_level["damage"] + (player.weapon.damage if player.weapon else 0)
                print(f"You hit the monster for {damage} damage! Good job!")
                chosen_level["health"] -= damage
                if chosen_level["health"] <= 0:
                    coins_earned = chosen_level["level"] * 100
                    player.coins += coins_earned
                    print(f"You earned {coins_earned} coins for completing the dungeon!")
                    print("Congratulations! You defeated the monster!")
                    break
        elif action == "block":
            if random.random() < 0.5:
                print("You failed to block the monster's attack!")
                player.base_health -= chosen_level["damage"]
            else:
                print("You successfully blocked the monster's attack and recovered a bit.")
                player.base_health += 10
        else:
            print("Invalid choice. Choose 'hit' or 'block'.")

        if player.base_health <= 0:
            print("You died. Game over.")
            return

    # Handle dungeon completion and unlock the next level
    if chosen_level["health"] <= 0:
        player.dungeon_level = chosen_level["level"]
        if chosen_level["level"] < 10:
            next_level = next((level for level in dungeon_levels if level["level"] == chosen_level["level"] + 1), None)
            if next_level:
                next_level["unlocked"] = True
                print(f"Next dungeon, Dungeon Level {next_level['level']} ({next_level['name']}), is now unlocked!")
        else:
            print("Congratulations! You've completed all dungeons. Wait for more levels to come out.")

    # Save the player state
    save_character_info(player)
