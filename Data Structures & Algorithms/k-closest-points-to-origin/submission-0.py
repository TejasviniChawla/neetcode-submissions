import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h= []
        ans =[]
        for x,y in points: 
            heapq.heappush(h, (x*x+y*y, [x,y]))
        for i in range(k):
            d, point = heapq.heappop(h)
            ans.append(point)
        return ans

        
