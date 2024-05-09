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

