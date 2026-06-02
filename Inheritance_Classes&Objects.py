import datetime

class Employee:

    raise_amount = 1.08
    def __init__(self,firstname, lastname, paycheck):
        self.firstname = firstname
        self.lastname = lastname
        self.paycheck = paycheck
        self.email = firstname + '.' + lastname + '@elastic.com'

    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def apply_raise(self):
        self.paycheck = int(self.paycheck * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        firstname, lastname, paycheck = emp_str.split('-')
        return cls(firstname, lastname, paycheck)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Akshay', 'Rawat', 28000)
emp2 = Employee("Vansh","Sapra",80000)
print(emp1.email)
print(emp1.paycheck)
print(emp2.email)
print(emp2.paycheck)
print(emp1.fullname())
# When we are passing the instance as parameter explicitly
print(Employee.fullname(emp1))

print(emp1.paycheck)
print(emp1.__dict__)
emp1.apply_raise()
print(emp1.paycheck)
print(emp1.raise_amount)
print(Employee.__dict__)
print(emp2.raise_amount)
emp1.raise_amount = 1.09
print(Employee.raise_amount)
print(emp1.raise_amount)

str_emp1 = 'Sagar-Rawat-50000'
new_str_1 = Employee.from_string(str_emp1)
print(new_str_1.fullname())

my_date = datetime.date(2026,5,23)
print(Employee.iswork_day(my_date))

class Developer(Employee):
    def __init__(self,firstname,lastname,paycheck,prog_lang):
        # option1 to call parent class constructor
        super().__init__(firstname,lastname, paycheck)
        # option2 to call parent class constructor
        Employee.__init__(self,firstname,lastname,paycheck)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,firstname,lastname,paycheck,employees=None):
        super().__init__(firstname,lastname,paycheck)
        if employees is None:
            self.employees = []
        self.employees = employees

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())


developer_1 = Developer("Sagar","Rawat",50000,'Python')
developer_2 = Developer("Karan","Rawat",85000,'Java')
developer_1.iswork_day(my_date)
print(help(Developer))
print(developer_1.email)
print(developer_1.prog_lang)

manager_1 = Manager('Aishwarya','Rawat',140000,[developer_1])
print(manager_1.fullname())
manager_1.add_employee(developer_1)
manager_1.add_employee(developer_2)
manager_1.print_employees()
print(developer_1)


