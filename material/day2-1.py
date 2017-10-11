Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3]
>>> if a:
	print " Contains elements "

	
 Contains elements 
>>> a = []
>>> if a:
	print " Contains elements "

	
>>> a = {}
>>> if a:
	print " Contains elements "

	
>>> None
>>> type(None)
<type 'NoneType'>
>>> a = "hello"
>>> a[::0]

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[::0]
ValueError: slice step cannot be zero
>>> a = { True: "true", False: "false" }
>>> a[True]
'true'
>>> a[0]
'false'
>>> a[1]
'true'
>>> a = { 0.2: "true", 0.1: "false" }
>>> a[0.2]
'true'
>>> a[0.1]
'false'
>>> def varargs(**kwargs):
	print type(kwargs)
	print kwargs

	
>>> varargs(1,2,3)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    varargs(1,2,3)
TypeError: varargs() takes exactly 0 arguments (3 given)
>>> varargs(one=1,two=2,three=3)
<type 'dict'>
{'three': 3, 'two': 2, 'one': 1}
>>> def varargs(*args, **kwargs):
	print type(kwargs)
	print kwargs
	print type(args)
	print args

	
>>> varargs(1,2,3)
<type 'dict'>
{}
<type 'tuple'>
(1, 2, 3)
>>> varargs(one=1,two=2,three=3)
<type 'dict'>
{'three': 3, 'two': 2, 'one': 1}
<type 'tuple'>
()
>>> varargs(1,2,3,one=1,two=2,three=3)
<type 'dict'>
{'three': 3, 'two': 2, 'one': 1}
<type 'tuple'>
(1, 2, 3)
>>> def fullname(fname, lname, title):
	print title + fname + lname

	
>>> fullname ("Aditya", title='Mr', lname ='Prabhakara')
MrAdityaPrabhakara
>>> fullname (fname="Aditya", lname ='Prabhakara', 'Mr')
SyntaxError: non-keyword arg after keyword arg
>>> def varargs(*args =(0,2,3), **kwargs):
	print type(kwargs)
	print kwargs
	print type(args)
	print args
	
SyntaxError: invalid syntax
>>> def varargs(*args, **kwargs):
	print type(kwargs)
	print kwargs
	print type(args)
	print args

	
>>> def fullname(fname, lname, title, age):
	print title + fname + lname + age

	
>>> fullname('A','B','C',20)

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    fullname('A','B','C',20)
  File "<pyshell#43>", line 2, in fullname
    print title + fname + lname + age
TypeError: cannot concatenate 'str' and 'int' objects
>>> def fullname(fname, lname, title, age):
	print title + fname + lname , age

	
>>> fullname('A','B','C',20)
CAB 20
>>> def f1():
	print "Hi"

	
>>> def f1():
	pass

>>> f1()
>>> class Car():
	pass

>>> type(Car)
<type 'classobj'>
>>> a = 0
>>> type(a)
<type 'int'>
>>> type(int)
<type 'type'>
>>> b = Car()
>>> type(b)
<type 'instance'>
>>> class Bus():
	pass

>>> b1 = Bus()
>>> type(b1)
<type 'instance'>
>>> class Car(object):
	pass

>>> class Bus(object):
	pass

>>> swift = Car()
>>> al = Bus()
>>> type(swift)
<class '__main__.Car'>
>>> type(al)
<class '__main__.Bus'>
>>> type(object)
<type 'type'>
>>> type(Car)
<type 'type'>
>>> class A():
	pass

>>> a = A()
>>> dir(a)
['__doc__', '__module__']
>>> a.__module__
'__main__'
>>> a.__doc__
>>> dir(swift)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> a
<__main__.A instance at 0x00000000038C4748>
>>> swift
<__main__.Car object at 0x0000000003976A90>
>>> swift
<__main__.Car object at 0x0000000003976A90>
>>> swift.name = "MS"
>>> dir(swift)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']
>>> swift.name
'MS'
>>> city= Car()
>>> city.name

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    city.name
AttributeError: 'Car' object has no attribute 'name'
>>> city.name = "Honda"
>>> def f(obj, name):
	obj.name=name
	return obj

>>> city = Car()
>>> city = f(city, "Honda")
>>> city.name
'Honda'
>>> swift = Car()
>>> swift = f(swift, "MS")
>>> siwft.name

Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    siwft.name
NameError: name 'siwft' is not defined
>>> swift.name
'MS'
>>> class Car(object):
	def __init__(name):
		pass

	
