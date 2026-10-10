import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums: 
            heapq.heappush(h, num*-1)
        ans = 0
        for i in range(k):
            ans = -1*heapq.heappop(h)
        
        return ans
