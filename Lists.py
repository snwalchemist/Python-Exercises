#LISTS ARE A FORM OF ARRAYS IN OTHER LANGUAGES
#IT IS A DATA STRUCTURE
li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2,5.3,'a', True]

#accessing items in the list
amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0])
print(amazon_cart[1])

#LIST SLICING
string = 'helllooo'
print(string)
print(string[0:2:1])

amazon_cart = [
'notebooks',
'sunglasses',
'toys',
'grapes'
]

print(amazon_cart[0::2])

#Lists are mutable
amazon_cart[0] = 'laptop'
print(amazon_cart) #notebooks in the original amazon_cart variable is replaced with 'laptop'
print(amazon_cart[0:3]) #this is list slicing and creates a new list or copy of the amazon cart
print(amazon_cart)

new_cart = amazon_cart #This format does not copy the list, it modifies it
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

amazon_cart[0] = 'laptop'
new_cart2 = amazon_cart[:] #This format creates an actual copy of the original "amazon_cart"
new_cart2[0] = 'gum'
print(new_cart2)
print(amazon_cart)

#MATRIX
#used to descript a multidimentional list. it's an array with another array inside

matrix = [
  [1,2,3],#this would be indexed as 0
  [4,5,6],
  [7,8,9],
]

print(matrix[0][1]) #first bracket tells python which array to use, second tells which index in the list to output

#LIST METHODS
#Owned by something like lists or strings

basket = [1,2,3,4,5]

#adding
new_list = basket.append(100)
print(new_list) #prints none because it doesn't produce an output it changes the list "in place"
print(basket)

basket2 = [1,2,3,4,5]
basket2.append(100)
new_list = basket2 #after appending then we can assign a variable, then we can print the variable
print(new_list)

#insert method
#modifies the list in place does not create a copy of the list
basket3 = [1,2,3,4,5]
basket3.insert(3,100)
new_list = basket3
print(new_list)

#extend method
#is iterable
basket4 = [1,2,3,4,5]
basket4.extend([100, 101])
new_list = basket4
print(new_list)

#removing method
#.pop removes at the end (uses indexes)
basket5 = [1,2,3,4,5]
basket5.pop() #removes the index given or the last item in the list
new_list = basket5
print(new_list)
new_list2 = basket5.pop(3) #when given a value .pop returns the value at the given index
print(new_list2)

#.remove method (uses values)
basket6 = [1,2,3,4,5]
basket6.remove(1) #removes whatever value is given
new_list = basket6
print(new_list)

#clear method
basket7 = [1,2,3,4,5]
basket7.clear() #removes all values in the list
new_list = basket7
print(new_list)
