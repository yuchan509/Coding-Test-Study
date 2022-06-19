def solution(n, times):
    left, right = min(times), n * max(times)

    while left <= right:

        res = 0
        mid = (left + right) // 2     

        for i in times:
            res += mid // i 

        if res >= n:
            right = mid - 1
        else:
            left = mid + 1

    return left


# Run.
n = 6
times = [7, 10]
solution(n, times)
