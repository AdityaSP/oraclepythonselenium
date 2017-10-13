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
p = '(man(go)?)'
>>> re.findall(p,t)
[('man', ''), ('mango', 'go'), ('man', '')]
>>> p = '(man(go)?)'
>>> t = 'man eats mango'
>>> re.findall(p,t)
[('man', ''), ('mango', 'go')]
>>> p = 'man(go)?'
>>> re.findall(p,t)
['', 'go']
>>> for m in re.finditer(p,t):
	print m.group()
	print m.groups(0)

	
man
(0,)
mango
('go',)
>>> for m in re.finditer(p,t):
	print m.group()
	print m.groups(1)

	
man
(1,)
mango
('go',)
>>> for m in re.finditer(p,t):
	print m.group()
	print m.groups

	
man
<built-in method groups of _sre.SRE_Match object at 0x0000000002F63210>
mango
<built-in method groups of _sre.SRE_Match object at 0x0000000002F63288>
>>> for m in re.finditer(p,t):
	print m.group()
	print m.group(1)

	
man
None
mango
go
>>> t = 'Showing 1 to 3 of 3 (1 Pages)'
>>> p ="c:\name"
>>> p
'c:\name'
>>> print p
c:
ame
>>> p =r"c:\name"
>>> print p
c:\name
>>> p = '''c:\name'''
>>> print p
c:
ame
>>> t
'Showing 1 to 3 of 3 (1 Pages)'
>>> 'Showing 13 to 300 of 3000 (5 Pages)'
'Showing 13 to 300 of 3000 (5 Pages)'
>>> t
'Showing 1 to 3 of 3 (1 Pages)'
>>> p = r"Showing ([0-9]+) to ([0-9]+) of ([0-9]+) \(([0-9]+) Pages \)'
SyntaxError: EOL while scanning string literal
>>> p = r"Showing ([0-9]+) to ([0-9]+) of ([0-9]+) \(([0-9]+) Pages \)"
>>> p
'Showing ([0-9]+) to ([0-9]+) of ([0-9]+) \\(([0-9]+) Pages \\)'
>>> re.findall(p,t)
[]
>>> t
'Showing 1 to 3 of 3 (1 Pages)'
>>> p = r"Showing ([0-9]+) to ([0-9]+) of ([0-9]+) \(([0-9]+) Pages\)"
>>> re.findall(p,t)
[('1', '3', '3', '1')]
>>> t
'Showing 1 to 3 of 3 (1 Pages)'
>>> t = t + t
>>> t
'Showing 1 to 3 of 3 (1 Pages)Showing 1 to 3 of 3 (1 Pages)'
>>> p
'Showing ([0-9]+) to ([0-9]+) of ([0-9]+) \\(([0-9]+) Pages\\)'
>>> re.findall(p,t)
[('1', '3', '3', '1'), ('1', '3', '3', '1')]
>>> 'Showing ([0-9]+) to ([0-9]+) of ([0-9]+) \\(([0-9]+) Pages\\)'
'Showing ([0-9]+) to ([0-9]+) of ([0-9]+) \\(([0-9]+) Pages\\)'
>>> t
'Showing 1 to 3 of 3 (1 Pages)Showing 1 to 3 of 3 (1 Pages)'
>>> t = 'Showing 1 to 3 of 3 (1 Pages)Showing 10 to 32 of 35 (100 Pages)'
>>> re.findall(p,t)
[('1', '3', '3', '1'), ('10', '32', '35', '100')]
>>> t ='Showing 1 to 3 of 3 (1 Pages)'
>>> re.findall(p,t)
[('1', '3', '3', '1')]
>>> re.findall(p,t)[0]
('1', '3', '3', '1')
>>> re.findall(p,t)[0][2]
'3'
>>> t ='Showing 17 to 38 of 34 (18 Pages)'
>>> p = r"Showing (\d)+ to (\d)+ of ([0-9]+) \(([0-9]+) Pages\)"
>>> re.findall(p,t)[0][2]
'34'
>>> re.findall(p,t)
[('7', '8', '34', '18')]
>>> for m in re.finditer(p,t):
	print m.groups()
	print m.groupdict()

	
