def dynamicArray(n, queries):
    # Write your code here
    lastAnswer = 0
    arr = [[] for i in range(n)]
    ans = []

    for i in range(len(queries)):
        if int(queries[i][0]) == 1:
            x = int(queries[i][1])
            y = int(queries[i][2])
            idx = ((x ^ lastAnswer) % n)
            arr[idx].append(y)
            print(arr)
        else:
            x = int(queries[i][1])
            y = int(queries[i][2])
            idx = ((x ^ lastAnswer) % n)
            lastAnswer = arr[idx][y % len(arr[idx])]
            ans.append(lastAnswer)
    return ans


n, q = map(int, input().split())
queries = [input().split() for i in range(q)]
ans = dynamicArray(n, queries)

for val in ans:
    print(val)