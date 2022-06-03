def solution(rows, columns, queries):

    answer = []
    arr = [[0] * columns for _ in range(rows)]

    v = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = v
            v += 1

    '''
        top    : starting row index : 2
        left   : starting col index : 2
        bottom : ending row index   : 5
        right  : ending col index1  : 4
    '''

    for t, l, b, r in queries:

        top, left, bottom, right =  t - 1, l - 1, b - 1, r - 1

        ans = []
        start = arr[top][left]
        ans.append(start)

        # row down.
        for i in range(top, bottom):   
            arr[i][left] = arr[i + 1][left]
            ans.append(arr[i + 1][left])

        # col right.
        for i in range(left, right):   
            arr[bottom][i] = arr[bottom][i + 1]
            ans.append(arr[bottom][i + 1])

        # col up.
        for i in range(bottom, top, -1):   
            arr[i][right] = arr[i - 1][right]
            ans.append(arr[i - 1][right])

        # row left.
        for i in range(right, left, - 1):
            arr[top][i] = arr[top][i - 1]
            ans.append(arr[top][i - 1])

        arr[top][left + 1] = start

        answer.append(min(ans))

    return answer


# Run.
rows, columns = 6, 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(rows, columns, queries)