import math
print(f'the value of pi is approx {math.pi:.5f}.')
print('the value of pi is approx {:.5f}.'.format(math.pi))
"""
Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up."""
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name,phone in table.items():
    print(f'{name:10}==>{phone:10d}')
"""Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():"""
animals = 'eels'
print(f'My hovercarft is full of {animals}.')
print(f'My hovercarft is full of {animals!r}.')

