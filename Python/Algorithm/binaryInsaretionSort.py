import time
import sys
def binaryInSort(lst):
    for i in range(len(lst)):
        key,position=lst[i],binarySearch(lst,lst[i],i-1)
        lst=lst[:position]+[key]+lst[position:i]+lst[i+1:]
    return lst

def biInSort(lst):
    for i in range(len(lst)):
        key,position,j=lst[i],binarySearch(lst,lst[i],i-1),i-1
        #lst=lst[:position]+[key]+lst[position:i]+lst[i+1:]
        while j>=position: lst[j+1],j=lst[j],j-1
        lst[position]=key
    return lst


def binarySearch(lst,key,end,start=0):
    while start<=end:
        mid=start+(end-start)//2;
        if key<lst[mid]: end=mid-1
        else: start=mid+1
    return start
st=time.time()
print(binaryInSort([37, 23, 0, 17, 12, 72, 31,46, 100, 88, 54]))
print('Execution Time:(ms) ',(time.time()-st)*1000)
st=time.time()
print(biInSort([37, 23, 0, 17, 12, 72, 31,46, 100, 88, 54]))
print('Execution Time:(ms) ',(time.time()-st)*1000)
   
