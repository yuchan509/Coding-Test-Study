from collections import deque

n, l, r = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

d = [[0, 1], [0, -1], [-1, 0], [1, 0]]

def bfs(x, y):
    
    total, cnt = 0, 0
    
    m = deque()
    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        
        m.append([x, y])
        total += arr[x][y]
        cnt += 1

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                distance = abs(arr[nx][ny] - arr[x][y])
                
                if l <= distance <= r:
                    visited[nx][ny] = 1
                    q.append([nx, ny])

    while m:
        i, j = m.popleft()
        arr[i][j] = total // cnt
    
    return  1 if cnt != 1 else 0

ans = 0
while 1:
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += bfs(i, j)
    
    if not cnt:
        break

    ans += 1
    
print(ans)


# Run.
'''
output : 3
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
'''