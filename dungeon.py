import random
from character import save_character_info

def dungeon_interaction(player, weapon_shop, armor_shop):
    print("Entering the dungeon...")
    player.health = 100

    dungeon_levels = [
        {"level": 1, "name": "Trainer", "health": 100, "damage": 5, "unlocked": True},
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

    # Unlock levels up to the player's current dungeon level
    for level in dungeon_levels:
        if level["level"] <= player.dungeon_level:
            level["unlocked"] = True

    while True:
        print("Available Dungeons:")
        for level in dungeon_levels:
            if level["unlocked"]:
                print(f"Dungeon Level {level['level']}: {level['name']}")
        chosen_dungeon = int(input("Which dungeon would you like to enter? (Enter the level number): "))
        chosen_level = next((level for level in dungeon_levels if level["level"] == chosen_dungeon), None)
        if chosen_level is None:
            print("Invalid dungeon level. Please choose from the available options.")
            continue
        if chosen_level["unlocked"]:
            break
        else:
            print("This dungeon is locked. Complete the previous dungeons first.")
            return

    while chosen_level["health"] > 0:
        print(f"Your Health: {player.health}")
        print(f"Monster Health: {chosen_level['health']}")
        action = input("Do you want to hit or block? (hit/block): ")
        if action.lower() == "hit":
            if random.random() < 0.5:
                print("You missed and got hit by the monster!")
                player.health -= chosen_level["damage"]
            else:
                equipped_weapon = player.weapon
                weapon_damage = next((weapon.damage for weapon in weapon_shop if weapon.name == equipped_weapon), 5)
                print(f"You hit the monster for {weapon_damage} damage!")
                chosen_level["health"] -= weapon_damage
                if chosen_level["health"] <= 0:
                    print("You defeated the monster!")
                    player.coins += chosen_level["level"] * 100
                    break
        elif action.lower() == "block":
            if random.random() < 0.5:
                print("You failed to block and got hit by the monster!")
                player.health -= chosen_level["damage"]
            else:
                print("You successfully blocked the monster's attack and gained 5 health!")
                player.health += 5
        else:
            print("Invalid action. Please choose 'hit' or 'block'.")

        if player.armor:
            equipped_armor = player.armor
            armor_health = next((armor.health for armor in armor_shop if armor.name == equipped_armor), 0)
            player.health += armor_health

        if player.health <= 0:
            print("Game over! Your health reached zero.")
            break

    if chosen_level["health"] <= 0:
        if chosen_level["level"] < 10:
            next_level = next((level for level in dungeon_levels if level["level"] == chosen_level["level"] + 1), None)
            if next_level is not None:
                next_level["unlocked"] = True
                print(f"Next dungeon, Dungeon Level {next_level['level']} ({next_level['name']}), is now unlocked!")
            player.dungeon_level = chosen_level["level"] + 1
        save_character_info(player)

    if chosen_level["level"] == 10:
        print("Congratulations! You've completed all dungeon levels!")
