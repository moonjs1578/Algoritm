def select_sort(arr, k):
    n = len(arr)
    cnt = 0
    for i in range(n-1, 0, -1):
        max_idx = i
        
        for j in range(i):
            if(arr[max_idx] < arr[j]):
                max_idx = j
                
        if max_idx != i:   
            arr[max_idx], arr[i] = arr[i], arr[max_idx]
            cnt+=1
            
        if(cnt == k) :
            print(f"{arr[max_idx]} {arr[i]}")
            return
    
    print(-1)

N, K = map(int, input().split())
A = list(map(int, input().split()))

select_sort(A, K)
