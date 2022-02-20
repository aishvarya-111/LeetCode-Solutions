class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0],-x[1]))
        right, rem, n = -1, 0, len(intervals)
        for x,y in intervals:
            if y <= right:
                rem += 1
            else:
                right = y
        return n - rem