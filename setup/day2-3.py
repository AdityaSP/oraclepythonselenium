Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from bank import Account
>>> reload(Account)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    reload(Account)
TypeError: reload() argument must be module
>>> dir
<built-in function dir>
>>> from bank reload Account
SyntaxError: invalid syntax
>>> dir()
['Account', '__builtins__', '__doc__', '__name__', '__package__']
>>> reload(bank)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    reload(bank)
NameError: name 'bank' is not defined
>>> from bank import Account
>>> Account.__doc__
' Base Account Class '
>>> from bank import Account
>>> Account.__doc__
' Base Account Class '
>>> from bank import Account
>>> Account.__doc__
' Base Account Class '
>>> del Account
>>> from bank import Account
>>> Account.__doc__
' Base Account Class '
>>> del Account
>>> Account.__doc__

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    Account.__doc__
NameError: name 'Account' is not defined
>>> reload(bank)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    reload(bank)
NameError: name 'bank' is not defined
>>> Account.__doc__

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    Account.__doc__
NameError: name 'Account' is not defined
>>> import bank
>>> from bank import Account
>>> Account.__doc__
' Base Account Class '
>>> del Account
>>> from bank import Account
>>> Account.__doc__
' Base Account Class '
>>> class LB(object):
	def breathe(self):
		print "I breathe"

		
>>> l = LB()
>>> l.breathe()
I breathe
>>> class HB(object):
	def breathe(self):
		print "I breathe"

		
>>> h = HB()
>>> h.breathe()
I breathe
>>> class HB(LB):
	pass

>>> h = HB()
>>> h.breathe()
I breathe
>>> class HB(object):
	def breathe(self):
		print "I breathe"
	def metathink(self):
		print "I Think therefore I am"

		
>>> class HB(LB):
	def metathink(self):
		print "I Think therefore I am"

		
>>> h = HB()
>>> h.breathe()
I breathe
>>> h.metathink()
I Think therefore I am
>>> l.breathe()
I breathe
>>> l.metathink()

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    l.metathink()
AttributeError: 'LB' object has no attribute 'metathink'
>>> class Fish(LB):
	def breathe(self):
		print "Breathe through gills"

		
>>> f= Fish()
>>> f.breathe()
Breathe through gills
>>> h.breathe()
I breathe
>>> reload(bank)
<module 'bank' from 'C:\Users\Dell lap\Desktop\Python\oracle\python-selenium\bank.py'>
>>> sa = SavingsAccount('Aditya',1000,'S')

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    sa = SavingsAccount('Aditya',1000,'S')
NameError: name 'SavingsAccount' is not defined
>>> sa = bank.SavingsAccount('Aditya',1000,'S')
>>> ca = bank.CurrentAccount('abc pvt', 1000, 'C')
>>> sa
SA(Aditya,1000)
>>> ca
CA(abc pvt,1000)
>>> sa.debit(5000)

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    sa.debit(5000)
  File "C:\Users\Dell lap\Desktop\Python\oracle\python-selenium\bank.py", line 32, in debit
    raise ValueError("Insufficient Balance")
ValueError: Insufficient Balance
>>> ca.debit(5000)
>>> ca
CA(abc pvt,-4000)
>>> issubclass
<built-in function issubclass>
>>> reload(bank)
<module 'bank' from 'C:\Users\Dell lap\Desktop\Python\oracle\python-selenium\bank.py'>
>>> sa = bank.SavingsAccount('Aditya',1000)
>>> ca = bank.CurrentAccount('abc pvt', 1000)
>>> sa
SA(Aditya,1000)
>>> ca
CA(abc pvt,1000)
>>> ca.debit(5000)
>>> sa.debit(5000)

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    sa.debit(5000)
  File "C:\Users\Dell lap\Desktop\Python\oracle\python-selenium\bank.py", line 33, in debit
    raise ValueError("Insufficient Balance")
ValueError: Insufficient Balance
>>> isinstance(ca,CurrentAccount)

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    isinstance(ca,CurrentAccount)
NameError: name 'CurrentAccount' is not defined
>>> isinstance(ca,bank.CurrentAccount)
True
>>> isinstance(ca,bank.SavingsAccount)
False
>>> isinstance(ca,bank.Account)
True
>>> isinstance(sa,bank.CurrentAccount)
False
>>> isinstance(sa,bank.SavingsAccount)
True
>>> isinstance(sa,bank.Account)
True
>>> iss

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    iss
NameError: name 'iss' is not defined
>>> issubclass(Account, SavingsAccount)

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    issubclass(Account, SavingsAccount)
NameError: name 'SavingsAccount' is not defined
>>> issubclass(bank.Account, bank.SavingsAccount)
False
>>> issubclass(bank.SavingsAccount, bank.Account)
True
>>> class A(object):
	pass

>>> def f(self):
	print "In f"

	
>>> A.f = f
>>> a = A()
>>> a.f()
In f
>>> class A(object):
	pass

>>> a = A()
>>> a.f = f
>>> a.f()

Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.f()
TypeError: f() takes exactly 1 argument (0 given)
>>> def f():
	print "In f"

	
>>> a.f = f
>>> a.f()
In f
>>> reload(bank)
<module 'bank' from 'C:\Users\Dell lap\Desktop\Python\oracle\python-selenium\bank.py'>
>>> sa = bank.SavingsAccount('Aditya',1000)
>>> sa.credit(1000).debit(500).credit(1000)
SA(Aditya,2500)
>>> class Hotel(object):
	def pay(self):
		print "Paid"
		return self
	def order(self):
		print "Note order"
		return self
	def eat(self):
		print "Yummy"
		return self
	def feedback(self):
		print "Give feedback"
		return self

	
>>> slv = Hotel()
>>> slv.order().pay().eat().feedback()
Note order
Paid
Yummy
Give feedback
<__main__.Hotel object at 0x0000000002CCCE10>
>>> slv.pay().order().eat().feedback()
Paid
Note order
Yummy
Give feedback
<__main__.Hotel object at 0x0000000002CCCE10>
>>> 
