"""
The syntax of the sort() method is:
********************************************
list.sort(key=..., reverse=...)

Alternatively, you can also use Python's built-in sorted() function for the same purpose.
*****************************************************************************************
sorted(list, key=..., reverse=...)

Note: The simplest difference between sort() and sorted() is: sort() changes the list directly and doesn't return any value, while sorted() doesn't change the list and returns the sorted list.
"""

#Example 1
vowels=['i','e','a','u','o']
ll=vowels[:]
revsort=vowels[:]
vowels.sort()
print('Sorted list',vowels)
revsort.sort(reverse=True)
print(revsort)
#sort with sorted function
print('Sorted',sorted(ll))
print('sorted with rev order',sorted(ll,reverse=True))
print('Unsorted list remain unchanged',ll)

#Example 3: Sort with custom Key or function

def takeSecond(elem):
    return elem[1]  #take second

random=[(2,2),(3,4),(4,1),(1,3)]
ll=random[:]

random.sort(key=takeSecond)
print('Sorted list' ,random)
print("using sorted",sorted(ll,key=takeSecond))

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]
eex5=employees[:]
#Example 4: custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')

#Example 5: Custom Key Using lambda
employees.sort(key=lambda x:x.get('Name'))
print(*employees,sep=' \n',end='\n\n')
employees.sort(key=lambda z:z.get('age'))
print(*employees,sep='\n',end='\n\n')
employees.sort(key=lambda y:y.get('salary'))
print(*employees,sep='\n',end='\n\n')
