N = int(input())

array = list(map(int, input().split())) 
array.sort()

result = []
result.append(array[0])

for i in range(1, N):
    num = result[i-1] + array[i]
    result.append(num)
    
print(sum(result))