#looping Techniques for Dict
knights={'nafisa':'the puure','Masud':'the brave'}
for k,v in knights.items():
    print(k,v)

#loop in list for item and index
ll=['tic','tac','toe']
for i, v in enumerate(ll):  #Return an enumerate object.
    print(i,v)

#loop OVER TWO OR MORE LIST
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers): #Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
    print('What is your{0}? It is {1}.'.format(q,a))
#loop over a sequence in reverse
for i in reversed(range(1,10,2)):
    print(i)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
#loop over in sorted order
for i in sorted(basket):
    print(i)
#using set on a seq eliminate duplicate elements
for i in sorted(set(basket)):
    print(i)

