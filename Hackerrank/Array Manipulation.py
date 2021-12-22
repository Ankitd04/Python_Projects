def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n + 2)
    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k
        # print(arr)

    maxnum = temp = 0
    for val in arr:
        temp += val
        maxnum = max(maxnum, temp)

    return maxnum


n, m = map(int, input().split())
queries = []
for i in range(m):
    queries.append(list(map(int, input().split())))

ans = arrayManipulation(n, queries)
print(ans)