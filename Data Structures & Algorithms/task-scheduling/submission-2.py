class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pendingQueue = deque()
        time = 0

        counts = Counter(tasks)

        maxHeap = []

        for task, count in counts.items():
            heapq.heappush(maxHeap, (-count, task))
        
        while maxHeap or pendingQueue:
            time += 1
            while pendingQueue:
                if pendingQueue[0][0] == time:
                    task = pendingQueue.popleft()
                    heapq.heappush(maxHeap, (task[1], task[2]))
                else:
                    break

            if maxHeap:
                ta = heapq.heappop(maxHeap)
                if ta[0] + 1 < 0:
                    pendingQueue.append((time + n + 1, ta[0] + 1, ta[1]))
        
        return time