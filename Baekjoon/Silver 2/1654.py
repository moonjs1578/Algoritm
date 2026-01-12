N, K = map(int, input().split())
array = []
for i in range(N):
    array.append(int(input()))

left = 1
right = max(array)
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for length in array:
        cnt += length // mid
    
    if cnt >= K :
        answer = mid
        left = mid + 1
    else:
        right = mid -1

print(answer)