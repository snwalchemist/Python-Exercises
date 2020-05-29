long_string = '''
WOW
O O
---
|||
'''
print(long_string)

first_name = 'Seth'
last_name = 'Hahn'
# string concatenation (only works with strings, can't mix)
full_name = first_name + ' ' + last_name
print(full_name)

#TYPE CONVERSION
#str is a built in function

#coverting integer to string and checking type
print(type(str(100)))
#coverting integer to string and string back to integer and output checking type
print(type(int(str(100))))

#ESCAPE SEQUENCE
#back slash tells python whatever comes after is a string
#\n tells python to start on a new license
#\t tells python to tab
weather1 = "it\'s \"kind of\" sunny"
weather2 = "it\\s \"kind of\" sunny"
weather3 = "\t it\'s \"kind of\" sunny \n hope you have a good day!"

print(weather1)
print(weather2)
print(weather3)

#FORMATTED STRINGS
name = 'johnny'
age = 55
print('hi ' + name + '. You are ' + str(age) + ' years old' )
#new way in python 2 called an f-string
print(f'hi {name}. You are {age} years old')
#old way
print('hi {}. You are {} years old'.format(name, age))
#could reaarrange variables
print('hi {1}. You are {0} years old'.format(name, age))
#could assign new vriables
print('hi {new_name}. You are {age} years old'.format(new_name = 'Sally', age=100))

#STRING INDEXES
#pythong indexes each character in a string including spaces
selfish = 'me me me'
print(selfish[3])
#can start and stop at different indexes
selfish2 = '01234567'
print(selfish2[0:8])
#***[start:stop:stepover]***
print(selfish2[0:8:2])
print(selfish2[1:])
print(selfish2[:5])
print(selfish2[::1])
print(selfish2[-1:])
print(selfish2[-2:])
#**useful notation to reverse a string
print(selfish2[::-1])

#IMMUTABILITY: Strings cannot be changed
#selfish3[8] = '01234567' (can't change the string to 8 here)
#you can reassign the vairable like this to change it
selfish2 = selfish2 + '8'
print(selfish2)

#LEN (LENGTH)
#len doesn't start from zero
greet = 'helllooooo'
print(len('hellloooo'))
print(greet[0:len(greet)])

#STRING METHODS
#methods are owned by built-in functions
quote = 'to be or not to be'

print(quote.upper())
print(quote.capitalize())
#.find outputs the index of what's being found
print(quote.find('be'))
print(quote.replace('be', 'me'))
#the quote looks like it's been changed but it's immutable so "quote" stays the same
print(quote)

quote2 = quote.replace('be', 'me')
print(quote2)

#BOOLEANS

name = 'Seth'
is_cool = False
is_cool = True

print(bool(1)) #this is True
print(bool(0)) #this is False
print(bool('True')) #this is True
print(bool('False')) #this is also True

#TYPE CONVERSION EXERCISE
birth_year = input('what year were you born? -->')
current_year = input('enter the current year -->')
age = int(current_year) - int(birth_year)

print(f'Your age is: {age}')

#PASSWORD CHECKER EXERCISE
username = input('username -->')
password = input('password -->')
password_length = len(password)
secret_password = '*' * password_length

print(f'{username}, your password {secret_password} is {password_length} letters long')
