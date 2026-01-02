#10
class Employee:
    antalEmployee = 500
    def __init__(self, name):
        self.__company_name = "Nasdaq"
        self.name = name
        Employee.antalEmployee += 1
    def get_info(self):
        return f'I work in {self.__company_name}. \nIt has {Employee.antalEmployee} employees.'

class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def get_info(self):
        return f"{super().get_info()} \nI'am {Employee.antalEmployee}th employee Developer. \nMy salary is {self.salary}\n"


class Intern(Employee):
    def __init__(self, name, duration):
        super().__init__(name)
        self.duration = duration
    def get_info(self):
        return f"{super().get_info()} \nI will stay for {self.duration} months\n"


e1 = Developer('Fortuna', 35000)
print(e1.get_info())

e2 = Intern('Fortuna', 3)
print(e2.get_info())
