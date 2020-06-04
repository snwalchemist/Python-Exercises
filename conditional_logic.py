#If Else logic

#If Else logic

is_old = True
is_licensed = True

if is_old:
  print('you are old enough to drive!') # runs if is_old is True
print('checkcheck') # prints no matter what

is_old = False

if is_old:
  print('you are old enough to drive!') # won't print since is_old is set to False
print('checkcheck')

if is_old:
  print('you are old enough to drive!') #does not run
else:
  print('checkcheck') #when is_old is false this line runs

is_older = False
has_license = False

if is_older: # this is an expression
  print('you are old enough to drive!') #does not run
elif has_license:
  print('you can drive now') #does not run
else:
  print('check form of id') #when is_old is false this line runs

is_older = True
has_license = False

#Key Word AND

if is_older and has_license: # expression that requires both booleans to be TRUE
  print('you are old enough to drive!') #does not run
else:
  print('Doesn\'t look like you should be diriving')

print('okok')
