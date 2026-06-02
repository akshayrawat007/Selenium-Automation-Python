# import pdb
# pdb.set_trace()

class Hello:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    def __repr__(self):
        return "This is secondary"

h1 = Hello('Akshay',45)
print(h1)