>>> swift=Car("MS")

Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    swift=Car("MS")
TypeError: __init__() takes exactly 1 argument (2 given)
>>> class Car(object):
	def __init__(self,name):
		pass

	
>>> swift=Car("MS")
>>> class Car(object):
	def __init__(self,name):
		self.name = name

		
>>> class Car(object):
	def __init__(obj,name):
		obj.name = name

		
>>> swift=Car("MS")
>>> swift.name
'MS'
>>> city=Car("Honda")
>>> city.name
'Honda'
>>> Car.__init__(swift,"Maruthi")
>>> swift.name
'Maruthi'
>>> Car.__init__(swift1,"Maruthi")

Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    Car.__init__(swift1,"Maruthi")
NameError: name 'swift1' is not defined
>>> swift.tyres = 5
>>> swift
<__main__.Car object at 0x0000000003976CF8>
>>> class A(object):
	counter = 0

>>> 
>>> obja = A()
>>> obja.counter
0
>>> objb = A()
>>> objb.counter
0
>>> A.counter = 10
>>> obja.counter
10
>>> objb.counter
10
>>> obja.counter = 20
>>> obja.counter
20
>>> objb.counter
10
>>> A.counter = 30
>>> obja.counter
20
>>> objb.counter
30
>>> class A(object):
	counter = 0
	def __init__(self):
		A.counter += 1
		print A.counter, "objects created"

		
>>> obja = A()
1 objects created
>>> objb = A()
2 objects created
>>> objc= A()
3 objects created
>>> class Account(object):
    def __init__(self, n, b, t):
        self.n = n
        self.b = b
        self.t = t

        
>>> ac1 = Account('Aditya',1000,'S')
>>> ac1
<__main__.Account object at 0x0000000003976F28>
>>> l = [1,2,34]
>>> l
[1, 2, 34]
>>> class Account(object):
	def __init__(self, n, b, t):
		self.n = n
		self.b = b
		self.t = t
	def __repr__(self):
		print "Account(" +n + "," + str(b) + ")"

		
>>> class Account(object):
	def __init__(self, n, b, t):
		self.n = n
		self.b = b
		self.t = t
	def __repr__(self):
		return "Account(" +n + "," + str(b) + ")"

	
>>> ac1 = Account('Aditya',1000,'S')
>>> ac1

Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    ac1
  File "<pyshell#176>", line 7, in __repr__
    return "Account(" +n + "," + str(b) + ")"
NameError: global name 'n' is not defined
>>> class Account(object):
	def __init__(self, n, b, t):
		self.n = n
		self.b = b
		self.t = t
	def __repr__(self):
		return "Account(" +self.n + "," + str(self.b) + ")"

	
>>> ac1 = Account('Aditya',1000,'S')
>>> ac1
Account(Aditya,1000)
>>> str(ac1)
'Account(Aditya,1000)'
>>> Account.__repr__(ac1)
'Account(Aditya,1000)'
>>> 'Account({},{})'.format(ac1.n, ac1.b)
'Account(Aditya,1000)'
>>> class Account(object):
	def __init__(self, n, b, t):
		self.n = n
		self.b = b
		self.t = t
	def __repr__(self):
		return 'Account({},{})'.format(self.n, self.b)

	
>>> ac1 = Account('Aditya',1000,'S')
>>> s = 'Aditya'
>>> s
'Aditya'
>>> print s
Aditya
>>> print ac1
Account(Aditya,1000)
>>> class Account(object):
	def __init__(self, n, b, t):
		self.n = n
		self.b = b
		self.t = t
	def __repr__(self):
		return 'Account({},{})'.format(self.n, self.b)
	def __str__(self):
		return '[Account -> {},{}]'.format(self.n, self.b)

	
>>> ac1 = Account('Aditya',1000,'S')
>>> ac1
Account(Aditya,1000)
>>> print ac1
[Account -> Aditya,1000]
>>> str(ac1)
'[Account -> Aditya,1000]'
>>> def sum2n(n):
	if not n:
		return 0
	return n + sum2n(n-1)

>>> sum2n(5)
15
>>> def sum2n(n, acc):
	if not n:
		return acc
	return sum2n(n-1, acc + n)

