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
		self.pay = int(self.pay * self.raise_amount)
		return self.pay
	

class Developer(Employee):
	raise_amount = 1.10
	
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		# Employee.__init__(self. first, last, pay)
		self.prog_lang = prog_lang
		
		
class Manager(Employee):
	
	def __init__(self, first, last, pay, employees = None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees
		
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)
			
	def rem_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
			
	def print_emp(self):
		for emp in self.employees:
			print('-->', emp.fullname())
			
			
dev_1 = Developer('Paavan', 'Gopala', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')
dev_3 = Developer('Manula', 'Subramanyam', 70000, 'Java-Selenium')

mgr_1 = Manager('Asvini', 'Yekkelli', 90000, [dev_1, dev_2])
print(mgr_1.email)

mgr_1.add_emp(dev_3)
#mgr_1.rem_emp(dev_1)
mgr_1.print_emp()

print(dev_1.email)
print(dev_1.prog_lang)

print(dev_1.pay)
# Developer.apply_raise(dev_1)
dev_1.apply_raise()
print(dev_1.pay)

print(isinstance(mgr_1, Employee))
print(issubclass(Developer, Employee))
