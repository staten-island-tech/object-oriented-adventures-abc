import json

def save_character_info(character):
    with open("character_info.json", "w") as f:
        json.dump(character.__dict__, f)
