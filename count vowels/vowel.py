words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in "aeiuo":
            print(f"the {word} contain the vowel '{letter}'")
            break
    else:
        print(f"the {word} has no vowels")