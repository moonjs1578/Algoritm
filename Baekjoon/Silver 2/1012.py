from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    arr[x][y] = 0  

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        current_x, current_y = queue.popleft()  

        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:  
                arr[nx][ny] = 0  
                queue.append((nx, ny))  


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1  

    cnt = 0
    for i in range(N):
        for j in range(M):  
            if arr[i][j] == 1:  
                bfs(i, j)
                cnt += 1
                
    print(cnt)