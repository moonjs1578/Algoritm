# 1 : 1가지
# 2 : 2가지 
# 3 : 4가지
# 4 : 7
# 5 : 13
# 6 : 24
# 7 : 44

N = int(input())
array = [0] * 11
array[1] = 1
array[2] = 2
array[3] = 4

for _ in range(N):
    x = int(input())
    
    for i in range(4, x+1):
        array[i] = array[i-1] + array[i-2] + array[i-3]
    print(array[x])
    