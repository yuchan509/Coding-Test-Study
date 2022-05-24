''''
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:
    
  A = [0, 1, 0, 1, 1]

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

    - 0 represents a car traveling east, --> P : 0 
    - 1 represents a car traveling west. --> Q : 0

We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
'''

## Prifixs sum

# solve.01 (50%)
from collections import deque
def solution(A):
    q = deque(A)
    ans = 0
    for i in A:
        if i == 0:
            q.popleft()
            cnt += q.count(1)
            if ans > 1E9:
                return -1
        else:
            q.popleft()
    return ans

# solve.02 (50%)
def solution(A):
    ans = 0 
    for idx, v in enumerate(A):
        if v == 0:
            ans += sum(A[idx:])
            if ans > 1E9:
                return -1
    return ans


# solve.03 (100%)
def solution(A):
    ans = 0 
    cnt = 0
    for v in A:
        if v == 0:
            cnt += 1
        else:
            ans += cnt
            
    if ans > 1e9: 
        return -1
    return ans

A = [0, 1, 0, 1, 1]
solution(A)