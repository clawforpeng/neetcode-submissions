class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sols = []

        visited = [False] * len(nums)

        def rec(permutation: List[int], visited: List[bool]):
            if len(permutation) == len(nums):
                sols.append(list(permutation))
                permutation.pop()
            else:
                for i, isVisited in enumerate(visited):
                    if not isVisited:
                        permutation.append(nums[i])
                        visited[i] = True
                        rec(list(permutation), visited)
                        permutation.pop()
                        visited[i] = False
        
        for i in range(len(nums)):
            visited[i] = True
            rec([nums[i]], visited)
            visited[i] = False


        return sols