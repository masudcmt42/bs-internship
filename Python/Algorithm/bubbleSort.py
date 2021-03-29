import sys
import time
def bSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
                if lst[j]>lst[j+1]: lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

if __name__=="__main__":
    lst=[int(x) for x in sys.argv[1:]]
    arr=lst[:]
    start=time.time()
    print(bSort(lst))
    print('Taken Time Quicksort(ms): ',(time.time()-start)*1000)
