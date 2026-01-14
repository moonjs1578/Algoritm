import sys
input = sys.stdin.readline

class MinHeap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        idx = len(self.heap) -1 

        while idx > 1:
            parent = idx // 2
            if(self.heap[idx] < self.heap[parent]):
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def pop(self):
        if len(self.heap) == 1:
            return 0
        
        min_value = self.heap[1]

        self.heap[1] = self.heap[-1]
        self.heap.pop()

        if len(self.heap) == 1:
            return min_value
        
        idx = 1
        while idx*2 < len(self.heap):
            left = idx*2
            right = idx*2+1
            smaller = left

            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smaller = right

            if self.heap[smaller] < self.heap[idx]:
                self.heap[idx], self.heap[smaller] = self.heap[smaller], self.heap[idx]
                idx = smaller
            else:
                break
        
        return min_value
    

N = int(input())
heap = MinHeap()

for _ in range(N):
    x = int(input())

    if x==0:
        print(heap.pop())
    else:
        heap.push(x)
