def solution(lines):
    ans = []

    for line in lines:
        date, s, t = line.split()
        s = s.split(":")
        t = t[:-1]

        end = (int(s[0]) * 3600 + int(s[1]) * 60 + float(s[-1])) * 1000
        start = 1 + end - float(t) * 1000
        ans.append([end, start])
    
    
    max_cnt = 0
    for t1 in ans:
        cnt = 0
        for t2 in ans:
            if t2[0] >= t1[0] and t2[-1] < t1[0] + 1000:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
        
    return max_cnt