class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        maxNonOverlapped = 0

        end = intervals[0][1]
        for interval in intervals:
            if interval[0] >= end:
                maxNonOverlapped += 1
                end = interval[1]
            else:
                end = min(end, interval[1])
        
        return len(intervals) - maxNonOverlapped - 1