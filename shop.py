class Weapon_Shop:
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage

class Armor_Shop:
    def __init__(self, name, price, health):
        self.name = name
        self.price = price
        self.health = health

def main_character_interaction():
    while True:
        bank_balance = 100
        action = input("What do you want to do? Dungeon or Shop: ")

        if action.lower() == "shop":
            shop = input("Do you want to visit the Weapon Shop or the Armor Shop? ")

            if shop.lower() == "weapon":
                weaponshop = [Weapon_Shop("Axe", 10, 10),
                               Weapon_Shop("Basic Sword", 50, 25),
                               Weapon_Shop("Wooden Sword", 100, 35),
                               Weapon_Shop("Stone Sword", 200, 50),
                               Weapon_Shop("Iron Sword", 400, 75)]

                print("Available Weapons:")
                for weapon in weaponshop:
                    print(f"{weapon.name} - Price: {weapon.price} - Damage: {weapon.damage}")

                chosen_weapon = input("Which weapon would you like to buy? Type exit to leave the shop. ")

                for weapon in weaponshop:
                    if chosen_weapon.lower() == weapon.name.lower():
                        if bank_balance >= weapon.price:
                            print(f"Purchased {weapon.name} for {weapon.price} coins.")
                            bank_balance -= weapon.price
                        else:
                            print("Invalid coins.")
                        if chosen_weapon.lower() == "exit":  
                            break

            elif shop.lower() == "armor":
                armorshop = [Armor_Shop("Cotton Armor", 10, 10),
                               Armor_Shop("Wool Armor", 50, 25),
                               Armor_Shop("Wooden Armor", 150, 50),
                               Armor_Shop("Thin Metal Armor", 250, 55),
                               Armor_Shop("Thick Metal Armor", 500, 80)]

                print("Available Armor:")
                for armor in armorshop:
                    print(f"{armor.name} - Price: {armor.price} - Armor Health: {armor.health}")

                chosen_armor = input("Which armor would you like to buy? Type exit to leave the shop. ")

                for armor in armorshop:
                    if chosen_armor.lower() == armor.name.lower():
                        if bank_balance >= armor.price:
                            print(f"Purchased {armor.name} for {armor.price} coins.")
                            bank_balance -= armor.price
                        elif bank_balance <= armor.price:
                            print("Invalid coins.")
                        elif chosen_armor.lower() == "exit":
                            break

        elif action.lower() == "dungeon":
            print("Entering the dungeon...")

        else:
            print("Invalid action. Please choose 'Dungeon' or 'Shop'.")

main_character_interaction()