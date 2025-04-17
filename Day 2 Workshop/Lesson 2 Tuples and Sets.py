my_tuple = ('apple', 'banana', 'cherry')
my_list = list(my_tuple)

my_list.append('orange')

my_tuple = tuple(my_list)

print(my_tuple)

#Sets
#Sets are unordered and unchangeable collections of data types
#Duplicates are not allowed in sets
set_fruits = {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'orange'}
print(set_fruits)