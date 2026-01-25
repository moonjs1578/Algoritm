import sys
from collections import deque

def bfs(start):
    visited[start] = True
    queue = deque()
    queue.append(start)

    while queue:
        current = queue.popleft()
        for x in graph[current]:
            if not visited[x]:
                queue.append(x)
                visited[x] = True

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)

