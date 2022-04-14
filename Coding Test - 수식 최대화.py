import re
from itertools import permutations

def solution(expression):
  op = ['+', '-', '*']
  case = [i for i in permutations(op, 3)]
  answer = 0

  for c in case:
    ex = re.split('(\D)', expression)
    for op in c :
      for _ in range(ex.count(op)): 
        idx = ex.index(op)
        next = str(eval(''.join(ex[idx-1:idx+2])))
        for _ in range(3) :
          ex.pop(idx-1)
        ex.insert(idx-1, next)

    answer = max(abs(int(ex[0])), answer)

  return answer

solution(expression)