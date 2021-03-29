try:
    raise Exception('spam','eggs')
except Exception as ints:
    print(type(ints))
    print(ints.args)
    print(ints)
    x,y=ints.args
    print('X = {0} Y = {1}'.format(x,y))
