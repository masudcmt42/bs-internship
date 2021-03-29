def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=',')
        a,b=b,a+b
    print()
def fib2(n):
    result=list()
    a, b= 0, 1
    while a<n:
        result.append(a)
        a, b= b, a+b
    return result
"""
Executing modules as scripts
***********************************
When you run a Python module with
python fibo.py <arguments>
the code in the module will be executed, just as if you imported it, 
but with the __name__ set to "__main__". T
hat means that by adding this code at the end of your module:
"""


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

"""you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file:
$ python fibo.py 50"""
