"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        sol = 0
        count = 0 # current meeting count

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        i, j = 0, 0
        timestamp = 0

        while i < len(start) and j < len(end):
            s = start[i]
            e = end[j]

            timestamp = min(s, e)

            if e == timestamp:
                j += 1
                count -= 1
            else:
                i += 1
                count += 1
            
            sol = max(sol, count)


        return sol
