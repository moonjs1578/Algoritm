# 1 : 1
# 2 : 3
# 3 : 5
# 4 : 11
# 5 : 21
# 6 : 43
# 7 : 85
# 8 : 171
# 짝수번 째 : 전꺼 + 1, 홀수번 째 : 전꺼 -1

n = int(input())
array = [0] * 1001
array[1] = 1


for idx in range(2, n+1):
    if idx%2==0:
        array[idx] = (2*array[idx-1] + 1) % 10007
    else:
         array[idx] = (2*array[idx-1] - 1) % 10007

print(array[n])