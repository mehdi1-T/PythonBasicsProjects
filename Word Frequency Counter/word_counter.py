def word_counter(words):
    result = []
    for word in words:
        counter = words.count(word)
        result.append([word, counter])
        for i in range(len(result)):
            for j in range(i+1, len(result)):
                if result[i] == result[j]:
                    del result[j]
    return result

words = ["hello","world","hello"]
words2 = ["apple", "banana", "apple", "orange", "banana", "apple"]

result = word_counter(words2)
print(result)