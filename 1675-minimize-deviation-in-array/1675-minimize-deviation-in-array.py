import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        answer = 10**20
        for num in nums:
            if num % 2 == 0:
                heappush(heap, -num)
            else:
                heappush(heap, -num*2)
        
        _min = -max(heap)

        while True:
            _max = -heappop(heap)
            answer = min(answer, _max-_min)
            
            if _max % 2:
                break

            heappush(heap, -_max//2)
            _min = min(_min, _max//2)

        return answer