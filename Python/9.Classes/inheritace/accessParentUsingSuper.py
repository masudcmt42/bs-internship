class GFG1:
    def __init__(self):
        print('HEY!!!!!!GfG I am initialised(class GFG1)')

    def sub_GFG(self,b):
        print('Printing From Class GFG1: ',b)
class GFG2(GFG1):
    def __init__(self):
        print('HEY!!!!!!GfG I am initialised(class GFG2)')
        super().__init__()
    def sub_GFG(self,b):
        print('Printing From Class GFG1: ',b)
        super().sub_GFG(b+1)
class GFG3(GFG2):
    def __init__(self):
        print('HEY!!!!!!GfG I am initialised(class GFG3)')
        super().__init__()
    def sub_GFG(self,b):
        print('Printing From Class GFG1: ',b)
        super().sub_GFG(b+1)
if __name__=="__main__":
    import sys
    gfg=GFG3()
#    print('systhem input: ',sys.argv[0],sys.argv[1],len(sys.argv))

    gfg.sub_GFG(int(input('Enter Number: ') if len(sys.argv)<=1 else sys.argv[1]))
