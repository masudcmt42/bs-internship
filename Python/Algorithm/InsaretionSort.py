import time
import sys
def iSort(lst):
    for i in range(len(lst)):
        key,j=lst[i],i-1
        while j>=0 and lst[j]>key: lst[j+1],j=lst[j],j-1
        lst[j+1]=key
    return lst
if __name__=="__main__":
    lst=[int(x) for x in sys.argv[1:]]
    arr=lst[:]
    start=time.time()
    print(iSort(lst))
    print('Taken Time Quicksort(ms): ',(time.time()-start)*1000)
