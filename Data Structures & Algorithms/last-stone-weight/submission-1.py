import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap 
        # 1. heapify
        # 2. chose h[0], pop it and store temp var-> first 
        # 3. chose h[0], pop it, and store temp var -> second
        # 4.1 if first == second, end
        # 4.2 elif first<second, then push y-x
        # repeat 2,3,4 till one element left in h 

        stones= [-x for x in stones]

        heapq.heapify(stones)
        #print(stones)

        while len(stones)>1: 
            first = -1* heapq.heappop(stones)
            second = -1* heapq.heappop(stones)
            #print(first, second)

            if first<second: 
                heapq.heappush(stones, -1*(second-first))
            if second<first:
                heapq.heappush(stones, -1*(first-second))
        
        if stones:
            return -1*stones[0]
        else:
            return 0
                
        