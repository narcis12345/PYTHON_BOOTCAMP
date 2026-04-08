def count_letters(text):
    letter_dictionary = {}
    
    for letter in text:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1
    
    return letter_dictionary

result = count_letters("softwire soft")
print(result)