#SETS
# un-ordered sets of unique objects

my_set = {1,2,3,4,5,5,5}
my_set.add(100)
my_set.add(2) # only returns one 2 b/c it has to be unique
print(my_set) #this prints only one 5, everyting has to be unique

my_list = [1,2,3,4,5,5,5]
print(set(my_list)) #converting a list into a set to return unique values
#set does not work by indexing so print(my_set[0]) throws an error
# we have to grab by the item in the set:
print(1 in my_set)
print(len(my_set))
print(list(my_set))

new_set = my_set.copy()

# METHODS

my_set1 = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set1.difference(your_set)) # only shows difference b/w the two sets

#Discard
print(my_set1.discard(5)) # modifies the set does not return yet..
print(my_set1) #now it returns the new set

#Difference_Update

print(my_set1.difference_update(your_set)) #again doesn't return values, just modifies the set
print(my_set1) # now the set has been updated to only include 1,2,3

#Intersection

my_set2 = {1,2,3,4,5}
your_set2 = {4,5,6,7,8,9,10}
print(my_set2.intersection(your_set2)) # returns 4,5 since that's the common values b/w both sets
#short hand way to do intersection
print(my_set2 & your_set2)

#Isdisnoint()
print(my_set2.isdisjoint(your_set2)) # returns False since the two sets do have values in common

my_set3 = {1,2,3,4,5}
your_set3 = {6,7,8,9,10}
print(my_set3.isdisjoint(your_set3)) #returns True since both sets do not have valuses in common or they are disjointed

#issubclass
my_set3 = {1,2,3,4,5}
your_set3 = {6,7,8,9,10}

#Union
print(my_set3.union(your_set3)) #united the sets together
#short hand way
print(my_set3 | your_set3)

#issubset

my_set4 = {4,5}
your_set4 = (my_set3 | your_set3)
print(f'--> Created SuperSet with a union on previous exercise: {your_set4}')
print(my_set4.issubset(your_set4)) #returns True
print(your_set4.issubset(my_set4)) #returns Fals b/c your_set4 is the superset, it contains values in my_set4

#Issuperset
print(your_set4.issuperset(my_set4))
