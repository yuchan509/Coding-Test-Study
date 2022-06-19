import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            
def bfs(x, y):
    
    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])
    return 1 

ans, cnt, limit, maxv = 0, 0, 0, max(sum(arr, []))
while limit <= maxv :
    
    res = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] <= limit:
                visited[i][j] = 1
                cnt += 1
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                res += bfs(i, j)
    
    ans = max(ans, res)     
    limit += 1

print(ans)


# Run.
'''
output : 5
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
'''

'''
output : 6
7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9
'''