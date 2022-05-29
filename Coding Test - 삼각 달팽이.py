def solution(n):
  arr = [[0] * i for i in range(1, n + 1)]

  # down -> right -> cross
  dx = [1, 0, -1]
  dy = [0, 1, -1]

  # init value.
  x, y, direct = 0, 0, 0

  for value in range(1, len(sum(arr, [])) + 1):

    arr[x][y] = value
    x += dx[direct]
    y += dy[direct]

    
    # [0][0] -> [1][0] -> [2][0] -> [3][0] -> [4][0](cancle) : [3][0]
    # -> [3][1] -> [3][2] -> [3][3] -> [2][2]
    if not 0 <= x < n or not 0 <= y < len(arr[x]) or arr[x][y] != 0:
      
      x -= dx[direct]
      y -= dy[direct]

      direct = (direct + 1) % 3

      x += dx[direct]
      y += dy[direct]
    
  ans = sum(arr, [])
  return ans


# Run.
n= 4
solution(n)