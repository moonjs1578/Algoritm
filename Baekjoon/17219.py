import sys
input = sys.stdin.readline

N , M = map(int, input().split())

dic = {}
for i in range(N):
    id, password = input().split()
    dic[id] = password

for i in range(M):
    id = input().strip()
    print(dic[id])