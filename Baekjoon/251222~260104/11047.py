N, K = map(int, input().split())

moneys = []

for i in range(N):
    moneys.append(int(input()))

cnt = 0

while(K>0):
    for money in reversed(moneys):
        if(K >= money):
            cnt += K // money
            K %= money

print(cnt)