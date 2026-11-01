class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sols = []

        counts = Counter(nums)

        def rec(counts: Dict[int, int], agg: List[int]):
            if len(agg) == len(nums):
                sols.append(agg)
                return
            for num in counts.keys():
                if counts[num] > 0:
                    agg.append(num)
                    counts[num] -= 1
                    rec(counts, agg[:])

                    counts[num] += 1
                    agg.pop()
        
        rec(counts, [])

        return sols