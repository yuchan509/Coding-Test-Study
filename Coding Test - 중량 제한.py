# Maximum Spanning Tree. (union - find)
class MST:
    def __init__(self, vertices):
        self.v = vertices 
        self.edges = []

    def addEdges(self, a, b, weight):
        self.edges.append((weight, a, b))
        
    def find(self, parent, x):
        if parent[x] == x:
            return x
        return self.find(parent, parent[x])
    
    def union(self, parent, x, y):
        rx, ry = self.find(parent, x), self.find(parent, y)
 
        if rx < ry:
            parent[ry] = rx
        else:
            parent[rx] = ry
            
    def kruskalMST(self, start, end):
        parent = [i for i in range(n + 1)]
        self.edges.sort(key = lambda x : -x[0])

        for edge in self.edges:
            weight, a, b = edge
            self.union(parent, a, b)
    
            if self.find(parent, start) == self.find(parent, end):
                print(weight)
                break
                
                
n, m = map(int, input().split())

mst = MST(n)
for _ in range(m):
    a, b, weight = map(int, input().split())
    mst.addEdges(a, b, weight)
    
start, end = map(int, input().split())
mst.KruskalMST(start, end)



# BFS + Parametric Search.
import sys
from collections import deque, defaultdict

input = sys.stdin.readline
n, m = map(int, input().split())
d = defaultdict(list)

for _ in range(m):
    a, b, weight = map(int, input().split())
    d[a].append((b, weight))
    d[b].append((a, weight))
    
start, end = map(int, input().split())

def bfs(k: int) -> bool:
    
    visited = [False] * (n + 1)
    q = deque()
    q.append(start)
    visited[start] = 1
    
    while q:
        x = q.popleft()
        
        for node, weight in d[x]:
            if weight >= k and not visited[node]:
                visited[node] = 1
                q.append(node)
                
    return visited[end]

left, right = 1, int(1e9)

while left <= right:
    mid = (left + right) // 2
    
    if bfs(mid): 
        left = mid + 1
    else:
        right = mid - 1

print(right)


# Run.
'''
3 3
1 2 2
3 1 3
2 3 2
1 3
'''