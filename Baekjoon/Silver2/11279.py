import sys
input = sys.stdin.readline
N = int(input())

class MaxHeap:
    def __init__(self):
        self.heap = [0]
    
    def push(self, x):
        self.heap.append(x)
        idx = len(self.heap) - 1

        while idx > 1:
            parent = idx // 2

            if self.heap[parent] < self.heap[idx]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def pop(self):
        # 빈 힙 처리
        if len(self.heap) == 1:
            return 0 
        
        max_value = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        
        if len(self.heap) == 1:
            return max_value
        
        
        idx = 1
        while idx*2 < len(self.heap):
            left = idx*2
            right = idx*2 + 1

            large = left
            if right < len(self.heap) and self.heap[right] > self.heap[left]:
                large = right
            
            if self.heap[idx] >= self.heap[large]:
                break

            self.heap[idx], self.heap[large] = self.heap[large], self.heap[idx]
            idx = large

        return max_value
    
myheap = MaxHeap()

for i in range(N):
    x = int(input())

    if x == 0:
        print(myheap.pop())
    else:
        myheap.push(x)