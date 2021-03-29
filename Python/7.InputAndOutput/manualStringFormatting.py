for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3),end=" ")
    print(repr(x*x*x).rjust(4))
"""The str.rjust() method of string objects right-justifies a string in a field of a given width by padding it with spaces on the left. There are similar methods str.ljust() and str.center()."""

#another method str.zfill()
print('12'.zfill(5))
print('-7.43'.zfill(7))
print('3.141592655359'.zfill(5))

