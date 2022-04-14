import re

def solution(s):
  modify_s = [re.split('\D', i) for i in 
              list(filter(None, re.split('[{}]', s))) if i != ',']
  modify_s.sort(key=len)

  answer = []
  for e in sum(modify_s, []):
    if e not in answer:
      answer.append(e)

  return list(map(int, answer))