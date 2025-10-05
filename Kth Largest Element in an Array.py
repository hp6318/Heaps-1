'''
Solution 1: Using Min-heaps - Favoured when K is small. 
    - Maintain a heap of size=k.
    - if size>k, then pop the smallest/top element of heap. 
    - Kth largest is the top of the heap after iterating over all elements.
Time complexity: O(NlogK)
Space complexity: O(k)
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for i in nums:
            heapq.heappush(heap,i)
            if len(heap)>k:
                heapq.heappop(heap) 
        
        return heap[0]

'''
Solution 2: Using Max-heaps - Favoured when K is big. 
    - Maintain a heap of size=(N-k).
    - if size>(N-k), then pop the biggest/top element of heap. 
    - keep a track of min_element, when popping out. At the end, result stores the Kth
      largest element 
Time complexity: O(Nlog(N-k))
Space complexity: O(N-k)
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        result = 10**4 + 1 # max value
        for i in nums:
            heapq.heappush(heap,-i) # make it max heap
            if len(heap)>len(nums)-k:
                result=min(result,-heapq.heappop(heap))

        return result