('7', '8', '34', '18')
{}
>>> for m in re.finditer(p,t):
	print m.groups()
	print m.groupdict()
	print m.group()

	
('7', '8', '34', '18')
{}
Showing 17 to 38 of 34 (18 Pages)
>>> for m in re.finditer(p,t):
	print m.groups()
	print m.groupdict()
	print m.group()
	print m.groups(1)

	
('7', '8', '34', '18')
{}
Showing 17 to 38 of 34 (18 Pages)
('7', '8', '34', '18')
>>> for m in re.finditer(p,t):
	print m.groups()
	print m.groupdict()
	print m.group()
	print m.groups(2)

	
('7', '8', '34', '18')
{}
Showing 17 to 38 of 34 (18 Pages)
('7', '8', '34', '18')
>>> for m in re.finditer(p,t):
	print m.groups()
	print m.groupdict()
	print m.group(1)
	print m.groups(2)

	
('7', '8', '34', '18')
{}
7
('7', '8', '34', '18')
>>> for m in re.finditer(p,t):
	print m.groups()
	print m.groupdict()
	print m.group(2)
	print m.groups(2)

	
('7', '8', '34', '18')
{}
8
('7', '8', '34', '18')
>>> p = r"Showing (\d)+ to (\d)+ of ([0-9]+) \(([0-9]+) Pages\)"
>>> p = r"Showing (\d+) to (\d+) of ([0-9]+) \(([0-9]+) Pages\)"
>>> 
>>> 
>>> t = '     hello     '
>>> p=r' +hello +'
>>> re.findall(p,t)
['     hello     ']
>>> p=r' +(hello) +'
>>> re.findall(p,t)
['hello']
>>> p=r' *(hello) *'
>>> p=r' *(\w) *'
>>> p=r' *(\w+) *'
>>> re.findall(p,t)
['hello']
>>> t = ' lsadjfl '
>>> re.findall(p,t)
['lsadjfl']
>>> p=r'\s*(\w+)\s*'
>>> re.findall(p,t)
['lsadjfl']
>>> p=r'^\s*(\w+)\s*$'
>>> re.findall(p,t)
['lsadjfl']
>>> t = 'asldfj99809'
>>> re.findall(p,t)
['asldfj99809']
>>> t = 'asldfj99809AASD*'
>>> re.findall(p,t)
[]
>>> p=r'^\s*([\w\S]+)\s*$'
>>> t = 'asldfj99809AASD*'
>>> re.findall(p,t)
['asldfj99809AASD*']
>>> p=r'^\s*(\S+)\s*$'
>>> re.findall(p,t)
['asldfj99809AASD*']
>>> t ='10-5-2017'
>>> p = r'(\d{1,2})-(\d{1,2})-(\d{4})
SyntaxError: EOL while scanning string literal
>>> p = r'(\d{1,2})-(\d{1,2})-(\d{4})'
>>> re.findall(p,t)
[('10', '5', '2017')]
>>> p = r'(?P<mon>\d{1,2})-(?P<day>\d{1,2})-(?P<year>\d{4})'
>>> re.findall(p,t)
[('10', '5', '2017')]
>>> for m in re.finditer(p,t):
	print m.groups('mon')

	
('10', '5', '2017')
>>> for m in re.finditer(p,t):
	print m.group('mon')

	
10
>>> for m in re.finditer(p,t):
	print m.group('mon') , m.group('year'), m.group('day')

	
10 2017 5
>>> p = r'(?P<mon>\d{1,2})-(?P<day>\d{1,2})-(?P<year>\d{2}|\d{4})'
>>> for m in re.finditer(p,t):
	print m.group('mon') , m.group('year'), m.group('day')

	
10 20 5
>>> p = r'(?P<mon>\d{1,2})-(?P<day>\d{1,2})-(?P<year>\d{4}|\d{2})'
>>> 
>>> for m in re.finditer(p,t):
	print m.group('mon') , m.group('year'), m.group('day')

	
10 2017 5
>>> p = r'(?P<mon>\d{1,2})-(?P<day>\d{1,2})-(?P<year>\d{2}\d{2}?)'
>>> for m in re.finditer(p,t):
	print m.group('mon') , m.group('year'), m.group('day')

	
