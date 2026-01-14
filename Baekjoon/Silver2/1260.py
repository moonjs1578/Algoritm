from collections import deque

def dfs(v):
    visited_dfs[v] = True
    print(v, end =' ')

    for x in graph[v]:
        if not visited_dfs[x]:
            dfs(x)


def bfs(v):
    visited_bfs[v] = True
    queue = deque([v])

    while queue:
        current = queue.popleft()
        print(current, end = ' ')

        for x in graph[current]:
            if not visited_bfs[x]:
                visited_bfs[x] = True
                queue.append(x)


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

dfs(V)
print()

bfs(V)
print()