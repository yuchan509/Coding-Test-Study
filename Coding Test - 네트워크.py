from collections import deque

def bfs(n, computers, node, visited):
  q = deque()
  q.append(node)

  while q:
    r = q.popleft()

    for c in range(n):
      if r != c and computers[r][c] != 0 and not visited[c]:
        visited[c] = True
        q.append(c)
  
  return 1
      
def solution(n, computers):
  ans = 0
  visited = [False] * n

  for idx in range(n):
    if not visited[idx]:
      ans += bfs(n, computers, idx, visited)

  return ans


# Run.
n = 3
computers = [[1, 1, 0], 
             [1, 1, 0], 
             [0, 0, 1]]

solution(n, computers)