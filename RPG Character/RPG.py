full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"


    if not isinstance(strength, int) or isinstance(intelligence, int) or isinstance(charisma, int):
        return "All stats should be integers"

    if any(i < 1 for i in (strength, intelligence, charisma)):
        return "All stats should be no less than 1"

    if any(x > 4 for x in (strength, intelligence, charisma)):
        return "All stats should be no more than 4"

    if strength + intelligence + charisma == 7:
        return "The character should start with 7 points."


    
    print(name)

create_character('ren', 4, 2, 1)