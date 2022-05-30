def solution(dirs):
      
  ans = set()
  dic = {"U" : (0, 1), "D" : (0, -1), "L" : (-1, 0), "R" : (1, 0)}
  x, y = 0, 0

  for d in dirs:
    _x, _y = x, y
    a, b = dic.get(d)
    if -6 < x + a < 6 and -6 < y + b < 6:
      x += a
      y += b
      ans.add((x, y, _x, _y))
      ans.add((_x, _y, x, y))

  return len(ans) // 2

# Run.
dirs = "ULURRDLLU"	
dirs = "LULLLLLLU"
solution(dirs)