from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
         queue.append([i, j])

def bfs():
  while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
            
print(max(map(max, graph)) - 1)