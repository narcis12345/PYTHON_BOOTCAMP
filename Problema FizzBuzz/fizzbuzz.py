def fizz_buzz_check(n):
    
    modified_list = []
    for number in range(1, n+1):
        if number % 3 == 0 and number % 5 == 0:
            modified_list.append("FizzBuzz")
        elif number % 5 == 0:
            modified_list.append("Buzz")
        elif number % 3 == 0:
            modified_list.append("Fizz")
        else:
            modified_list.append(number)
    return modified_list

n = 15
modified_list = fizz_buzz_check (n)
print(f"The new list is: {modified_list}")
