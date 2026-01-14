# 2 : 2
# 3 : 3
# 4 : 5
# 5 : 8
# 6 : 13
# 7 : 21
# 8 : 34
# 9 : 55

n = int(input())
array = [0]*1001

array[1] = 1
array[2] = 2

if n==1:
    print(array[n])
elif n == 2:
    print(array[n])
else:
    for i in range(3, n+1):
        array[i] = (array[i-1] + array[i-2]) % 10007
    print(array[n])