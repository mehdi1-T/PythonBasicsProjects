def number_of_words(text):
    return text.split(" ")
    
def number_of_characters(words):    
    return sum(len(word) for word in words)

def number_of_sentences(text):
    return text.split(".")

def longest_word(words):
    longest = ""
    for i in range(len(words)):
        if len(words[i]) > len(longest):
            longest = words[i]
    return longest

def shorter_word(words):
    shorter = words[0]
    for i in range(len(words)):
        if len(words[i]) < len(shorter):
            shorter = words[i]
    return shorter

def vowels_percentage(text, vowels):
    total_vowels = 0
    for char in text:
        if char.lower() in vowels:
            total_vowels += 1
    clean_text = text.replace(" ","")
    percentage = (total_vowels / len(clean_text)) * 100
    return percentage


vowels = ["e", "i", "u", "a", "o"]
text = input("Text: ").strip()

words = number_of_words(text)
characters = number_of_characters(words)
sentences = number_of_sentences(text)
longestWord = longest_word(words)
shorterWord = shorter_word(words)
vowels = vowels_percentage(text, vowels)


print(f"Words: {words}")
print(f"characters: {characters}")
print(f"sentences: {sentences}")
print(f"longest Word: {longestWord}")
print(f"shorter Word: {shorterWord}")
print(f"vowels percentage: {vowels}")