10 2017 5
>>> t
'10-5-2017'
>>> t = '10-5-17'
>>> 
>>> for m in re.finditer(p,t):
	print m.group('mon') , m.group('year'), m.group('day')

	
>>> p = r'(?P<mon>\d{1,2})-(?P<day>\d{1,2})-(?P<year>\d{2}(\d{2})?)'
>>> 
>>> for m in re.finditer(p,t):
	print m.group('mon') , m.group('year'), m.group('day')

	
10 17 5
>>> t
'10-5-17'
>>> t = '10-5-2017'
>>> for m in re.finditer(p,t):
	print m.group('mon') , m.group('year'), m.group('day')

	
10 2017 5
>>> re.findall(p,t)
[('10', '5', '2017', '17')]
>>> p = r'(?P<mon>\d{1,2})-(?P<day>\d{1,2})-(?P<yyyy>\d{2}(?P<yy>\d{2})?)'
>>> re.findall(p,t)
[('10', '5', '2017', '17')]
>>> for m in re.finditer(p,t):
	print m.group('mon') , m.group('yyyy'), m.group('day'), m.group('yy')

	
10 2017 5 17
>>> t = '10-5-17'
>>> 
>>> for m in re.finditer(p,t):
	print m.group('mon') , m.group('yyyy'), m.group('day'), m.group('yy')

	
10 17 5 None
>>> reo = re.compile(p)
>>> reo.findall(t)
[('10', '5', '17', '')]
>>> reo.findall(t)
[('10', '5', '17', '')]
>>> reo.findall(t)
[('10', '5', '17', '')]
>>> reo.findall(t)
[('10', '5', '17', '')]
>>> import time
>>> time.time()
1507793049.017
>>> time.localtime()
time.struct_time(tm_year=2017, tm_mon=10, tm_mday=12, tm_hour=12, tm_min=54, tm_sec=16, tm_wday=3, tm_yday=285, tm_isdst=0)
>>> time.ctime()
'Thu Oct 12 12:54:40 2017'
>>> m =time.localtime()
>>> type(m)
<type 'time.struct_time'>
>>> m.tm_hour
12
>>> m.tm_sec
31
>>> import subprocess
>>> subprocess.check_output('dir')
'1503142919.83.jpg  DLLs\t\t       first.py\t\tnoida.txt\n1503142921.91.jpg  Doc\t\t       geckodriver.log\tphotos\n1503142925.14.jpg  LICENSE.txt\t       greetaug17.py\tpython.exe\n1503142927.27.jpg  Lib\t\t       greetaug17.pyc\tpythonw.exe\n1503142929.86.jpg  NEWS.txt\t       greetoct10.py\tselenium\n1503142934.14.jpg  README.txt\t       greetoct10.pyc\ttcl\n1503142937.38.jpg  Scripts\t       include\t\ttest.xlsx\n1503142940.29.jpg  Tools\t       jul29.txt\ttoreadaug17.xlsx\n1503142946.33.jpg  aug4.py\t       libs\t\ttoreadaug19.xlsx\n1503142949.71.jpg  aug4.pyc\t       lntaug17.txt\nBank.py\t\t   createdbyapgm.xlsx  name.xml\nBank.pyc\t   debug.log\t       newfile.xlsx\n'
>>> subprocess.call('cd D:')

Traceback (most recent call last):
  File "<pyshell#299>", line 1, in <module>
    subprocess.call('cd D:')
  File "D:\sw\Python27\lib\subprocess.py", line 523, in call
    return Popen(*popenargs, **kwargs).wait()
  File "D:\sw\Python27\lib\subprocess.py", line 711, in __init__
    errread, errwrite)
  File "D:\sw\Python27\lib\subprocess.py", line 959, in _execute_child
    startupinfo)
