#DICTIONARY
#python terminology is "dict"
#its a data typ and a data structure the helps organize data
#has a key and a value
# an un-ordered key pair so it's not indexed

dictionary = {
  'a': 1,
  'b': 2,
  'x': 3
}

print(dictionary['b']) #returns value assigned in the dict which is 2
print(dictionary) # because dict's are un-ordered, this print statement may not return the dictionary as it's currently listed... a, b, x

#Can hold different data types:
dictionary2 = {
  'a': [1,2,3],
  'b': 'hello',
  'x': True
}

#accessing the first dict key and the 2nd in the list 2
print(dictionary2['a'][1])

my_list = [
  {
  'a': 1,
  'b': 2,
  'x': 3
  },
  {
  'a': [4,5,6],
  'b': 'hello',
  'x': True
  }
]

print(my_list[1]['a'][2])

#UNDERSTANDING DATA STRUCTURES
# lists might be used to record a line of customers at a Store.
# a dict might be used for a user profile in a game

# a dictionary key needs to have a special property it has to be immutable so a list cannot be a key in a dictionary
dictionary3 = {
  123: [1,2,3],
  True: 'hello',
  'x': True
}

print(dictionary3[123]) # most of the time keys in a dict will be a descriptive string
print(dictionary3[True])
print(dictionary3['x'])

#DICTIONARY METHODS
#dictionary keys need to be unique

user = {
  'basket': [1,2,3],
  'greet': 'hello'
}

user2 = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 20
}

#.GET METHOD
# print(user.get['age']) this would throw a keyerror b/c 'age' does not exist in the dict

print(user.get('age')) #returns 'None' instead of an error
print(user.get('age', 55)) # this adds 55 as age for user since age doesn't exist in this dict
print(user2.get('age', 55)) # cince age exists, the dict age is used instad of default value 55

#DICT (not as common)
user3 = dict(name = 'JohnJohn') # name cant be an expression (wraped in quotes like a string) so 'name' won't work
print(user3)

#IN
print('basket' in user2) #like lists, we can use 'in' to find keys in a dict- returns boolean value T or F

# METHOD: Keys
print('greet' in user2.keys()) # returns boolean value

#METHODS: items
print(user2.items()) #returns keys and key values in the dict. this is called a tupple

#METHOD: clear
print(user2.clear()) # doesnt return anything it clears the dict in place

#METHOD: copy
user4 = user2.copy()
print(user2.clear())
print(user4) # user2 was copied and returned as user4

#METHOD: pop

user5 = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 20
}

print(user5.pop('age'))
print(user5)

#METHOD popitem
print(user5.popitem()) #randomly pops something but may just remove the last value pair
print(user5)

#METHOD update
print(user5.update({'ages': 55})) #updates a key value or provides a default
print(user5)
