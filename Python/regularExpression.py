import re       #import module
text="the rain in spain"
x=re.search("^the.*spain$",text)
print(x)        #this will return a Match Object
#Match Object has property
print(x.span()) #returns a tuple containing the start-, and end positions of the match.
print(x.string) #returns the string passed into the function
print(x.group())#returns the part of the string where there was a match
print(x.start()) 
#The findall() function returns a list containing all matches.
print(re.findall('ai',text))

#The split() function returns a list where the string has been split at each match
print(re.split('\s',text))
#The sub() function replaces the matches with the text of your choice
print(re.sub('\s','-',text))

