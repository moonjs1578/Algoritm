import sys
input = sys.stdin.readline

N = int(input())

stairs = [0] * (N + 1)
sol = [0] * (N + 1)

for i in range(1, N + 1):
    stairs[i] = int(input())

if N == 1:
    print(stairs[1])
else:
    sol[1] = stairs[1]
    sol[2] = stairs[1] + stairs[2]

    for i in range(3, N + 1):
        sol[i] = stairs[i] + max(sol[i-3] + stairs[i-1], sol[i-2])

    print(sol[N])