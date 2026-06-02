class Employee2:
    def __init__(self,firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def email(self):
        return f"{self.firstname}.{self.lastname}@elastic.com"

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split(' ')
        self.firstname = firstname
        self.lastname = lastname

    @fullname.deleter
    def fullname(self):
        print('Deleted Name!')
        self.firstname = None
        self.lastname = None


employee_2 = Employee2('John','Cena')

employee_2.fullname = 'The Rock'
print(employee_2.fullname)
print(employee_2.email)

del employee_2.fullname
print(employee_2.fullname)

