f = open('workfile','w') #open file as write mode
print(f.closed)
f.close()
#it is eqv to
with open('workfile') as f:
    read_date=f.read() 
#check that the file has been automatically closed
print(f.closed)

#Method of FIle Object
f=open('workfile2','r+')
s=f.read()
print(s)
print(f.read()) #will print '' becuse cursor already reach EOF
f=open('workfile3','r+')
s=f.readline()
s2=f.readline()
print(s,s2)
print(f.readline())     #print will be blank

f.seek(0,0)
for line in f:
    print(line,end=' ')
#Writting File
f.write('This is a Test\n')
nn=f.write('This is a Test2\n') #this is return the number of char is written
print(nn)

#other types of object neetd to be converted as string
value =('the ans',42) # this is tuple
s=str(value)
print(f.write(s))
f.close()
#seek function, To change the file object’s position, use f.seek(offset, whence) 
# whence 0= measures from the beginning of the file
# whence 1= uses the current file position
# whence 2= uses the end of the file as the reference point.
f=open('workfile4','rb+')
f.write(b'123456789abcdef')
print(f.seek(5))
print(f.read(1))
print(f.seek(-3,2))
print(f.read(1))

