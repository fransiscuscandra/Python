class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + "." + last + "@company.com"

    @property  # this is property decorator
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")
emp_1.first = "Jim"

emp_1.fullname = "King Kong"

print(emp_1.first)
print(emp_1.email)  # with @property, email method is execute like attribute
# print(emp_1.email()) # this is the command if u dont have @property
print(emp_1.fullname)  # this command with @property decorator
# print(emp_1.fullname()) #this command without @property decorator

del emp_1.fullname
print(emp_1.fullname)
