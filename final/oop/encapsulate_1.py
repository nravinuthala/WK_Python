class Employee:
    __count = 0;
    def __init__(self, salary):
        self.__salary = salary
        Employee.__count = Employee.__count+1

    def display(self):
        print(f"The number of employees {Employee.__count}")
        print(f"My salary is {self.__salary}")

    def increment_salary(self, inc):
        self.__salary += inc

emp = Employee(10000)
emp2 = Employee(12000)

try:
    print(emp.__count)
    print(emp.__salary)
    print(_Employee__salary)
    emp.__salary += 30000
except: print("Attribute error")
finally:
    emp.display()
    emp.increment_salary(50000)
    emp.display()