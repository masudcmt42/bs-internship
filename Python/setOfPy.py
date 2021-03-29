'''
Python also includes a data type for sets. 
A set is an unordered collection with no duplicate elements. 
Basic uses include membership testing and eliminating duplicate entries. 
Set objects also support mathematical operations like union,
intersection, difference, and symmetric difference.
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)    # show that duplicates have been removed
print('apple' in basket)
print('manggo' in basket)
# Demonstrate set operations on unique letters from two words
a=set('abracadabra')
b=set('alacazam')
print(a) #unique latter in a
print('a-b: ',a-b) #latter in a but not b
print('union: ',a|b)
print('intersection ',a&b)
print('latter a or b but not both ',a^b)
#similariy to list comprehension