>>> sum2n(5,0)
15
>>> import greetoct10
>>> dir()
['A', 'Account', 'Bus', 'Car', '__builtins__', '__doc__', '__name__', '__package__', 'a', 'ac1', 'al', 'b', 'b1', 'city', 'f', 'f1', 'fullname', 'greetoct10', 'l', 'obja', 'objb', 'objc', 's', 'sum2n', 'swift', 'varargs']
>>> dir(greetoct10)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'sayhi']
>>> greetoct10.sayhi()
Hi
>>> greetoct10.__doc__
>>> greetoct10.__file__
'greetoct10.py'
>>> greetoct10.__name__
'greetoct10'
>>> greetoct10.__package__
>>> import greetoct10
>>> greetoct10.__doc__
>>> reload(greetoct10)
<module 'greetoct10' from 'greetoct10.py'>
>>> greetoct10.__doc__
' This is just a test module '
>>> greetoct10.sayhi.__doc__
' just a function which says a cheerful Hi'
>>> import greet.py

Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    import greet.py
ImportError: No module named greet.py
>>> import sys
>>> sys.path
['', 'D:\\sw\\Python27\\Lib\\idlelib', 'C:\\Users\\Dell lap\\Desktop\\Python\\lnt\\mysore\\aug-16-17-18-19', 'C:\\WINDOWS\\SYSTEM32\\python27.zip', 'D:\\sw\\Python27\\DLLs', 'D:\\sw\\Python27\\lib', 'D:\\sw\\Python27\\lib\\plat-win', 'D:\\sw\\Python27\\lib\\lib-tk', 'D:\\sw\\Python27', 'D:\\sw\\Python27\\lib\\site-packages', 'D:\\sw\\Python27\\lib\\site-packages\\openpyxl-2.5.0a2-py2.7.egg']
>>> sys.path.append('C:\\Users\\Dell lap\\Desktop\\Python\\oracle\\python-selenium')
>>> sys.path
['', 'D:\\sw\\Python27\\Lib\\idlelib', 'C:\\Users\\Dell lap\\Desktop\\Python\\lnt\\mysore\\aug-16-17-18-19', 'C:\\WINDOWS\\SYSTEM32\\python27.zip', 'D:\\sw\\Python27\\DLLs', 'D:\\sw\\Python27\\lib', 'D:\\sw\\Python27\\lib\\plat-win', 'D:\\sw\\Python27\\lib\\lib-tk', 'D:\\sw\\Python27', 'D:\\sw\\Python27\\lib\\site-packages', 'D:\\sw\\Python27\\lib\\site-packages\\openpyxl-2.5.0a2-py2.7.egg', 'C:\\Users\\Dell lap\\Desktop\\Python\\oracle\\python-selenium']
>>> import greet
>>> greet.sayhi()
Hi from greet module
>>> reload(greet)
<module 'greet' from 'C:\Users\Dell lap\Desktop\Python\oracle\python-selenium\greet.pyc'>
>>> import bank
>>> ac1 = bank.Account('Aditya',10000000,'S')
>>> ac1
<bank.Account object at 0x000000000397E668>
>>> reload(bank)
<module 'bank' from 'C:\Users\Dell lap\Desktop\Python\lnt\mysore\aug-16-17-18-19\bank.pyc'>
>>> ac1 = bank.Account('Aditya',10000000,'S')
>>> ac1
<bank.Account object at 0x000000000397E9B0>
>>> str(ac1)
'<bank.Account object at 0x000000000397E9B0>'
>>> reload(bank)
<module 'bank' from 'C:\Users\Dell lap\Desktop\Python\lnt\mysore\aug-16-17-18-19\bank.pyc'>
>>> sys.path
['', 'D:\\sw\\Python27\\Lib\\idlelib', 'C:\\Users\\Dell lap\\Desktop\\Python\\lnt\\mysore\\aug-16-17-18-19', 'C:\\WINDOWS\\SYSTEM32\\python27.zip', 'D:\\sw\\Python27\\DLLs', 'D:\\sw\\Python27\\lib', 'D:\\sw\\Python27\\lib\\plat-win', 'D:\\sw\\Python27\\lib\\lib-tk', 'D:\\sw\\Python27', 'D:\\sw\\Python27\\lib\\site-packages', 'D:\\sw\\Python27\\lib\\site-packages\\openpyxl-2.5.0a2-py2.7.egg', 'C:\\Users\\Dell lap\\Desktop\\Python\\oracle\\python-selenium']
>>> sys.path.pop(2)
'C:\\Users\\Dell lap\\Desktop\\Python\\lnt\\mysore\\aug-16-17-18-19'
>>> reload(bank)

Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    reload(bank)
ImportError: No module named bank
>>> import bank
>>> reload(bank)

Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    reload(bank)
ImportError: No module named bank
>>> 
