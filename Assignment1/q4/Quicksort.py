'''

'''
def quicksort(A, lo, hi):
    '''
This function computes quicksort
:param: A: Array that will be sorted
:param: lo and hi: pointers used to partitioning
Time Complexity: O(N*log(N)) 
'''
    if hi > lo:
        pivot = A[lo]
        left, right = partition(A, lo, hi, pivot)
        quicksort(A, lo, left-1)
        quicksort(A, right, hi)
        
def partition(A, lo, hi, pivot):
    mid = lo
    while mid <= hi:
        if A[mid] < pivot:
            A[mid], A[lo] = A[lo], A[mid]
            lo += 1
            mid += 1
        elif A[mid] == pivot:
            mid += 1
        else:
            A[mid], A[hi] = A[hi], A[mid]
            hi -= 1
    return lo, mid
