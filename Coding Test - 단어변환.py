from collections import deque

def oneCheck(x, y):
  cnt = 0
  for i, j in zip(x, y):
    if i != j:
      cnt += 1
      if cnt > 1 :
        return 0
  return 1

def solution(begin, target, words):
  if target not in words: return 0

  q = deque()
  q.append([begin, 0])
  visited = [False for _ in range(len(words))] 

  while q:
    current_word, cnt = q.popleft()

    if current_word == target: return cnt

    for idx, word in enumerate(words):
      if oneCheck(current_word, word) == 1 and visited[idx] == False:
        visited[idx] = True
        q.append([word, cnt + 1])

  return cnt

# Run.
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

solution(begin, target, words)