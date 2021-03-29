def scope_test():
    def do_local():
        spam='the local spam'
    def do_nonlocal():
        nonlocal spam
        spam='the nonlocal spam'
    def do_global():
        global spam
        spam='the Global spam'
    spam='the test spam'
    do_local()
    print('After local assignment:',spam)
    do_nonlocal()
    print('After nonlocal assignment:',spam)
    do_global()
    print('After global assignment:',spam)
scope_test()
print('In Global assignment:',spam)
