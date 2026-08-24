class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sols = []
        maxHeap = []
        for i in range(k):
            maxHeap.append((-nums[i], i))

        heapq.heapify(maxHeap)
        sols.append(-maxHeap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))
            while (maxHeap[0][1] <= i - k):
                heapq.heappop(maxHeap)
            sols.append(-maxHeap[0][0])

        return sols