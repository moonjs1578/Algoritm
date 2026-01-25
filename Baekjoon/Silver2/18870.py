N = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(set(arr))

compress = {}
for i, v in enumerate(sorted_arr):
    compress[v] = i

for x in arr:
    print(compress[x], end=" ")