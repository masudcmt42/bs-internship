from collections import deque




#make a list[] 

bikes=["apachi","Yahamma",'Dayang','Hero','Honda','R1v3']

#print first item
print('first item biles[0]= '+bikes[0])


#get last item
print('last item bikes[-1]= '+bikes[-1])

#loop through list
for x in bikes:
    print(x)

#adding item to end of list   N.B Use list.append(x) method
bikes.append('suzuki')
bikes[len(bikes):]=['pluser']

#Extebd the list list.extend(iterable)
bikes.extend(["Runner"])

#insert list list.insert(i,X)
bikes.insert(3,'R1v3')
#Remove first item whose value is equal to x list.remove(X)
bikes.remove('R1v3')
#Remove i index item and return value using list.pop(X)
val=bikes.pop(5);  #if a.pop() it remove and return last value.

print(val)
print(bikes)
#Return the number of item
print(bikes.count('R1v3'))
#sort list
bikes.sort() # Learn more in sorting list see sortOfListPy file
print(bikes)


'''
#making Numerical lists
squre=[]  #new list
for x in range(1,11):
        squre.append(x**2)  # **2 is squre operator
print(squre)

#list Comprehensions
squres=[x**2 for x in range(1,10)] #New list equv to list(map(lambda x: x**2,range(10)))
print(squres)

#Slicing a List
newBike=bikes[2:5]
print('Old bike list: ',bikes)
print(newBike)

#Delete any Item from list by index
del newBike[1]
print(newBike)


print(squres)
#taking first n element of the list
print('first 5 element',squres[:5])
#taking last n element
print('last 5 element',squres[-5:])

#taling all but except last n element
print('all except last 2',squres[:-2])

#Revarce List 
print(squre[::-1]) #or user squre.reverse() 
'''

#using list as stack
stack=[3,2,4,5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)
#using List as Queues
queue=deque(['masud','nafisa','rana','Anjum'])
queue.append('Nowsin')
queue.append('tuba')
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)
