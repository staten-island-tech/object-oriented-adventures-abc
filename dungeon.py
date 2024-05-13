import random

class DungeonLevel:
    def __init__(self, level, monster, health, damage):
        self.level = level
        self.monster = monster
        self.health = health
        self.damage = damage

dungeon_levels = [
    DungeonLevel(1, "Trainer", 100, 5),
    DungeonLevel(2, "Dog", 125, 15),
    DungeonLevel(3, "Tiger", 150, 20),
    DungeonLevel(4, "Zombie", 175, 25),
    DungeonLevel(5, "Spider", 200, 30),
    DungeonLevel(6, "Alien", 225, 35),
    DungeonLevel(7, "T-Rex", 250, 40),
    DungeonLevel(8, "Witch", 275, 45),
    DungeonLevel(9, "Ghost", 300, 50),
    DungeonLevel(10, "Demon", 325, 80)
]

class Dungeon:
    def __init__(self, player_health):
        self.player_health = player_health

    def enter_dungeon(self):
        for level in dungeon_levels:
            print(f"You've entered Dungeon Level {level.level}. Prepare to face {level.monster}!")
            while level.health > 0 and self.player_health > 0:
                action = input("Do you want to hit or block? ").lower()
                if action == "hit":
                    if random.random() < 0.5:
                        print(f"You hit the {level.monster}!")
                        level.health -= 10  # Assuming a constant hit damage
                    else:
                        print(f"You missed! The {level.monster} hits you!")
                        self.player_health -= level.damage
                elif action == "block":
                    print("You block the monster's attack!")
                    self.player_health += 5  # Gains 5 health when blocking
                else:
                    print("Invalid action. Choose 'hit' or 'block'.")

                if level.health <= 0:
                    print(f"You defeated the {level.monster}!")
                    break
                elif self.player_health <= 0:
                    print("You were defeated. Game over.")
                    return
                print(f"Your health: {self.player_health}, {level.monster}'s health: {level.health}")
        print("Congratulations! You've cleared the dungeon!")

def play_dungeon():
    player_health = 100  # Initial player health
    dungeon = Dungeon(player_health)
    dungeon.enter_dungeon()
    redo = input("Do you want to redo the dungeon? (yes/no): ").lower()
    if redo == "yes":
        play_dungeon()

play_dungeon()