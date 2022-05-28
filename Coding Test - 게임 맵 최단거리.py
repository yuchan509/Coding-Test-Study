from collections import deque

def solution(maps):

  n, m = len(maps), len(maps[0])
  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]

  q = deque()
  q.append([0, 0, 1])
  visited = [[False] * m for _ in range(n)]
  visited[0][0] = True

  while q:
   x, y, cnt = q.popleft()
   
   if x == n - 1 and y == m - 1: return cnt

   for idx in range(4):
     nx = x + dx[idx]
     ny = y + dy[idx]

     if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
       if maps[nx][ny] != 0:
         visited[nx][ny] = True
         q.append([nx, ny, cnt + 1])

  if visited[n-1][m-1] == False : return -1

  return cnt


# Run.(1 : 가능, 0 : 불가능)
maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]

solution(maps)