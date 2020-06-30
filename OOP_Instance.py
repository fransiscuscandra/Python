
class Employee: 
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@company.com' 

    def fullname(self):
        return '{} {}'.format(self.first, self.last ) 

emp_1 = Employee( 'Corey' , 'Schafer' , 50 )
emp_2 = Employee( 'Test' , 'User' , 10 )

name = Employee.fullname(emp_1) 
print(name)
print(emp_1.email)
print(emp_2.email)
#print('{} {}'.format(emp_1.first, emp_1.last ) )
name2 = emp_2.fullname()
print(name2) 

#print(emp_1)
#print(emp_2)

#emp_1.first = 'Corey'
#emp_1.last = 'Schafer'
#emp_1.email = 'Corey.Schaefer@company.com'
#emp_1.pay = 50

#emp_2.first = 'Test'
#emp_2.last = 'User'
#emp_2.email = 'Test.User@company.com'
#emp_2.pay = 10 

#print(emp_1.email)
#print(emp_2.email)
