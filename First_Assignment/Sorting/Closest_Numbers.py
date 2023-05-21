#!/usr/bin/env python3

N = int(input())
arr = [int(x) for x in input().split()]
arr.sort()

result = []
diff = 2**31-1
for i in range(1, len(arr)):
    if arr[i] - arr[i-1] <= diff:
        if arr[i] - arr[i-1] < diff:
            diff = arr[i] - arr[i-1]
            result = []
        result.append(arr[i])
        result.append(arr[i-1])

print(' '.join([str(x) for x in sorted(result)]))