sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word in sentence:
    print("Word found in sentence")
else:
    print("Word not found in sentence")