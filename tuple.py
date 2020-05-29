#TUPLES
# like lists but they are immutable so basically immutable lists

my_tuple = (1,2,3,4,5)
# my_tuple[1] = 'z'  #this would retunr an error b/c you cant change it
# makes code more predictable but they are less flexible
# tuples are usually faster than lists

user = {
  (1,2,3): [1,2,3],
  'greet': 'Helo!',
  'age': 20
}

# returns a tuple of the dict
print(user.items())
# accessing the tuple key in the dict and returning the value which is a list
print(user[(1,2,3)])

my_tuple1 = (1,2,3,4,5)
new_tuple = my_tuple1[1:4]

print(new_tuple)

#accessing pieces of the tuple or values indexed in the tuple
x = my_tuple1[0]
y = my_tuple1[1]
print(x,y)
# a shorter way to do this is similar to what we did with lists:

x,y,z, *other = (1,2,3,4,5)

print(f'{x}: this is the x value or index of 0 in the tuple')
print(f'{y}: this is the x value or index of 1 in the tuple')
print(f'{z}: this is the x value or index of 1 in the tuple')
print(other)
print(f'{other}: other produces a list of the remaining values int the tuple')

#METHOD count
# counts number of times x value is found in the tuple
my_tuple2 = (1,2,3,4,5,5)
print(my_tuple2.count(5))

#METHOD index
# returns index of value given inthe tuple
print(my_tuple2.index(3))

#METHOD len
print(len(my_tuple2))
