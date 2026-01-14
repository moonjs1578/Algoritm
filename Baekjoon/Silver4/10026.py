import sys
from collections import deque # [필수] 큐를 쓰기 위해 가져옴

input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    visited[x][y] = True
    current_color = array[x][y]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft() # 줄 맨 앞사람 꺼내기, 그냥 pop하면 맨 뒤에 있는 인덱스 나옴
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < N) and (0 <= ny < N):
                if not visited[nx][ny]:
                    if array[nx][ny] == current_color:
                        visited[nx][ny] = True 
                        q.append((nx, ny))

N = int(input())
array = []
for i in range(N):
    array.append(list(input().strip()))
                 
visited = [[False] * N for _ in range(N)]
cnt_normal = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j) 
            cnt_normal += 1
            
            
for i in range(N):
    for j in range(N):
        if array[i][j] == 'R':
            array[i][j] = 'G'

visited = [[False] * N for _ in range(N)] 
cnt_blind = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j) 
            cnt_blind += 1
        
print(cnt_normal, cnt_blind)