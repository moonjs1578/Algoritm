N, M = map(int, input().split())

dogam = {}

for i in range(1, N+1):
    name = input()
    dogam[name] = i
    dogam[str(i)] = name
    
for i in range(M):
    query = input()
    print(dogam[query])
    
