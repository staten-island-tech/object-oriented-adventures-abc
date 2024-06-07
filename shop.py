import json
from save import save_character_info

class WeaponShop:
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage

    def to_dict(self):
        return {'name': self.name, 'price': self.price, 'damage': self.damage}

class ArmorShop:
    def __init__(self, name, price, health):
        self.name = name
        self.price = price
        self.health = health

    def to_dict(self):
        return {'name': self.name, 'price': self.price, 'health': self.health}

def shop_interaction(player, save_character_info):
    while True:
        bank_balance = player.coins
        shop = input("Do you want to visit the Weapon Shop or the Armor Shop? Type the full shop out. Type 'exit' to leave: ").lower()

        if shop == "exit":
            break

        if shop == "weapon shop":
            weaponshop = [
                WeaponShop("Axe", 100, 10),
                WeaponShop("Basic Sword", 150, 25),
                WeaponShop("Wooden Sword", 200, 35),
                WeaponShop("Stone Sword", 400, 50),
                WeaponShop("Iron Sword", 550, 75),
                WeaponShop("Chainsaw", 900, 100),
                WeaponShop("Blade", 1000, 150),
                WeaponShop("Samurai", 1200, 250),
                WeaponShop("Cat", 1750, 280),
                WeaponShop("Dog", 2500, 300),
                WeaponShop("Basketball", 5800, 325),
                WeaponShop("Wallet", 10000, 350),
                WeaponShop("Money", 15000, 455),
                WeaponShop("Credit Card", 21000, 470),
                WeaponShop("Idk", 24500, 500),
                WeaponShop("X", 100000, 1111),
            ]

            print("Weapons you can buy in this shop:")
            for weapon in weaponshop:
                print(f"{weapon.name} - Price: {weapon.price} - Damage: {weapon.damage}")

            chosen_weapon = input("Which weapon would you like to buy? Type its full name. Type 'exit' to leave the shop. ").lower()

            if chosen_weapon == "exit":
                break

            for weapon in weaponshop:
                if chosen_weapon == weapon.name.lower():
                    if bank_balance >= weapon.price:
                        print(f"Purchased {weapon.name} for {weapon.price} coins.")
                        player.weapon = weapon
                        bank_balance -= weapon.price
                        player.coins = bank_balance
                        save_character_info(player)
                        break
                    else:
                        print("Insufficient coins.")
                        break
            else:
                print("Invalid weapon choice.")

        elif shop == "armor shop":
            armorshop = [
                ArmorShop("Cotton Armor", 100, 10),
                ArmorShop("Wool Armor", 200, 25),
                ArmorShop("Wooden Armor", 300, 50),
                ArmorShop("Thin Metal Armor", 1000, 55),
                ArmorShop("Thick Metal Armor", 5000, 80),
                ArmorShop("Thicker Metal Armor", 7500, 100),
                ArmorShop("Type Armor", 10000, 130),
                ArmorShop("Blue Armor", 15000, 190),
                ArmorShop("IDK Armor", 18000, 240),
                ArmorShop("Yuck Armor", 20000, 290),
                ArmorShop("Please Armor", 21000, 390),
                ArmorShop("Help Orange Armor", 25000, 510),
                ArmorShop("Red Russian Armor", 27500, 590),
                ArmorShop("X Armor", 111111, 1111),
            ]

            print("Armor you can buy in this shop:")
            for armor in armorshop:
                print(f"{armor.name} - Price: {armor.price} - Armor Health: {armor.health}")

            chosen_armor = input("Which armor would you like to buy? Type its full name. Type 'exit' to leave the shop. ").lower()

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
                print("Invalid armor choice, make sure you spelled it right with spaces.")

        else:
            print("Invalid shop choice. Type 'Armor Shop' or 'Weapon Shop.'")
