import random
from save import save_character_info

def dungeon_interaction(player):
    print("Entering the dungeon...")

    # initializes the players health
    player.health = player.get_health

    dungeon_levels = [
        {"level": 1, "name": "Trainer", "health": 100, "damage": 15, "unlocked": False},
        {"level": 2, "name": "Dog", "health": 305, "damage": 35, "unlocked": False},
        {"level": 3, "name": "Tiger", "health": 400, "damage": 40, "unlocked": False},
        {"level": 4, "name": "Zombie", "health": 500, "damage": 50, "unlocked": False},
        {"level": 5, "name": "Spider", "health": 650, "damage": 65, "unlocked": False},
        {"level": 6, "name": "Alien", "health": 800, "damage": 80, "unlocked": False},
        {"level": 7, "name": "T-Rex", "health": 1000, "damage": 90, "unlocked": False},
        {"level": 8, "name": "Witch", "health": 1250, "damage": 100, "unlocked": False},
        {"level": 9, "name": "Ghost", "health": 1500, "damage": 150, "unlocked": False},
        {"level": 10, "name": "Demon", "health": 2750, "damage": 250, "unlocked": False}
    ]

    for level in dungeon_levels:
        if level["level"] <= player.dungeon_level:
            level["unlocked"] = True


    print("Unlocked Levels:")
    for level in dungeon_levels:
        if level["unlocked"]:
            print(f"Level {level['level']}: {level['name']}")

    chosen_level = None
    while chosen_level is None:
        print("Available Dungeons:")
        for level in dungeon_levels:
            if level["unlocked"]:
                print(f"Dungeon Level {level['level']}: {level['name']}")
        chosen_dungeon = input("What dungeon do you want to do? Enter the number (or type 'exit' to quit the dungeon): ")
        
        if chosen_dungeon.lower() == 'exit':
            print("Exiting dungeon selection.")
            break
        
        if chosen_dungeon.isdigit():
            chosen_dungeon = int(chosen_dungeon)
            chosen_level = next((level for level in dungeon_levels if level["level"] == chosen_dungeon), None)
            if chosen_level and chosen_level["unlocked"]:
                break
        print("Invalid choice or dungeon is locked. Retype an option.")

    if chosen_level:
        print(f"You chose Dungeon Level {chosen_level['level']}: {chosen_level['name']}")

    while chosen_level and chosen_level["health"] > 0 and player.base_health > 0:
        print(f"Your Health: {player.get_health()}")
        print(f"Monster Health: {chosen_level['health']}")
        action = input("Do you want to hit or block? (hit/block): ").lower()

        if action == "hit":
            if random.random() < 0.5:
                print("You got hit by the monster!")
                player.base_health -= chosen_level["damage"]
            else:
                damage = 5 + (player.weapon.damage if player.weapon else 0)  
                print(f"You hit the monster for {damage} damage! Good job!")
                chosen_level["health"] -= damage
                if chosen_level["health"] <= 0:
                    coins_earned = chosen_level["level"] * 100
                    player.coins += coins_earned
                    print(f"You got {coins_earned} coins for winning!")
                    print("Congratulats! You won something for once.")
                    break
        elif action == "block":
            if random.random() < 0.5:
                print("You failed to block, lol u got hit.")
                player.base_health -= chosen_level["damage"]
            else:
                print("You successfully blocked and recovered 10 health, nice.")
                player.base_health += 10
        else:
            print("That's not an option. Choose 'hit' or 'block'.")

        if player.base_health <= 0:
            print("You died. You suck, quit the game.")
            return

    # dungeon completion and next level
    if chosen_level:
        if chosen_level["health"] <= 0:
            player.dungeon_level += 1  # dungeon level of player +1
            if player.dungeon_level <= 10:
                next_level = next((level for level in dungeon_levels if level["level"] == player.dungeon_level), None)
                if next_level:
                    next_level["unlocked"] = True
                    print(f"Next dungeon, Dungeon Level {next_level['level']} ({next_level['name']}), is now unlocked!")
            else:
                print("Wow you're kind of cool, you completed the game, there are no more to do!")
    else:
        print("You didn't select a dungeon.")

    save_character_info(player)
    
