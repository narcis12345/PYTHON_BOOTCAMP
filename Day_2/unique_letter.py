def unique_letter (text):
    
    letter_dictionary = {}

    for letter in text:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1
    
    for letter in text:
        if letter_dictionary[letter] == 1:
            return letter
    
    return 0

text = "aabbccddeeffg"

result = unique_letter(text)

if result == 0:
    print("In this text there are no unique letters")
else:
    print(f"In this text the first unique letter is {result}")
