words = ["apple", "banana", "cherry", "date", "elderberry"]

for word in words:
    if "a" in word:
        words.remove(word)

print(words)


#corrected 
words = ["apple", "banana", "cherry", "date", "elderberry"]

for word in words[:]:  # Iterate over a copy
    if "a" in word:
        words.remove(word)

print(words)  

