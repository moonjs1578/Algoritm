import sys

# 시간 초과 방지를 위해 빠른 입력 사용 (input() 대신 사용)
input = sys.stdin.readline

def insertion_sort(arr, k):
    n = len(arr)
    cnt = 0  # 저장(대입) 횟수를 세는 변수
    
    # 1. 두 번째 원소(인덱스 1)부터 마지막 원소까지 순회
    # (첫 번째 원소는 이미 정렬된 상태라고 가정하기 때문)
    for i in range(1, n):
        key = arr[i]  # 이번에 정렬할 값 (따로 빼둠)
        j = i - 1     # key 바로 앞의 인덱스부터 비교 시작
        
        # 2. 정렬된 앞부분(0 ~ i-1)을 뒤에서부터 앞으로 훑으며 비교
        # 조건: j가 0보다 크거나 같고, key보다 앞의 값이 더 크다면
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # [저장 1] 큰 값을 뒤로 한 칸 밈 (Shift)
            cnt += 1             # 저장 횟수 증가
            
            # K번째 저장이라면, 방금 저장한 값을 출력하고 종료
            if cnt == k:
                print(arr[j + 1]) 
                return
            
            j -= 1  # 더 앞쪽 값과 비교하기 위해 인덱스 감소
        
        # 3. while문을 빠져나왔다는 건, key가 들어갈 자리를 찾았다는 뜻 (j+1 위치)
        # 제자리(i)가 아니라면 이동이 있었다는 뜻이므로 key를 삽입
        if j + 1 != i:
            arr[j + 1] = key  # [저장 2] 찾은 빈 자리에 key 삽입
            cnt += 1          # 저장 횟수 증가
            
            # [주의] 여기서도 저장이 발생하므로 K번째인지 꼭 확인해야 합니다!
            # (작성하신 코드에는 이 부분이 빠져 있어서 추가가 필요합니다)
            if cnt == k:
                print(key)  # key값(arr[j+1]) 출력
                return

    # 4. 모든 정렬이 끝날 때까지 K번 저장이 안 일어났다면 -1 출력
    print(-1)

# 입력 받기
# N: 배열의 크기, K: 저장 횟수 제한
N, K = map(int, input().split())
# A: 정렬할 숫자 리스트
A = list(map(int, input().split()))

insertion_sort(A, K)