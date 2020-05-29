#LISTS CONTINUED

#index method uses a start and a stop
basket = ['a','d','c','d','e']
print(basket.index('d', 0, 4)) #looks for the string 'd' b/w the index of 0 and 4 in the list. this throws an error if the lookup value is not in the indexed range given

#KEYWORDS

#in
print('c' in basket) #in keword looks to see if lookup value is in the list this is True
print('x' in basket) #x isn't in the list so in keword returns false
print('i' in 'hi my name is seth')

#.count method
print(basket.count('d'))

#.sort method & sorted function
basket2 = [3,2,3,7,5,6,9]
basket2.sort()
print(basket) #sorts list alphabetically or numerically
print(sorted(basket2)) #sorted is a function and sorts a copy of a list this
#so the above function sorted does the same thing as the below
new_basket2 = basket2[:] #can use .copy() as well instead of [:]
new_basket2.sort() #sorts the copy of new_basket2 in place
print(new_basket2)

#.reverse method
basket2.reverse() #basket2 has already been sorted. reverse is ordering the list indexes in reverse
print(basket2)

#LIST PATTERS AND USEFUL TRICKS
basket3 = ['a','d','c','d','e','m','s']
#slicing method to reverse order
basket3.sort() #sorts the list
basket3.reverse() #the list is now in reverse order
print(basket3[::-1]) #copies basket and sorts the list again **will see this notation alot
print(basket3) #returns the modified list

#range takes a start and stop
print(range(1,100))
print(list(range(1,100))) #generates a list of numbers fro index starting at 0 to 100
print(list(range(100))) #does the same thing

#.join
sentence = '!'
new_sentence = sentence.join(['--> ','hi','my','name','is'])
print(new_sentence)
#short-hand way of doing this
new_sentence2 = ' '.join(['--> ','hi','my','name','is'])
print(new_sentence2)

#List unpacking
var1, var2, var3 = [1,2,3] #each variable is assigned to each value in the list
print(var1)
print(var2)
print(var3)

var4, var5, var6, *other, var7 = [1,2,3,4,5,6,7,8,9]
print(var4)
print(var5)
print(var6)
print(other) #star unpacks all other list items after last variable or to index before next variable assigned after other. this also returns a list
print(var7) 
