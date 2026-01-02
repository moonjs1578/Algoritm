N = int(input())
stairs = [0]*(N+1)
for i in range(1, N+1):
    stairs[i] = int(input())
    
def sol(N):
    if N == 0:
        return 0
    elif N == 1:
        return stairs[1]
    elif N == 2:
        return stairs[1] + stairs[2]
    
    result = stairs[N] + max(sol(N-3) + stairs[N-1], sol(N-2)) # 1, 2계단 택1이므로 3개로 묶어서 생각
    
    return result

print(sol(N))