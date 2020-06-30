class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):  # dunnder = double underline
        return "Employee('{}', '{}', {} )".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    # example of adding time
    # def __addtime__(self, other):
    #     if isinstance(other, timedelta):
    #         return timedelta(self._days + other._days ,
    #                          self._seconds + other._seconds ,
    #                          self._microseconds + other._microseconds )
    #     return NotImplemented


emp_1 = Employee("Tom", "Cruse", 50)
emp_2 = Employee("Freeman", "Jack", 40)

# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# sample of using dunner add (__add__)
# more information in link https://docs.python.org/3/reference/datamodel.html
print(emp_1 + emp_2)
# same with
print(len("test"))
print("test".__len__())

print(len(emp_1))
