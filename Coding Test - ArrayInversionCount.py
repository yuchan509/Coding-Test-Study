# 2. inversion counting.
# N is an integer within the range [0..100,000];
# computes the number of inversions in A, or returns −1 if it exceeds 1,000,000,000.

'''
# Min Heap.
# [-1, 6, 3, 4, 7, 4]

# leve1 1 : (-1, 0)
# leve1 2 : (4, 3), (3, 2)
# leve1 3 : (6, 1), (7, 4), (4, 5)

---------------------------------
# cnt = 0
# sorted_list = [0]
# value : -1, index : 0


# leve1 1 : (3, 2)
# leve1 2 : (4, 3), (4, 5)
# leve1 3 : (6, 1), (7, 4), 

---------------------------------
# cnt = 1
# sorted_list = [0, 2*]
# value : 3, index : 2

# leve1 1 : (4, 3)
# leve1 2 : (6, 1), (4, 5)
# leve1 3 : (7, 4)

---------------------------------
# cnt = 1
# sorted_list = [0, 2, 3*]
# value : 4, index : 3

# leve1 1 : (4, 5)
# leve1 2 : (6, 1), (7, 4)
# leve1 3 : 

---------------------------------
# cnt = 2
# sorted_list = [0, 2, 3, 5*]
# value : 4, index : 5

# leve1 1 : (6, 1)
# leve1 2 : (7, 4)
# leve1 3 : 

---------------------------------
# cnt = 0
# sorted_list = [0, 1*, 2, 3, 5]
# value : 6, index : 1

# leve1 1 : (7, 4)
# leve1 2 : 
# leve1 3 : 

---------------------------------
# cnt = 0
# sorted_list = [0, 1, 2, 3, 4*, 5]
# value : 7, index : 4

# leve1 1 : 
# leve1 2 : 
# leve1 3 : 
'''

from bisect import bisect_left, insort_left
from heapq import heappush, heappop

def solution(A):
    
    if len(A) < 2: return 0
    
    min_heap = []
    for idx, value in enumerate(A):
        heappush(min_heap, (value, idx))
    print(min_heap)
    
    sorted_list = []
    ans = 0
    while min_heap:
        value, idx = heappop(min_heap)
        
        insort_left(sorted_list, idx)
        print(min_heap, idx - bisect_left(sorted_list, idx) )
        ans += idx - bisect_left(sorted_list, idx) 
        
        if ans > 1e9: return -1

    return ans


def solution(A):

    if len(A) < 2: return 0

    sorted_left = []
    ans = 0
    for i in range(1, len(A)):
            insort_left(sorted_left, A[i-1])
            ans += i - bisect_left(sorted_left, A[i])

            if ans > 1e9: return -1
    return ans


# Run.
A = [-1, 6, 3, 4, 7, 4]
solution(A)