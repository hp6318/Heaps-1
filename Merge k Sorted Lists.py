'''
Solution - Min-heap with custom comparator by creating wrapper heapNode
    - Add the listNodes of all lists wrapped under heapNode whose comparator funtion
      is defined in a min-heap (priority queue)
    - create a dummy head. point it's next to listNode at top of heap (which is at minimum value)
    - if the poped node from the heap has a next (more elements of that list), then 
      add that listNode by wrapping under a newly created heapNode. 
    - repeat until heap is empty
Time Complexity: 
    - O(klogk) : add first nodes of all list to heap
    - O(N*klogk) : N=total nodes(or elements) combined across all lists. 
                   Adding them to the priority queue/heap. 
                   Since heap size is always <=k, bubbling up/down while pushing 
                   N nodes is N*klogk
    Total : O(N*klogk)
Space Complexity: 
    - O(k) : maintaining heap of size k
    - O(N) : creating N heapNodes to wrap ListNodes for using custom comparator in heaps.
    Total: O(N)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class heapNode:
    def __init__(self,listNode):
        self.listnode = listNode
    def __lt__(self,other_node):
        return self.listnode.val<=other_node.listnode.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for li in lists:
            if li!=None:
                heapq.heappush(heap,(heapNode(li))) # create new heapNode in order to use custom comparator

        head = ListNode()
        node = head
        while heap:
            node.next = heapq.heappop(heap).listnode
            node = node.next
            if node.next!=None:
                heapq.heappush(heap,(heapNode(node.next)))
        
        return head.next
