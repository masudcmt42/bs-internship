import time
import random

#simplified Way but Not Faster
def margeSort(lst):
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    left,right=margeSort(lst[:mid]),margeSort(lst[mid:])
    rst=[]
    for k in range(len(lst)):
        if len(left)<=0 or (len(right)>0 and left[0]>right[0]):
            rst.append(right.pop(0))
        else:
            rst.append(left.pop(0))
    return rst

#another fast way
def merge(left, right,A):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
	    if left[i] <= right[j]: A[k], i, k = left[i], i + 1, k + 1
	    else: A[k], j, k = right[j], j + 1, k + 1
    while i < len(left): A[k], i, k = left[i], i + 1, k + 1
    while j < len(right): A[k], j, k = right[j], j + 1, k + 1
def mSort(A):
    if len(A) < 2: return
    left, right = A[ : len(A) // 2], A[len(A) // 2 : ]
    mSort(left)
    mSort(right)
    merge(left, right, A)

# another simplified and faster Way
def mgSort(lst):
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    left,right=mgSort(lst[:mid]),mgSort(lst[mid:])
    i,j=0,0
   # print('unsorted: ',lst)
    for k in range(len(lst)):
        if i>=len(left): lst[k],j=right[j],j+1
        elif j>=len(right): lst[k],i=left[i],i+1
        elif left[i]<right[j]: lst[k],i=left[i],i+1
        else: lst[k],j=right[j],j+1
    #print('sorted:   ',lst)
    return lst
if __name__=="__main__":
	lst1=[random.randint(2,2000) for itr in range(100000)]
	lst2,lst3=lst1[:],lst1[:]
	print('Total element:',len(lst1))
	start=time.time()
	lst=margeSort(lst1)
	print('Total element:',len(lst1),"Time: ",(time.time()-start))
	print("Way 2")
	start=time.time()
	mSort(lst2)
	print('Total element:',len(lst2),"Time: ",(time.time()-start))
	print("Way 3")
	start=time.time()
	lst3=mgSort(lst3)
	print('Total element:',len(lst3),"Time: ",(time.time()-start))

