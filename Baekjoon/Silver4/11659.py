N, M = map(int, input().split())

array = [0]
array = list(map(int, input().split()))


sum = [0] * (N+1)

for i in range(1, N+1):
    sum[i] += sum[i-1] + array[i-1]

result = []
for i in range(M):
    start, end = map(int, input().split())
    ans = sum[end] - sum[start-1]
    result.append(ans)

for val in result:
    print(val)