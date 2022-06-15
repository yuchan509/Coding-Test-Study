from itertools import permutations

def check(case, d):
    a, b, op, limit = list(d.replace("~", ""))
    if op == "=": op = "=="
    diff = str(abs(case.index(a) - case.index(b)) - 1)
    if eval(diff + op + str(limit)):
        return 1
    else:
        return 0

def solution(n, data):

    cnt, ans = 0, 0
    member = ['A', 'C', 'F', 'J', 'M', 'N', 'R', 'T']
    for case in permutations(member, len(member)):
        for d in data:
            cnt += check(case, d)

        if cnt == n:
            ans += 1
        cnt = 0 

    return ans

# Run.
# output : 2
n = 2
data = ["N~F=0", "R~T>2"]
solution(n, data)
    
# output : 0
n = 2
data = ["M~C<2", "C~M>1"]
solution(n, data)