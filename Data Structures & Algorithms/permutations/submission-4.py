class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sols = []

        visited = [False] * len(nums)

        def rec(permutation: List[int], visited: List[bool]):
            if len(permutation) == len(nums):
                sols.append(list(permutation))
            else:
                for i, isVisited in enumerate(visited):
                    if not isVisited:
                        permutation.append(nums[i])
                        visited[i] = True
                        rec(permutation, visited)
                        permutation.pop()
                        visited[i] = False
        


        rec([], visited)



        return sols