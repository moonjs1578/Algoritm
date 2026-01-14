from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start):
    cnt = 0
    q = deque([start])
    visited[start] = True
    while q:
        current = q.popleft()
        
        for node in graph[current]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
                cnt+=1
    return cnt

visited = [False] * (N+1)

print(bfs(1))