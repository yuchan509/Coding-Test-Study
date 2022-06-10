from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):

    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            
            if 0 <= nx < m and 0 <= ny < n:
                if arr[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return 1

res = []
for _ in range(int(input())):

    m, n, k= map(int, input().split())

    arr = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]

    for _ in range(k):
        r, c = map(int, input().split())
        arr[r][c] = 1
    
    
    ans = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and visited[i][j] == False:
                ans += bfs(i, j)
    
    res.append(ans)

for r in res:
    print(r)


# Run.
'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''