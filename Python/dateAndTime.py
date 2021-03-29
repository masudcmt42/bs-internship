import datetime as d     #for display current date

x=d.datetime.now()
print(x) #current Date
print(x.year)   #display Year only
print(x.strftime("%A")) #display WeekDay

#create a object
X=d.datetime(2020,5,17)
print(X)

#The strftime() Method
"""The datetime object has a method for formatting date objects into readable strings.
The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:"""

print(X.strftime("%B"))
