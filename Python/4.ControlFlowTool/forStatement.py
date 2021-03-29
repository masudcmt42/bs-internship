#Measure some String
cords=['cat','windows','Masud Rana']
for w in cords:
    print(w,len(w))

fruites=['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# Strategy:  Iterate over a copy
for index, item in enumerate(fruites):
    if len(item) <=4: 
        del fruites[index]

print(fruites)

#The Range Function
for i in range(5):
    print(i)

for i in range(5,10):
    print(i)
for i in range(0,10,2):
    print(i)
for i in range(-10,-100,-30):
    print(i)
#Print list with index using Range
for i in range(len(fruites)):
    print(i,fruites[i])
print('0+1+2+3= ',sum(range(4))) #0+1+2+3

print('odd num list: ',list(range(1,10,2)))

