class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low,high = 0,max(time)*totalTrips
        while(low<high):
            mid = (low+high)//2
            t = 0
            for i in time:
                t+=(mid//i)
                
            if t<totalTrips:
                low = mid+1
            else:
                high = mid
        return low
        
            