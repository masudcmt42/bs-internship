try:
    raise NameError('HiThere')
except NameError:
    print('An Exception flew by!')
    raise    #again raise Exception of NameError

