import sys
input = sys.stdin.readline

N, M = map(int, input().split())

no_listener = set()
for _ in range(N):
    no_listener.add(input().strip()) 

no_watcher = set()
for _ in range(M):
    no_watcher.add(input().strip())

# result = sorted(list(no_listener & no_watcher))

result = set()

for name in no_watcher:
    if(no_listener.__contains__(name)):
        result.add(name)

result = sorted(result)

print(len(result))
for name in result:
    print(name)
    
# no_listener.__contains__(name) -> list를 써서 풀면 시간 복잡도 n, set을 써서 풀면 Hash값으로 바로 찾아서 시간 복잡도 더 낮음
