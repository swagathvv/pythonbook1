Python 3.4.0 (default, Apr 11 2014, 13:05:18) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def first(word):
	return word[0]

>>> def last(word):
	return word[-1]

>>> def middle(word):
	return word[1:-1]

>>> first(swag)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    first(swag)
NameError: name 'swag' is not defined
>>> first('swa')
's'
>>> last('swa')
'a'
>>> middle('sw')
''
>>> middle('')
''
>>> middle('e')
''
>>> 
# 2
>>> def is_palindrome(word):
	if len(word)<=1:
		return ('true')
	if first(word) != last(word):
		return ('false')
	return is_palindrome(middle(word))

>>> is_palindrome('sas')
'true'
>>> is_palindrome('swaf')
'false'
>>> 
