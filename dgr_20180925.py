Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> input("Cienījamais lietotāj, lūdzu ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 10
10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigais = input("Cienījamais lietotāj, lūdzu ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais
10
>>> mans_mainigais = input("Cienījamais lietotāj, lūdzu ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 20, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainigais)
<type 'int'>
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test_1_20180925.py', 'mans_mainigais': 5, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 4
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test_1_20180925.py', 'mans_mainigais': 4, '__package__': None, 'x': 16, '__name__': '__main__', '__doc__': None}
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 89
mans_mainigais = 
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 156
mans_mainigais = 156
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 12
mans_mainigais = 12
vai Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 12
mans_mainigais = 12
Respektīvi, Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 8.6549
mans_mainigais =      8.655
Respektīvi, Tu esi ievadījis skaitli:     8.6549
vēl atmiņā tagad ir arī mainīgais x =      74.9072940
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 15
mans_mainigais =                                                                                                 15.000000
Respektīvi, Tu esi ievadījis skaitli:    15.0000
vēl atmiņā tagad ir arī mainīgais x =     225.0000000
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 4
mans_mainigais =                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         4.000000
Respektīvi, Tu esi ievadījis skaitli:     4.0000
vēl atmiņā tagad ir arī mainīgais x =      16.0000000
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 15
mans_mainigais =     15.000
Respektīvi, Tu esi ievadījis skaitli:    15.0000
vēl atmiņā tagad ir arī mainīgais x =     225.0000000
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi simbolu rindu: 15

Traceback (most recent call last):
  File "/home/user/test_1_20180925.py", line 2, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi simbolu rindu: 15

Traceback (most recent call last):
  File "/home/user/test_1_20180925.py", line 2, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> aaa

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    aaa
NameError: name 'aaa' is not defined
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi simbolu rindu: ssss

Traceback (most recent call last):
  File "/home/user/test_1_20180925.py", line 2, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi simbolu rindu: aa
mans_mainigais = aa
Respektīvi, Tu esi ievadījis rindu: aa
>>> 
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> input("Cienījamais lietotāj, lūdzu ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 10
10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigais = input("Cienījamais lietotāj, lūdzu ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais
10
>>> mans_mainigais = input("Cienījamais lietotāj, lūdzu ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 20, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainigais)
<type 'int'>
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test_1_20180925.py', 'mans_mainigais': 5, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 4
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test_1_20180925.py', 'mans_mainigais': 4, '__package__': None, 'x': 16, '__name__': '__main__', '__doc__': None}
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 89
mans_mainigais = 
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 156
mans_mainigais = 156
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 12
mans_mainigais = 12
vai Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 12
mans_mainigais = 12
Respektīvi, Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 8.6549
mans_mainigais =      8.655
Respektīvi, Tu esi ievadījis skaitli:     8.6549
vēl atmiņā tagad ir arī mainīgais x =      74.9072940
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 15
mans_mainigais =                                                                                                 15.000000
Respektīvi, Tu esi ievadījis skaitli:    15.0000
vēl atmiņā tagad ir arī mainīgais x =     225.0000000
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 4
mans_mainigais =                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         4.000000
Respektīvi, Tu esi ievadījis skaitli:     4.0000
vēl atmiņā tagad ir arī mainīgais x =      16.0000000
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi vienu skaitli: 15
mans_mainigais =     15.000
Respektīvi, Tu esi ievadījis skaitli:    15.0000
vēl atmiņā tagad ir arī mainīgais x =     225.0000000
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi simbolu rindu: 15

Traceback (most recent call last):
  File "/home/user/test_1_20180925.py", line 2, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi simbolu rindu: 15

Traceback (most recent call last):
  File "/home/user/test_1_20180925.py", line 2, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> aaa

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    aaa
NameError: name 'aaa' is not defined
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi simbolu rindu: ssss

Traceback (most recent call last):
  File "/home/user/test_1_20180925.py", line 2, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=================== RESTART: /home/user/test_1_20180925.py ===================
Cienījamais lietotāj, lūdzu ievadi simbolu rindu: aa
mans_mainigais = aa
Respektīvi, Tu esi ievadījis rindu: aa
>>> 
gegegeg
