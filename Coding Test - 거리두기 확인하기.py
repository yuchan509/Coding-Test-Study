# 모든 P(앉아 있는 사람)를 기준으로 탐색. --> bfs 이용.
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


from collections import deque

def bfs(place): 
  PList  =  []
  for i in range(len(place)):
    for j in range(len(place[0])):
      if place[i][j] == "P": PList.append([i, j])

  for p in PList:
    queue = deque([p])
    visited = [[False]*5 for _ in range(5)]
    distance = [[0]*5 for _ in range(5)]
    visited[p[0]][p[-1]] = True

    while queue:
      x, y = queue.popleft()

      dx = [0, 0, -1, 1]
      dy = [1, -1, 0, 0]  

      for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < 5 and 0 <= ny < 5:
          if not visited[nx][ny] and place[nx][ny] != "X":

            if place[nx][ny] == "O":
              visited[nx][ny] = True
              queue.append([nx, ny])
              distance[nx][ny] = distance[x][y] + 1

            if place[nx][ny] == "P" and distance[x][y] < 2:
              return 0

  return 1

def solution(places):
  answer = []
  for place in places:
    answer.append(bfs(place))
  return answer

solution(places)