class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0

        incoming = []
        scheduled = []

        sols = []

        for i in range(len(tasks)):
            task = tasks[i]
            heapq.heappush(incoming, [task[0], task[1], i])
        
        while incoming or scheduled:
            while incoming and time >= incoming[0][0]:
                t = heapq.heappop(incoming)
                heapq.heappush(scheduled, [t[1], t[0], t[2]])
            
            if not scheduled:
                time = incoming[0][0]
                while incoming and time >= incoming[0][0]:
                    t = heapq.heappop(incoming)
                    heapq.heappush(scheduled, [t[1], t[0], t[2]])
            
            task = heapq.heappop(scheduled)
            sols.append(task[2])

            time += task[0]
        
        return sols
