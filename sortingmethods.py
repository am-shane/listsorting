#Algorithm:
#4/13/20
#Austin Shane
#Algorithm: demonstrates use of Bubblesort, selectionsort, insertionsort, mergesort, and quicksort functions
#           main function uses createRandList function to create a random list, information contained in each functions
#           docstring is printed, and each function is ran on a newly generated random list, with the output
#           sorted as according to the methods of each function type.

#sources used: https://www.geeksforgeeks.org/generating-random-number-list-in-python/
#              https://stackoverflow.com/questions/12097033/python-index-error-value-not-in-list-on-indexvalue

import random

def BubbleSort(list):
    '''--BUBBLE SORT--
    Stable : YES
    In Place / Extra Memory : IN PLACE
    Expensive Operations: multiple passes through list, linear access time, swap/write operations
    Best Case Runnng Time: O(n)
    Average Running Time: O(n^2)
    Worst Case Running Time: O(n^2)
    When Used:  Smaller lists or lists that are already mostly sorted, but typically used for education.
    '''
    sortCheck = False
    while sortCheck == False:
        for item in range(len(list)):
            for i in range(0, (len(list))-item-1):
                if list[i] > list[i+1]:
                    list[i],list[i+1] = list[i+1],list[i]

        if list == sorted(list):
            sortCheck = True

def SelectionSort(list):
    '''--SELECTION SORT--
    Stable : NO
    In Place / Extra Memory : IN PLACE
    Expensive Operations: memory write operations
    Best Case Running Time: O(n^2)
    Average Running Time: O(n^2)
    Worst Case Running Time: O(n^2)
    When Used: Smaller lists, low memory environments, partially sorted subarrays
    '''
    sortCheck = False
    while sortCheck == False:
        for item in range(len(list)):
            minimum = item
            for i in range(item+1, len(list)):
                if list[minimum] > list[i]:
                    minimum = i
            list[item],list[minimum] = list[minimum],list[item]
        if list == sorted(list):
            sortCheck = True

def InsertionSort(list):
    '''--INSERTION SORT--
    Stable : YES
    In Place / Extra Memory : IN PLACE
    Expensive Operations: Inserting elements- requires shifting all elements over one.
    Best Case Running Time: O(n)
    Average Running Time: O(n^2)
    Worst Case Running Time: O(n^2)
    When Used: data nearly sorted, smaller size list, as a recursive base case
    '''
    sortCheck = False
    while sortCheck is False:
        for item in range(1, len(list)):
            temp = list[item]
            i = item-1
            while i >= 0 and temp < list[i]:
                list[i+1] = list[i]
                i -=1
            list[i+1] = temp
        if list == sorted(list):
            sortCheck = True

def MergeSort(list):
    '''--MERGE SORT--
    Stable : YES
    In Place / Extra Memory : NOT IN PLACE, MAY USE EXTRA MEMORY
    Expensive Operations: Recursively dividing halves, merging sublists
    Best Case Running Time: O(n log(n))
    Average Running Time: O(n log(n))
    Worst Case: O(n log(n))
    When Used: to guarantee a consistent running time regardless of input, more efficient comparisons, unknown data sets.
    '''
    sortCheck = False
    while sortCheck is False:
        if len(list) > 1:
            i,j,n = 0,0,0
            midpoint = len(list)//2
            half1, half2 = list[:midpoint], list[midpoint:]
            half1Length, half2Length = len(half1), len(half2)
            MergeSort(half1)
            MergeSort(half2)
            while i < half1Length and j < half2Length:
                if half1[i] < half2[j]:
                    list[n] = half1[i]
                    i+=1
                else:
                    list[n] = half2[j]
                    j+=1
                n+=1
            while i < half1Length:
                list[n] =half1[i]
                i+=1
                n+=1
            while j < half2Length:
                list[n] = half2[j]
                j+=1
                n+=1
        if list == sorted(list):
            sortCheck = True

def QuickSort(list, begin=None, end=None):
    '''--QUICK SORT--
    Stable : NO
    In Place / Extra Memory : IN PLACE
    Expensive Operations: iteration over sub-arrays, choosing adequate pivot, swapping elements
    Best Case Running Time: O(n log(n))
    Average Running Time: O(n log(n))
    Worst Case: O(n^2)
    When Used: Arrays, especially in linked lists, faster sort times, when real-time processing is required
    '''
    if begin is None and end is None:
        begin = 0
        end = len(list) -1
    if begin >= end:
        return
    partition = partitioner(list, begin, end)
    QuickSort(list, begin, partition-1)
    QuickSort(list, partition+1, end)

def partitioner(list, begin, end):
    '''partitioner function used in quicksort'''
    base = list[begin]
    lower = begin+1
    higher = end
    complete = False
    while complete is False:
        while lower <= higher and list[higher] >= base:
            higher -=1
        while lower <= higher and list[lower] <= base:
            lower += 1
        if lower <= higher:
            list[lower], list[higher] = list[higher],list[lower]
        else:
            complete = True
    list[begin], list[higher] = list[higher], list[begin]
    return higher

def createRandList():
    '''creates a list of 15 random numbers between 1 and 125'''
    randList = [random.randrange(1,125,1) for number in range(15)]
    return randList

def main():
    print("random lists are generated by createRandList function, which \n", createRandList.__doc__)
    print("_____________________________________________________________")
    print(BubbleSort.__doc__)
    randList = createRandList()
    print("generating new random list...")
    print("random list:", randList)
    BubbleSort(randList)
    print("using Bubble Sort:", randList)

    print("_____________________________________________________________")
    print(SelectionSort.__doc__)
    randList = createRandList()
    print("generating new random list...")
    print("random list:", randList)
    SelectionSort(randList)
    print("using Selection Sort:", randList)

    print("_____________________________________________________________")
    print(InsertionSort.__doc__)
    randList = createRandList()
    print("generating new random list...")
    print("random list:", randList)
    InsertionSort(randList)
    print("using Insertion Sort:", randList)

    print("_____________________________________________________________")
    print(MergeSort.__doc__)
    randList = createRandList()
    print("generating new random list...")
    print("random list:", randList)
    MergeSort(randList)
    print("using Merge Sort:", randList)

    print("_____________________________________________________________")
    randList = createRandList()
    print(QuickSort.__doc__)
    print("generating new random list...")
    print("random list:", randList)
    QuickSort(randList)
    print("using Quick Sort:", randList)

main()