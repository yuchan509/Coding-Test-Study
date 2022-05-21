r, c = map(int, input().split())
t, s = map(int, input().split())

# ansewer
ans = 0

# direct -> right : [0(fixed)][1] -> down : [1][0(fixed)] -> left :[0][-1] -> up : [-1][0]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# init value.
# direct : right : 0, down : 1, left : 2, up : 3
x, y, direct = 0, 0, 0

# Create empty array for Spiral array.(r X c array)
arr = [[0]*c for _ in range(r)]

# Create value(1 ~ r*c) 
for value in range(1, r*c+1):

  arr[x][y] = value
  x += dx[direct]
  y += dy[direct]

  # condition :
  if not 0 <= x < r or not 0 <= y < c or arr[x][y] != 0:
      x -= dx[direct]
      y -= dy[direct]

      # change direction.
      direct = (direct + 1) % 4
      x += dx[direct]
      y += dy[direct]

      if t < value < s:
        ans += 1

print(ans)