WindowsError: [Error 2] The system cannot find the file specified
>>> 
>>> subprocess.check_output('dir')
'1503142919.83.jpg  DLLs\t\t       first.py\t\tnoida.txt\n1503142921.91.jpg  Doc\t\t       geckodriver.log\tphotos\n1503142925.14.jpg  LICENSE.txt\t       greetaug17.py\tpython.exe\n1503142927.27.jpg  Lib\t\t       greetaug17.pyc\tpythonw.exe\n1503142929.86.jpg  NEWS.txt\t       greetoct10.py\tselenium\n1503142934.14.jpg  README.txt\t       greetoct10.pyc\ttcl\n1503142937.38.jpg  Scripts\t       include\t\ttest.xlsx\n1503142940.29.jpg  Tools\t       jul29.txt\ttoreadaug17.xlsx\n1503142946.33.jpg  aug4.py\t       libs\t\ttoreadaug19.xlsx\n1503142949.71.jpg  aug4.pyc\t       lntaug17.txt\nBank.py\t\t   createdbyapgm.xlsx  name.xml\nBank.pyc\t   debug.log\t       newfile.xlsx\n'
>>> s = 'My first file created by a python program'
>>> s
'My first file created by a python program'
>>> fh = open('oracle1012.txt','wt')
>>> fh.write(s)
>>> fh.close()
>>> fh = open('oracle1012.txt', 'rt')
>>> s = fh.read()
>>> s
'Line 1\nLine 2\nLine 3\nLine 4'
>>> fh.close()
>>> fh = open('oracle1012.txt', 'rt')
>>> fh.readlines()
['Line 1\n', 'Line 2\n', 'Line 3\n', 'Line 4']
>>> fh.close()
>>> fh = open('oracle1012.txt', 'rt')
>>> for line in fh:
	print line

	
Line 1

Line 2

Line 3

Line 4
>>> for line in fh:
	print line

	
>>> fh.seek(0)
>>> for line in fh:
	print line.strip()

	
Line 1
Line 2
Line 3
Line 4
>>> fh.seek(0)
>>> s = fh.read(10)
>>> s
'Line 1\nLin'
>>> fh.read(3)
'e 2'
>>> fh.tell()
14L
>>> fh.seek.__doc__
'seek(offset[, whence]) -> None.  Move to new file position.\n\nArgument offset is a byte count.  Optional argument whence defaults to\n0 (offset from start of file, offset should be >= 0); other values are 1\n(move relative to current position, positive or negative), and 2 (move\nrelative to end of file, usually negative, although many platforms allow\nseeking beyond the end of a file).  If the file is opened in text mode,\nonly offsets returned by tell() are legal.  Use of other offsets causes\nundefined behavior.\nNote that not all file objects are seekable.'
>>> fh.tell()
14L
>>> fh.seek(3,1)
>>> fh.tell()
17L
>>> fh.read(3)
'ine'
>>> fh.tell()
20L
>>> fh.seek(3,0)
>>> fh.read(1)
'e'
>>> fh.seek(0,0)
>>> fh.tell()
0L
>>> fh.close()
>>> import requests
>>> r = requests.get("https://news.marvel.com/wp-content/uploads/sites/28/2017/02/HULK_post_master.jpg")
>>> r.status_code
200
>>> r.content[:100]
'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00II*\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xec\x00\x11Ducky\x00\x01\x00\x04\x00\x00\x00<\x00\x00\xff\xee\x00\x0eAdobe\x00d\xc0\x00\x00\x00\x01\xff\xdb\x00\x84\x00\x06\x04\x04\x04\x05\x04\x06\x05\x05\x06\t\x06\x05\x06\t\x0b\x08\x06\x06\x08\x0b\x0c\n\n\x0b\n\n\x0c\x10\x0c\x0c\x0c'
>>> fh.open('hulk.jpg', 'wb')

Traceback (most recent call last):
  File "<pyshell#344>", line 1, in <module>
    fh.open('hulk.jpg', 'wb')
