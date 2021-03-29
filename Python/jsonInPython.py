import json     #import Module
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)   #parse X
print(y["age"])     # the result is a Python dictionary


#Convert from Python to JSON
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y=json.dumps(x)     # convert into JSON
print(y)        # the result is a JSON string


"""
You can convert Python objects of the following types, into JSON strings
Python 	JSON
dict 	Object
list 	Array
tuple 	Array
str 	String
int 	Number
float 	Number
True 	true
False 	false
None 	null
"""
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
#Convert a Python object containing all the legal data types
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
# use four indents to make it easier to read the result
print(json.dumps(x, indent=4))
#Use the separators parameter to change the default separator
json.dumps(x, indent=4, separators=(". ", " = "))
#Use the sort_keys parameter to specify if the result should be sorted or not
json.dumps(x, indent=4, sort_keys=True)
