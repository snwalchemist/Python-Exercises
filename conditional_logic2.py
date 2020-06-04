# TRUTHY & FALSEY

#

# this would say this person is old enough to drive since python converts is_older and has_license to boolean
is_older = 'hello'
has_license = 5

print(bool('hello')) # returns True
print(bool(5)) # Returns

# emptpy values or None values return FALSE
print(bool('')) # returns FASLE
print(bool(0)) # returns FALSE

if is_older and has_license:
  print('you are old enough to drive!') #does not run
else:
  print('Doesn\'t look like you should be diriving')

print('okok')

password = '123'
username = 'johnny'

if password and username:
  print('you\'ve been logged in')
else:
  print('issue logging you in')

# TERNARY OPERATOR
# this is a short cut, can only be used in certain circumstances but keeps code cleaner
# evaluates conditional expressions

# condition_if_true if condition else condition_if_else

is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message) # returns message allowed since is_friend is equal to true

# Short Circuiting

is_Friend1 = True
is_User1 = True

if is_Friend1 and is_User1:
  print('best friends forever')

# this is short circuiting, interpreter only needs to evaluate one of the conditions to return an output
if is_Friend1 or is_User1:
  print('best friends forever') # returns

# Logical Operators

# and, or, > , < , = , >= , <= , != , == (= can't be used b/c we use it as an expression for assigning variables)

print('a' > 'b')
print('a' > 'A')

print(1 < 2 < 3 < 4) # an expression that evaluates to True

# Short circuit example, once interpretor sees 2 is not greater thatn 3 it evaluates to false w/o evaluating the rest of the expression

print(1 < 2 > 3 < 4) # an expression that evaluates to False

print(0 != 1) # returns True since it is true that 0 is not equal to 1

# Key Word: Not

print(not(True)) # Returns False
print(not(False)) # Returns opposite or True

# Exercise Time

is_magician = False
is_expert = True

# check if magician and expert print "you are a master magician"

# check if magician but not expert print "at lease your getting there"

# if you're not a magician print "You need magic powers"

if is_magician and is_expert:
  print('You are a master magician')
elif is_magician and not is_expert:
  print('At least you are getting there')
else:
  print('you need magic powers')

print(True == 1) #True
print('' == 1) #False
print([] == 1) #False
print(10 == 10.0) #True
print([] == []) #True
print('1' == 1) #False confusing but this is bad code

# Key Word is

# checks the location in memory not the of the expression
print(True is 1) # False different data structures
print('' is 1) # False
print([] is 1) #False
print(10 is 10.0) # False
print([] is []) # False
print('1' is 1) #False

print(True is True) # False different data structures
print('1' is '1') # False
print([] is []) #False
print(10 is 10.0) # False
print(10 is 10) #True b/c it's the same data structure
print([1,2,3] is [1,2,3]) # False b/c these are two seperate lists or live in different parts of memory
