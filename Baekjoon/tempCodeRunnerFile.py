N, M = map(int, input().split())

dogam = {}

for i in range(1, N+1):
    name = input().split()
    dogam[name] = i
    dogam[i] = name
    
for i in range(M):
    query = input().split()
    print(dogam[query])
    
