from collections import defaultdict, deque

def solution(n, vertex):
  graph = defaultdict(list)

  for a, b in vertex:
    graph[a].append(b)
    graph[b].append(a)

  ans = {}
  q = deque()
  q.append([1, 0])
  visited = [False] * (n + 1)

  while q:
    check = 0
    node, depth = q.popleft()
    ans[node] = depth
    visited[node] = True

    for i in graph[node]:
      if not visited[i]:
        visited[i] = True
        q.append([i, depth + 1])
        
  answer = len([k for k, v in ans.items() if v == max(ans.values())])
  return answer

# Run.
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, vertex)