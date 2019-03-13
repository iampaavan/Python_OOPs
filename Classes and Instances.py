# Python OOPS concepts

class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
	
	def fullname(self):
		return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Paavan', 'Gopala', 50000)
emp_2 = Employee('Test', 'User', 60000)

# using the instance, call the fullname method --> requires no argument
#emp_1.fullname()

# using class to call the fullname method --> requires us to pass the employee as the arg
print(Employee.fullname(emp_1))

emp_1.pay = 60000
#print('Employee email is: ' + emp_1.email)
#print('Pay of employee: ' + emp_1.fullname() + ' is $', emp_1.pay)
#print(emp_1.fullname())
#print(emp_2.fullname())
