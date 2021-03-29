year= 2020
event='Us election'
print(f'Result of the {year} {event}')

#Using str.format()
yes_votes=42_572_654
no_votes=3_123_495
print('yes_votes',type(yes_votes),yes_votes)
percentage=yes_votes/(yes_votes+no_votes)
print('{:-9} YES votes {:2.2%}'.format(yes_votes,percentage))
a,b=10,20
print('a = {1} b = {0}'.format(b,a))
print('{:7.7f}'.format(20.31))

#Some Example
s='Hello, world'
print(str(s))
print(repr(s))
print(str(1/7)) 
x=10+3.25
y=200*200
s='the value of x is '+repr(x)+', and y is ' + repr(y)+'...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# The argument to repr() may be any Python object:
print(repr((x,y,('span','egg'))))
