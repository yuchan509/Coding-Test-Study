def solution(A):
    ans, length = float('inf'), len(A)

    dp = [0] * length
    dp[0] = A[0]

    for i in range(1, length):
        dp[i] = dp[i - 1] + A[i]

    for i in range(1, length):
        left = dp[i - 1]
        right = dp[length - 1] - left
        ans = min(ans, abs(left - right))
    
    return ans

A = [3, 1, 2, 4, 3]
solution(A)