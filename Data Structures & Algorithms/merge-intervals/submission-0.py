class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        start, end = intervals[0][0], intervals[0][1]

        sols = []

        for index, interval in enumerate(intervals):
            newStart, newEnd = interval[0], interval[1]

            if newStart <= end:
                start = min(start, newStart)
                end = max(end, newEnd)
            else:
                sols.append([start, end])
                start = newStart
                end = newEnd
            
            if index == len(intervals) - 1:
                sols.append([start, end])
        
        return sols