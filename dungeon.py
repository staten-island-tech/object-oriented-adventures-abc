import random
from save import save_character_info

def dungeon_interaction(player, save_function):
    print("Entering the dungeon...")

    player.base_health = 100
    player.health = player.max_health

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

    print("Unlocked Levels:")
    for level in dungeon_levels:
        print(level)

    while True:
        print("Available Dungeons:")
        for level in dungeon_levels:
            if level["unlocked"]:
                print(f"Dungeon Level {level['level']}: {level['name']}")
        chosen_dungeon = int(input("What dungeon do you want to do? Enter the number: "))
        chosen_level = next((level for level in dungeon_levels if level["level"] == chosen_dungeon), None)
        print("Chosen Level:", chosen_level)
        if chosen_level is None:
            print("Invalid choice. Try again.")
            continue
        if chosen_level["unlocked"]:
            break
        else:
            print("This dungeon is locked. Complete the previous dungeons first.")

    while chosen_level["health"] > 0:
        print(f"Your Health: {player.health}")
        print(f"Monster Health: {chosen_level['health']}")
        action = input("Do you want to hit or block? (hit/block): ")
        if action.lower() == "hit":
            if random.random() < 0.5:
                print("You got hit by the monster!")
                player.health -= chosen_level["damage"]
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
                player.health -= chosen_level["damage"]
            else:
                print("You successfully blocked the monster's attack and recovered a bit.")
                player.health += 10
        else:
            print("Invalid choice. Choose 'hit' or 'block'.")

        if player.health <= 0:
            print("You died. Game over.")
            break

    if chosen_level["health"] <= 0:
        if chosen_level["level"] < 10:
            next_level = next((level for level in dungeon_levels if level["level"] == chosen_level["level"] + 1), None)
        if next_level is not None:
            next_level["unlocked"] = True
            print(f"Next dungeon, Dungeon Level {next_level['level']} ({next_level['name']}), is now unlocked!")
        player.dungeon_level = chosen_level["level"] + 1
    save_function(player)  # Call the function passed as an argument


    if chosen_level["level"] == 10:
        print("Congratulations! You've completed all dungeons. Wait for more levels to come out.")
