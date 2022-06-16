from collections import deque

r, c = map(int, input().split())

arr = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    
    wolf, sheep = 0, 0
    
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        
        if arr[x][y] == "o": 
            sheep += 1

        if arr[x][y] == "v":
            wolf += 1

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if arr[nx][ny] != "#":
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                  
    return (sheep, 0) if wolf < sheep else (0, wolf)

s, w = 0, 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != "#" and not visited[i][j]:
            a, b = bfs(i, j)
            s += a
            w += b
            
print(s, w)


# Run.
'''
output : 0 2
6 6
...#..
.##v#.
#v.#.#
#.o#.#
.###.#
...###
'''