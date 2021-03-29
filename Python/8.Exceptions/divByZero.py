def this_fails(s):
    return s/0
try:
    x=this_fails(10)
except ZeroDivisionError as arr:
    print('Handling rum-time error:',arr)

