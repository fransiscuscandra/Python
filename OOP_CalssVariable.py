
class Employee: 

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@company.com' 

        Employee.num_of_emps += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last ) 
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount )

#class variable is a variable(s) that is shared among all instances in class

emp_1 = Employee( 'Corey' , 'Schafer' , 50 )
print(Employee.num_of_emps)
emp_2 = Employee( 'Test' , 'User' , 10 )
print(Employee.num_of_emps)

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

#print(emp_1.__dict__)

print(Employee.__dict__)

Employee.raise_amount = 1.05
emp_1.raise_amount = 1.035 
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
