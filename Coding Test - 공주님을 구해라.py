import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
visited = [[0 for _ in range(m)] for i in range(n)]

def bfs():
    
    ans = []
    cnt = -1
    q = deque()
    q.append([0, 0, 0])
    
    while q:
        
        x, y, cnt = q.popleft()
        visited[x][y] = 1
        if x == n - 1 and y == m - 1:
            ans.append(cnt)
            break
            
        if arr[x][y] == 2:
            teleport = (n - x + m - y - 2) + cnt
            ans.append(teleport)
       
        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] != 1:
                    visited[nx][ny] = 1
                    q.append([nx, ny, cnt + 1])
    
    return "Fail"  if not len(ans) or min(ans) > t else min(ans)

print(bfs())


# Run.
'''
output : 10
6 6 16
0 0 0 0 1 1
0 0 0 0 0 2
1 1 1 0 1 0
0 0 0 0 0 0
0 1 1 1 1 1
0 0 0 0 0 0
'''

'''
output : Fail
3 4 100
0 0 0 0
1 1 1 1
0 0 2 0
'''