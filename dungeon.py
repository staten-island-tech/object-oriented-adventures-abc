import random
from main import save_character_info

def dungeon_interaction(player):
    print("Entering the dungeon...")

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

    for level in dungeon_levels:
        if level["level"] <= player.dungeon_level:
            level["unlocked"] = True

    while True:
        print("Available Dungeons:")
        for level in dungeon_levels:
            if level["unlocked"]:
                print(f"Dungeon Level {level['level']}: {level['name']}")

        chosen_dungeon = input("What dungeon do you want to do? Enter the number or type 'exit' to leave: ")

        if chosen_dungeon.lower() == 'exit':
            print("Exiting the dungeon...")
            return

        try:
            chosen_dungeon = int(chosen_dungeon)
        except ValueError:
            print("Invalid choice. Try again.")
            continue

        chosen_level = next((level for level in dungeon_levels if level["level"] == chosen_dungeon), None)

        if chosen_level is None:
            print("Invalid choice. Try again.")
            continue

        if not chosen_level["unlocked"]:
            print("This dungeon is locked. Complete the previous dungeons first.")
            continue

        # Reset player's health to maximum health at the start of the dungeon
        player.base_health = player.max_health

        while chosen_level["health"] > 0:
            print(f"Your Health: {player.health}")
            print(f"Monster Health: {chosen_level['health']}")
            action = input("Do you want to hit, block, or exit? (hit/block/exit): ")

            if action.lower() == "hit":
                if random.random() < 0.5:
                    print("You got hit by the monster!")
                    player.base_health -= chosen_level["damage"]
                else:
                    print("You hit the monster! Good job!")
                    chosen_level["health"] -= 20
                    if chosen_level["health"] <= 0:
                        print("Congratulations! You defeated the monster!")
                        player.coins += chosen_level["level"] * 100
                        break
            elif action.lower() == "block":
                if random.random() < 0.5:
                    print("You failed to block the monster's attack!")
                    player.base_health -= chosen_level["damage"]
                else:
                    print("You successfully blocked the monster's attack and recovered a bit.")
                    player.base_health += 10
            elif action.lower() == "exit":
                print("Exiting the dungeon...")
                return
            else:
                print("Invalid choice. Choose 'hit', 'block', or 'exit'.")

            player.base_health = min(player.base_health, player.max_health)

            if player.base_health <= 0:
                print("You died. Game over.")
                return

        if player.base_health <= 0:
            return

        if chosen_level["health"] <= 0:
            if chosen_level["level"] < 10:
                next_level = next((level for level in dungeon_levels if level["level"] == chosen_level["level"] + 1), None)
                if next_level:
                    next_level["unlocked"] = True
                    print(f"Next dungeon, Dungeon Level {next_level['level']} ({next_level['name']}), is now unlocked!")
                player.dungeon_level = chosen_level["level"] + 1
            save_character_info(player)

        if chosen_level["level"] == 10:
            print("Congratulations! You've completed all dungeons. Wait for more levels to come out.")
            break

