class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raised_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)


emp_1 = Employee("Corey", "Schafer", 50)
emp_2 = Employee("Test", "User", 10)

# Employee.set_raised_amt(1.05)
# emp_2.set_raised_amt(1.07)
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

emp_str_1 = "John-Doe-70"
emp_str_2 = "Steve-Smith-30"
emp_str_3 = "Jane-Doe-90"

# first, last, pay = emp_str_1.split("-")
# print(first, last, pay)
# new_emp_1 = Employee(first, last, pay)
# print(new_emp_1.first, new_emp_1.last, new_emp_1.email)
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.first, new_emp_1.last, new_emp_1.pay)
