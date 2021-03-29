import sys
try:
    f=open('nyfike.txt','r')
    s=f.readline()
    i=int(s.strip())
except OSError as err:
    print('Os Error: {0}'.format(err))
except ValueError:
    print('could not convert data into int')
except:
    print('Unexceptd Error:',sys.exc_info()[0])
    raise

