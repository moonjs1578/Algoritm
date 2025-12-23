import sys

# [필수] N이 최대 500,000이므로 기본 재귀 깊이(1,000)를 늘려줘야 함
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def quick_sort(arr, p, r):
    if p < r:
        # 분할(partition)을 수행하고 피벗의 확정 위치(q)를 받아옴
        q = partition(arr, p, r)
        
        # 피벗을 기준으로 왼쪽과 오른쪽을 재귀적으로 정렬
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)

def partition(arr, p, r):
    global cnt, K # 전역 변수 사용
    
    x = arr[r] # 피벗은 해당 구간의 맨 오른쪽 값
    i = p - 1  # i: 피벗보다 작은 값들이 모인 구역의 끝 지점 (아직 없으므로 p-1)
    
    # j: 탐색 인덱스 (p부터 r-1까지)
    for j in range(p, r):
        if arr[j] <= x: # 현재 값이 피벗보다 작거나 같다면
            i += 1
            # [교환 1] 작은 구역(i)을 한 칸 넓히고, 현재 값(j)을 그곳으로 보냄
            arr[i], arr[j] = arr[j], arr[i]
            cnt += 1
            
            # K번째 교환인지 확인
            if cnt == K:
                print(f"{min(arr[i], arr[j])} {max(arr[i], arr[j])}")
                sys.exit(0) # 정답을 찾으면 프로그램 즉시 종료
                
    # [교환 2] 탐색이 끝나면 피벗(arr[r])을 자신의 자리(i+1)로 이동
    if i + 1 != r:
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        cnt += 1
        
        if cnt == K:
            print(f"{min(arr[i + 1], arr[r])} {max(arr[i + 1], arr[r])}")
            sys.exit(0)
            
    return i + 1 # 피벗의 최종 위치 반환

# 입력 받기
N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0 # 총 교환 횟수

quick_sort(A, 0, N - 1)

# 여기까지 코드가 실행되었다면 K번 교환이 일어나지 않은 것
print(-1)