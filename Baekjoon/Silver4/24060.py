sorted
def merge(arr, left, mid, right):
    i = left 
    j = mid+1
    k = left
    
    while(i<= mid and j <= right):
        if(arr[i] <= arr[j]):
            sorted[k] = arr[i]
            k+=1 
            i+=1
        else:
            sorted[k] = arr[j]
            k+=1
            j+=1
    
    if(i<=mid):
        for idx in range(i, mid):
            sorted[k] = arr[idx]
            k+=1
    elif(j<=right):
        for idx in range(j, right):
            sorted[k] = arr[idx]
            j+=1
    
    for idx in range(right):
        arr[idx] = sorted[idx]
    
def merge_sort(arr, left, right, k):
    if(left < right):
        mid = (left+right)//2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)
        
N, K = map(int, input().split())
A = list(map(int, input().split()))

merge_sort(A, 0, N, K)