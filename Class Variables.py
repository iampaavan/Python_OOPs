# Python OOPS concepts

class Employee:
	
	num_of_employees = 0
	raise_amount = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
	
		Employee.num_of_employees += 1
	
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * Employee.raise_amount)
		#self.pay = int( self.pay * self.raise_amount )
		return self.pay

print('Total no. of employees initially: ', Employee.num_of_employees)

emp_1 = Employee('Paavan', 'Gopala', 50000)
emp_2 = Employee('Test', 'User', 60000)

print('Total no. of employees currently: ', Employee.num_of_employees)

emp_1.raise_amount = 1.05

print('Percent of raise for Emp_1: ', emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)


#print(emp_1.pay)
#print(emp_1.apply_raise())
#print(Employee.apply_raise(emp_1))
#print(emp_1.__dict__)
#rint(Employee.__dict__)
