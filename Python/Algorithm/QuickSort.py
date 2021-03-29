import sys
import time
r=0
def quickSort(lst):
    global r
    r=r+1
    if len(lst)<=1:
        return lst
    pivot=lst[(len(lst)//2)]
    hi = [x for x in lst if x > pivot]
    mid = [x for x in lst if x == pivot]
    lo = [x for x in lst if x < pivot]
    return quickSort(lo) +mid + quickSort(hi)

#C++ Style 
def partition(arr,lo,hi):
    pivot=arr[hi]
    i=lo-1
    for j in range(lo,hi):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[hi]=arr[hi],arr[i+1]
    return i+1
def Qsort(arr,lo,hi):
    global r
    r=r+1
    if hi>lo:
        pi=partition(arr,lo,hi)
        Qsort(arr,lo,pi-1)
        Qsort(arr,pi+1,hi)



if __name__=="__main__":
    lst=[int(x) for x in sys.argv[1:]]
    arr=lst[:]
    start=time.time()
    print(quickSort(lst))
    print('Taken Time Quicksort: ',(time.time()-start)*1000)
    print('no of recurtion: ',r)
#    print(arr)
    start=time.time()
    r=0
    Qsort(arr,0,len(arr)-1)
    print(arr)
    print('Taken Time Qsort: ',(time.time()-start)*1000)
    print('no of recurtion: ',r)
