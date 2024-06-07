import json

def save_character_info(player):
    character_info = {
        'name': player.name,
        'dungeon_level': player.dungeon_level,
        'armor': player.armor.to_dict() if player.armor else None,
        'weapon': player.weapon.to_dict() if player.weapon else None,
        'coins': player.coins,
        'health': player.base_health
    }
    with open("character_info.json", "w") as f:
        json.dump(character_info, f)
