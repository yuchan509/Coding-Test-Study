from collections import deque

n, k = map(int, input().split())

MAX = 100001
arr = [0] * MAX

def bfs():
    
    q = deque()
    q.append([n, 0])

    while q:
        x, cnt = q.popleft()
        arr[x] = 1

        if x == k:
            break

        for pos in [x - 1, x + 1, x * 2]:
            if 0 <= pos < MAX and not arr[pos]:
                arr[pos] = 1
                q.append([pos, cnt + 1])

    return cnt

print(bfs())

# Run.
'''
output : 4
5 17
'''
