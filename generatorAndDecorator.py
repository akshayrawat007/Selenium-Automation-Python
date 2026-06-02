

def square_numbers(my_num):
    for i in my_num:
        yield (i*i)

numbers2 = square_numbers([1,2,3,4,5])
print(next(numbers2))
print(next(numbers2))
print(next(numbers2))
print(next(numbers2))
print(next(numbers2))

# list comprehension
result = [y*y for y in [1,2,3,4,5]]
print(result)