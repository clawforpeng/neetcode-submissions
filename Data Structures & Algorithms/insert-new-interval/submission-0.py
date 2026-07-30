class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sols = []

        newStart, newEnd = newInterval[0], newInterval[1]

        i = 0

        while i < len(intervals) and intervals[i][1] < newStart:
            sols.append(intervals[i])
            i += 1
        
        while i < len(intervals) and newEnd >= intervals[i][0]:
            newStart = min(intervals[i][0], newStart)
            newEnd = max(intervals[i][1], newEnd)
            i += 1
        
        sols.append([newStart, newEnd])

        while i < len(intervals):
            sols.append(intervals[i])
            i += 1

        return sols