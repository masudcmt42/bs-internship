from random import randint
from timeit import repeat
from bubbleSort import bSort
from InsaretionSort import iSort
from QuickSort import quickSort,Qsort
from margeSort import margeSort,mSort,mgSort

import sys

def run_algorithm(algo,lst,com=''):
    setUpCode=f"from __main__ import {algo}" \
            if algo !="sorted" else ""
    #print(setUpCode)
    stmt=f"{algo}({lst})"
    times=repeat(setup=setUpCode,stmt=stmt,repeat=3,number=10)

    print(f"Algorithm: {algo} {com}. Minimum execution time: {min(times)}")

if __name__=="__main__":
    SIZE=int(sys.argv[1])
    lst=[randint(0,10000) for i in range(SIZE)]
    if SIZE>5000: print("Insaretion sort Cann't hendel more then 1000 element")
    else: run_algorithm(algo="iSort",lst=lst)
    if SIZE>1000: print("Bubble sort Cann't hendal more then 100 element")
    else:
        run_algorithm(algo="bSort",lst=lst,com="Slow Algo")
    run_algorithm(algo="sorted",lst=lst)
    run_algorithm(algo="quickSort",lst=lst)
    run_algorithm(algo="margeSort",lst=lst,com="Slow Algo")
    run_algorithm(algo="mSort",lst=lst,com="faster Algo")
    run_algorithm(algo="mgSort",lst=lst,com="faster Algo")
