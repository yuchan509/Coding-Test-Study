n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]           

def dfs(x, y):
  visited[x][y] = True
  global cnt

  if graph[x][y] == 1:
    cnt += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if visited[nx][ny] == False and graph[nx][ny] == 1:
          dfs(nx, ny)

cnt = 0
house = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and visited[i][j] == False:
      dfs(i, j)
      house.append(cnt)
      cnt = 0

print(len(house))
for i in sorted(house):
  print(i)