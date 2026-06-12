# def get_weather(temp):
#     if temp > 20:
#         return "hot"
#     else:
#         return "cold"
#
# def add(a,b):
#     return a + b
#
# def divide(a,b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a / b
#
#
# class UserManager:
#     def __init__(self):
#         self.users = {}
#
#     def add_user(self,username, email):
#         if username in self.users:
#             raise ValueError("User already exists")
#         self.users[username] = email
#         return True
#
#     def get_user(self,username):
#         return self.users.get(username)
#
#
class ComplexNumber:

    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __add__(self, other):
        real_part = self.real + other.real
        img_part = self.img + other.img
        return ComplexNumber(real_part,img_part)

    def __str__(self):
        return f"{self.real}i + {self.img}j"


c1 = ComplexNumber(4,5)
c2 = ComplexNumber(6,7)
result = c1 + c2
print(result)

#
#
#
#
#
#
#
#
