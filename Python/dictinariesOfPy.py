'''
The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.
'''
tel={'jack':4098,'sape':2452}
tel['guido']=4127
print(tel)
print(tel['jack'])

#delete item
del tel['sape']
#insert item
tel['ivr']=4127
print(tel)
#print all key
print(list(tel))
#Sort item
print(sorted(tel))
#conditions on dic
print('ivr' in tel)
print('dd' in tel)
#Constructor builds dictinaries dict()
dd=dict([('a',23),('b',24),('c',25),('d',32)])
print(dd)
#when keys are simple string
print(dict(shap=2342,guido=5643,jack=3241))
# dict comprehension 
print({x:x**2 for x in (2,4,6)})

