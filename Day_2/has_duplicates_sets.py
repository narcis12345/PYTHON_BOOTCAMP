def has_duplicates (numbers_list):

    set_numbers_list = set(numbers_list)

    if len(numbers_list) > len(set_numbers_list):
        return True
    else:
        return False
    
numbers_list = [1, 2, 1, 4, 5]

result = has_duplicates(numbers_list)
print(result)