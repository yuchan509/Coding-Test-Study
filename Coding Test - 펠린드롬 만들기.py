# Create Dictionary
import math
from collections import Counter

ans = ""
dic = Counter(list("AABB"))

# Check len(odd) < 2.
mid = ""
chk = [k for k, v in dic.items() if v % 2 != 0]
if chk:
  mid += chk[0]

for i in sorted(dic):
  ans += i * math.floor(dic.get(i) / 2)

if len(chk) > 1:
  print("I'm Sorry Hansoo")
else:
  print(ans + mid + ans[::-1])
