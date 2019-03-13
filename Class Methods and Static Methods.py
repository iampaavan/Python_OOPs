# Python OOPS concepts
import datetime


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
		# self.pay = int(self.pay * Employee.raise_amount)
		self.pay = int( self.pay * self.raise_amount )
		return self.pay
	
	@classmethod
	def set_apply_raise(cls, amount):
		cls.raise_amount = amount
		
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)
	
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


my_date = datetime.date(2019, 2, 18)


print('Total no. of employees initially: ', Employee.num_of_employees)

emp_1 = Employee('Paavan', 'Gopala', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'manjula-subramanyamachary-10000'
emp_str_2 = 'Thilak-Yajaman-20000'
emp_str_3 = 'Tester-Method-30000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print('Total no. of employees currently: ', Employee.num_of_employees)

Employee.set_apply_raise(1.06)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(new_emp_1.email)
print(new_emp_1.fullname())

print(Employee.is_workday(my_date))
