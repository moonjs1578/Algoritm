N, M = map(int, input().split())

trees = list(map(int, input().split()))

left = 0
right = max(trees)
height = 0
while left<=right:
    mid = (left+right) // 2
    result = 0

    for tree in trees:
        dis = tree - mid
        if dis > 0:
            result += dis

    if result >= M:
        height = mid
        left = mid+1
    else:
        right = mid -1

print(height)