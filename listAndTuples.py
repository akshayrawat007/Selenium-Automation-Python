
names = ["Akshay","Rawat",34,66,"Vansh"]
for i in names:
    print(i)

names.append("Abhay")
for i in names:
    print(i)


names2 = [4,34,7,1,17,34,8]
# names2.reverse()
# for i in names2:
#     print(i)
print(names2)
names2.insert(3,88)
print(names2)
names2.pop(0)
print(names2)
names2.remove(34)
names3 = names2.copy()
print(names3)


# tuple
tup = (2,1,4,7,4)
print(tup[4])
print(type(tup))

print(tup[-3:-1])
print(tup.index(4))
print(tup.count(4))

 # Need to add comma for single element
tup1 = (7,)
print(type(tup1))

# Question1

movies = []
for i in range(3):
    movie = input("Enter movie name: ")
    movies.append(movie)

print(movies)

# Question 2
palindrome = [1,2,3,2,3]
palindrome2 = palindrome.copy()
palindrome2.reverse()
if palindrome == palindrome2:
    print("It is a pallindrome")

firstKey = 0
lastKey = len(palindrome) - 1
is_palindrome = True
while firstKey < lastKey:
    if palindrome[firstKey] != palindrome[lastKey]:
        is_palindrome = False
        break

    firstKey += 1
    lastKey -= 1
if is_palindrome:
        print("Palindrome")
else:
        print("Not Palindrome")

# Question 3

tup4 = ["C","D","A","A","B","B","A"]
tup4.sort()
count = 0
for i in tup4:
    if i =='A':
        count+=1

print(count)
print(tup4)





