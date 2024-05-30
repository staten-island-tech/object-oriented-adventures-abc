import json
from save import save_character_info

class WeaponShop:
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage

class ArmorShop:
    def __init__(self, name, price, health):
        self.name = name
        self.price = price
        self.health = health

def save_character_info(character):
    with open("character_info.json", "w") as f:
        json.dump(character.__dict__, f)

def shop_interaction(player, save_character_info):
    while True:
        bank_balance = player.coins
        action = input("What do you want to do? Buy or Exit: ").lower()

        if action == "buy":
            shop = input("Do you want to visit the Weapon Shop or the Armor Shop? ").lower()

            if shop == "weapon":
                weaponshop = [
                    WeaponShop("Axe", 10, 10),
                    WeaponShop("Basic Sword", 50, 25),
                    WeaponShop("Wooden Sword", 100, 35),
                    WeaponShop("Stone Sword", 200, 50),
                    WeaponShop("Iron Sword", 400, 75)
                ]

                print("Available Weapons:")
                for weapon in weaponshop:
                    print(f"{weapon.name} - Price: {weapon.price} - Damage: {weapon.damage}")

                chosen_weapon = input("Which weapon would you like to buy? Type 'exit' to leave the shop. ").lower()

                if chosen_weapon == "exit":
                    break

                for weapon in weaponshop:
                    if chosen_weapon == weapon.name.lower():
                        if bank_balance >= weapon.price:
                            print(f"Purchased {weapon.name} for {weapon.price} coins.")
                            player.weapon = weapon.name
                            bank_balance -= weapon.price
                            player.coins = bank_balance
                            save_character_info(player)
                            break
                        else:
                            print("Insufficient coins.")
                            break
                else:
                    print("Invalid weapon choice.")

            elif shop == "armor":
                armorshop = [
                    ArmorShop("Cotton Armor", 10, 10),
                    ArmorShop("Wool Armor", 50, 25),
                    ArmorShop("Wooden Armor", 150, 50),
                    ArmorShop("Thin Metal Armor", 250, 55),
                    ArmorShop("Thick Metal Armor", 500, 80)
                ]

                print("Available Armor:")
                for armor in armorshop:
                    print(f"{armor.name} - Price: {armor.price} - Armor Health: {armor.health}")

                chosen_armor = input("Which armor would you like to buy? Type 'exit' to leave the shop. ").lower()

                if chosen_armor == "exit":
                    break

                for armor in armorshop:
                    if chosen_armor == armor.name.lower():
                        if bank_balance >= armor.price:
                            print(f"Purchased {armor.name} for {armor.price} coins.")
                            player.armor = armor
                            bank_balance -= armor.price
                            player.coins = bank_balance
                            save_character_info(player)
                            break
                        else:
                            print("Insufficient coins.")
                            break
                else:
                    print("Invalid armor choice.")

            else:
                print("Invalid shop choice.")

        elif action == "exit":
            break

        else:
            print("Invalid action. Please choose 'Buy' or 'Exit'.")

if __name__ == "__main__":
    # Add the necessary imports for player-related functionality
    from main import load_character_info, display_character_info, create_main_character

    while True:
        player = load_character_info()
        if player is None:
            player = create_main_character()
            save_character_info(player)

        print("Welcome to The Dungeons!")
        display_character_info(player)

        shop_interaction(player)

        action = input("Do you want to continue exploring or exit the game? (Explore/Exit): ").lower()
        if action == "exit":
            print("Exiting the game. Goodbye!")
            break

save_character_info(player)