Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.findall(r"Showing (\d)+ to (\d)+ of (\d)+", "Showing 1 to 3 of 3 (1 Pages)")
[('1', '3', '3')]
>>> raise ValueError("Some value is wrong")

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    raise ValueError("Some value is wrong")
ValueError: Some value is wrong
>>> raise Exception("Some generic exception")

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    raise Exception("Some generic exception")
Exception: Some generic exception
>>> err = ValueError("Some value")
>>> err
ValueError('Some value',)
>>> raise err

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    raise err
ValueError: Some value
>>> isinstance(err, ValueError)
True
>>> isinstance(err, Exception)
True
>>> class InsufficientBalanceError(Exception):
	pass

>>> raise InsufficientBalanceError("Please check your balance")

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    raise InsufficientBalanceError("Please check your balance")
InsufficientBalanceError: Please check your balance
>>> import calc
9
>>> calc.adder(5,6)
11
>>> reload(calc)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    reload(calc)
  File "C:\Users\Dell lap\Desktop\Python\oracle\python-selenium\calc.py", line 6, in <module>
    print adder(int(sys.argv[1]),int(sys.argv[2]))
IndexError: list index out of range
>>> calc
<module 'calc' from 'C:\Users\Dell lap\Desktop\Python\oracle\python-selenium\calc.py'>
>>> calc.__name__
'calc'
>>> reload(calc)
<module 'calc' from 'C:\Users\Dell lap\Desktop\Python\oracle\python-selenium\calc.py'>
>>> calc.adder(7,8)
15
>>> from calc import sub

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    from calc import sub
ImportError: cannot import name sub
>>> from calc2 import add

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    from calc2 import add
ImportError: cannot import name add
>>> from calc2 import adder
>>> reload(calc2)

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    reload(calc2)
NameError: name 'calc2' is not defined
>>> import re
>>> p = 'text'
>>> s = 'does not contain'
>>> re.search(p, t)

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    re.search(p, t)
NameError: name 't' is not defined
>>> re.search(p, s)
>>> s = s +
SyntaxError: invalid syntax
>>> s = s + " text
SyntaxError: EOL while scanning string literal
>>> s = s + " text"
>>> s
'does not contain text'
>>> re.search(p, s)
<_sre.SRE_Match object at 0x0000000002F684A8>
>>> m  = re.search(p, s)
>>> m
<_sre.SRE_Match object at 0x0000000002F68578>
>>> m.start()
17
>>> m.end()
21
>>> s[m.start(), m.end()]

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s[m.start(), m.end()]
TypeError: string indices must be integers, not tuple
>>> s[m.start(): m.end()]
'text'
>>> s
'does not contain text'
>>> s[17:21]
'text'
>>> t = s + " text"
>>> t
'does not contain text text'
>>> m  = re.search(p, t)
>>> m.start(), m.end()
(17, 21)
>>> re.findall(p, t)
['text', 'text']
>>> for m in re.finditer(p, t):
	print "found at", m.start(), m.end()

	
found at 17 21
found at 22 26
>>> m.string
'does not contain text text'
>>> p = 'sas'
>>> t ='sasasas'
>>> re.findall(p, t)
['sas', 'sas']
>>> p = 'ab*'
>>> t = 'abbbababbbbbbbbababab'
>>> t = 'abbbababbbbbbbbabababaaa'
>>> re.findall(p,t)
['abbb', 'ab', 'abbbbbbbb', 'ab', 'ab', 'ab', 'a', 'a', 'a']
>>> p= 'ab+'
>>> t = 'abbbababbbbbbbbabababaaa'
>>> re.findall(p,t)
['abbb', 'ab', 'abbbbbbbb', 'ab', 'ab', 'ab']
>>> p = 'ab?'
>>> t = 'abbbababbbbbbbbabababaaa'
>>> re.findall(p,t)
['ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'a', 'a', 'a']
>>> p = 'ab{3}'
>>> t = 'abbbababbbbbbbbabababaaa'
>>> re.findall(p,t)
['abbb', 'abbb']
>>> p = 'a[ab]+'
>>> t = 'abbbababbbbbbbbabababaaa'
>>> re.findall(p,t)
['abbbababbbbbbbbabababaaa']
>>> t = 'abbbababbbbbbsbbabababaaa'
>>> p = 'a[ab]+'
>>> re.findall(p,t)
['abbbababbbbbb', 'abababaaa']
>>> p = 'a[ab]+?'
>>> re.findall(p,t)
['ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'aa']
>>> t='http:\\www.google.com'
>>> p = 'http'
>>> re.findall(p,t)
['http']
>>> t=':\\www.httpgoogle.com'
>>> re.findall(p,t)
['http']
>>> p = '^http'
>>> t=':\\www.httpgoogle.com'
>>> re.findall(p,t)
[]
>>> t='http:\\www.google.com'
>>> re.findall(p,t)
['http']
>>> p = 'com$'
>>> t='http:\\www.google.com'
>>> re.findall(p,t)
['com']
>>> p = 'a(ab)*'
>>> t = 'ababababababab'
>>> re.findall(p,t)
['', '', '', '', '', '', '']
>>> p = 'a(ab)+'
>>> re.findall(p,t)
[]
>>> t = 'abababababababaab'
>>> re.findall(p,t)
['ab']
>>> p = 'a(ab)*'
>>> t = 'abababababababaabab'
>>> re.findall(p,t)
['', '', '', '', '', '', '', 'ab']
>>> p = 'a(ab{3})*'
>>> t = 'abababababababaabbbab'
>>> re.findall(p,t)
['', '', '', '', '', '', '', 'abbb', '']
>>> p ='^[a-z0-9_-]{3,16}$'
>>> t ='om'
>>> re.findall(p,t)
[]
>>> t ='omi'
>>> re.findall(p,t)
['omi']
>>> t ='omi+'
>>> re.findall(p,t)
[]
>>> t ='omilasjdlf'
>>> re.findall(p,t)
['omilasjdlf']
>>> t ='omilasjdlfASDF'
>>> re.findall(p,t)
[]
>>> re.findall(p,t,re.IGNORECASE)
['omilasjdlfASDF']
>>> t ='omilasjdlfASDFasdfasdfasfwr'
>>> len(t)
27
>>> re.findall(p,t,re.IGNORECASE)
[]
>>> p ='^[a-zA-Z0-9_-]{3,16}$'
>>> re.findall(p,t,re.IGNORECASE)
[]
>>> t ='omilasjdlfASDF'
>>> re.findall(p,t)
['omilasjdlfASDF']
>>> t = 'man eats mango'
>>> p = 'man|mango'
>>> t = 'man eats mango'
>>> re.findall(p,t)
['man', 'man']
>>> p = 'mango|man'
>>> re.findall(p,t)
['man', 'mango']
>>> p = 'man(go)?'
>>> re.findall(p,t)
['', 'go']
>>> p = '(man(go)?)'
>>> re.findall(p,t)
[('man', ''), ('mango', 'go')]
>>> p = 'man(go)?'
>>> re.findall(p,t)
['', 'go']
>>> for m in re.finditer(p,t):
	print m.group

	
<built-in method group of _sre.SRE_Match object at 0x0000000002F63210>
<built-in method group of _sre.SRE_Match object at 0x0000000002F63288>
>>> for m in re.finditer(p,t):
	print m.group()

	
man
mango
>>> p = "man[mango]*"
>>> t
'man eats mango'
>>> re.findall(p,t)
['man', 'mango']
>>> t = 'man eats mango at manm hotel'
>>> re.findall(p,t)
['man', 'mango', 'manm']
>>> 
