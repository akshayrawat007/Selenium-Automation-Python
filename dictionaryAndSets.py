info = {
    "name": "Akshay",
    "languages": ["java", "python", "javascript"],
    "age": 32
}

print(info["languages"])
info["name"] = "Akshay Rawat" #overwrite
info["bloodgroup"] = "AB+"
print(info)

student = {
    "name": "Vansh",
    "subjects" : {
        "phy": 67.8,
        "chem": 70,
        "maths": 64
    }
}
print(student["subjects"]["chem"])

print(list(student.keys()))
print(student.values())
print(student.items())
# Gives an error when we are trying to extract a key that is not present
print(student.get("name2"))

new_dict = {"city": "Delhi"}
student.update(new_dict)
print(student)

#Set is the collection of unordered  items, Each element in the set must be unique & immutable
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
print(collection)
collection.remove(2)
print(collection)

#Question 1

dict_2 = {}
for i in range(0,3):
    key = input("Enter a key")
    value = input("Enter a value")
    dict_2[key] = value

print(dict_2)

#Question 2
studentsSubject = ["python","java","C++","python","javascript","java","python","java","C++","C"]
classrooms = set(studentsSubject)
print(classrooms)

#Question 3
set2 = {9,"9.0"}
print(set2)

#Function Question

def factorial(number):
    fact = 1
    for k in range(1,number+1):
        fact *= k
        print(fact)


print(factorial(5))

def sumofnaturalnumber(number):
    if number == 0:
        return 0
    else:
        return  number + sumofnaturalnumber(number-1)

print(sumofnaturalnumber(7))