AttributeError: 'file' object has no attribute 'open'
>>> fh = open('hulk.jpg', 'wb')
>>> fh.write(r.content)
>>> fh.close()
>>> r = requests.get('http://omdbapi.com/?s=hulk&apikey=BanMePlz')
>>> r.text[:100]
u'{"Search":[{"Title":"The Incredible Hulk","Year":"2008","imdbID":"tt0800080","Type":"movie","Poster"'
>>> import json
>>> data = json.loads(r.text)
>>> type(data)
<type 'dict'>
>>> data.keys()
[u'Search', u'totalResults', u'Response']
>>> len(data['Search'])
10
>>> data['Search'][0]
{u'imdbID': u'tt0800080', u'Year': u'2008', u'Type': u'movie', u'Poster': u'https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyNzk3MjA1OF5BMl5BanBnXkFtZTcwMTE1Njg2MQ@@._V1_SX300.jpg', u'Title': u'The Incredible Hulk'}
>>> data['Search'][0]['Title']
u'The Incredible Hulk'
>>> for movie in data['Search']:
	print "title" , movie['Title']

	
title The Incredible Hulk
title Hulk
title Hulk Vs.
title Planet Hulk
title The Incredible Hulk
title The Incredible Hulk Returns
title The Incredible Hulk
title Hulk and the Agents of S.M.A.S.H.
title The Trial of the Incredible Hulk
title The Death of the Incredible Hulk
>>> for movie in data['Search']:
	print "Poster" , movie['Poster']

	
Poster https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyNzk3MjA1OF5BMl5BanBnXkFtZTcwMTE1Njg2MQ@@._V1_SX300.jpg
Poster https://images-na.ssl-images-amazon.com/images/M/MV5BNjcxMzZhZTEtMmEwYi00NDJmLWE5ZmUtOWJiMzRmMzEzMTY3L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg
Poster https://images-na.ssl-images-amazon.com/images/M/MV5BMTc1NzMzMzU4Nl5BMl5BanBnXkFtZTcwNTQ3NDYwNQ@@._V1_SX300.jpg
Poster https://images-na.ssl-images-amazon.com/images/M/MV5BYmFlNTNhNjktNDQ4NC00ZmVhLTg2NmYtOWExMmI0MzQ1ODFmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg
Poster https://images-na.ssl-images-amazon.com/images/M/MV5BMTI3MzMwODM4N15BMl5BanBnXkFtZTcwMDM2Njc0MQ@@._V1_SX300.jpg
Poster https://images-na.ssl-images-amazon.com/images/M/MV5BMTI5NjQ0NzczN15BMl5BanBnXkFtZTcwNzM1ODMyMQ@@._V1_SX300.jpg
Poster https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4MjYzMDU0MV5BMl5BanBnXkFtZTcwMzk3MjkxMQ@@._V1_SX300.jpg
Poster https://images-na.ssl-images-amazon.com/images/M/MV5BMTg1MzIxMzM4Nl5BMl5BanBnXkFtZTcwMTg3Mzc5OQ@@._V1_SX300.jpg
Poster https://images-na.ssl-images-amazon.com/images/M/MV5BMjA1NDg2MDI0Nl5BMl5BanBnXkFtZTcwMDQ1MjMyMQ@@._V1_SX300.jpg
Poster https://images-na.ssl-images-amazon.com/images/M/MV5BMTU5OTA1OTkwNV5BMl5BanBnXkFtZTcwODM3ODkyMQ@@._V1_SX300.jpg
>>> for movie in data['Search']:
	r = requests.get(movie['Poster'])
	open(movie['imdbID']+".jpg", 'wb').write(r.content)

	
>>> import csv
>>> reader = csv.DictReader(open("oracle1012.txt",delimiter=','))

Traceback (most recent call last):
  File "<pyshell#367>", line 1, in <module>
    reader = csv.DictReader(open("oracle1012.txt",delimiter=','))
TypeError: 'delimiter' is an invalid keyword argument for this function
>>> reader = csv.DictReader(open("oracle1012.txt",'r'),delimiter=',')
>>> for row in reader:
	print row['login', 'password']

	

Traceback (most recent call last):
  File "<pyshell#371>", line 2, in <module>
    print row['login', 'password']
KeyError: ('login', 'password')
>>> for row in reader:
	print row['login'], row['password']

	
sp sp
hello what
>>> reader = csv.DictReader(open("oracle1012.txt",'r'),delimiter=',')
>>> for row in reader:
	print row['login'], row['password']

	
admin admin
sp sp
hello what
>>> 
