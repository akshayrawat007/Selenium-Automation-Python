# Question 1
def calculate_upper_and_lower_letters(word):
    upper_letters_count = 0
    lower_letters_count = 0
    for i in word:
        if i == " ":
            continue
        elif i.isupper():
            upper_letters_count += 1
        elif i.islower():
            lower_letters_count += 1
        # handling edge case
        else:
            raise ValueError("Not a letter")
    return upper_letters_count, lower_letters_count

upper_letters, lower_letters = calculate_upper_and_lower_letters('AkshAy RawaT')
print(f'Upper case letters: {upper_letters}')
print(f'Lower case letters: {lower_letters}')


#Question 2
#Option 1
def unique_elements_extraction1(list1):
    unique_list = []
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

# Option 2 , directly typecasting into set and then back to list
def unique_elements_extraction2(list2):
    list1 = set(list2)
    return list(list1)

print(unique_elements_extraction1(["Java","C++","Python","C++","C","JavaScript","Java","Python"]))
print(unique_elements_extraction2(["Java","C++","Python","C++","C","JavaScript","Java","Python"]))


#Question 3
def palindrome_check(list3):
    first_pointer = 0
    last_pointer = len(list3) -1
    is_palindrome = True
    while first_pointer < last_pointer:
        if list3[first_pointer] == list3[last_pointer]:
            first_pointer += 1
            last_pointer -= 1
        else:
            is_palindrome = False
            print("Not a palindrome")
            break
    if is_palindrome: print('Palindrome')
    return is_palindrome

print(palindrome_check([1,2,3,3,3,2,1])) # odd count
print(palindrome_check([2,2,4,4,4,4,2,2])) # even count
print(palindrome_check([1,8,9,8,7])) # not a palindrome


#Question 4
temperature = float(input("Temperature is: "))
type_0f_temp = input(
    "Type 'C' for celsius to fahrenheit or 'F' for fahrenheit to celsius: "
)
if type_0f_temp.upper() == "C":
    fahrenheit = (temperature * 9/5) + 32
    print(f"Temperature in fahrenheit: {fahrenheit}")
elif type_0f_temp.upper() == "F":
    celsius = (temperature - 32) * 5/9
    print(f"Temperature in celsius: {celsius}")
else:
    raise ValueError("Invalid type of temperature")


#Question 5
def fibonacci_series():
    first_value = 0
    second_value = 1
    fibonacci_list = []
    while first_value <= 50:
        fibonacci_list.append(first_value)
        next_value = first_value + second_value
        first_value = second_value
        second_value = next_value
    return fibonacci_list

print(fibonacci_series())


#Question 6
def print_missing_number(input_list):
    start = input_list[0]
    end = input_list[len(input_list)-1]
    for i in range(start,end+1):
        if i not in input_list:
            print("Missing number is: ", i)
            break

# Taking random raw list with default comma-separated
list5 = list(map(int, input("Enter the list: ").split(",")))
# Passing the list as raw
# print_missing_number([10,11,12,13,14,16,17,18,19,20])
print_missing_number(list5)


#Question 7
class IntegerAndRoman:

    # Converted to static method as no class or instance variables are being crated or used
    @staticmethod
    def convert_integer_to_roman(number):
        roman_values = {
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        roman_numeral = ""
        for value, roman_symbol in roman_values.items():
            while number >= value:
                roman_numeral += roman_symbol
                number -= value
        return roman_numeral

obj1 = IntegerAndRoman()
print(obj1.convert_integer_to_roman(67))
print(obj1.convert_integer_to_roman(23))
print(obj1.convert_integer_to_roman(99))


#Question 8
class ReversalOfString:

    def __init__(self):
        pass

    # Converted to static method as no class or instance variables are being crated or used
    @staticmethod
    def reverse_words(sentence):
        words = sentence.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

reversal = ReversalOfString()
print(reversal.reverse_words("Akshay Rawat Cypress Infra"))

