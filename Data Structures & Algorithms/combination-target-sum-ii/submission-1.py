class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sols = []
        candidates.sort()

        def rec(i: int, target: int, acc: List[int]):
            if i == len(candidates):
                return
            cur = candidates[i]
            
            if cur > target:
                return
            elif cur == target:
                acc.append(cur)
                sols.append(acc)
            else:
                j = i + 1
                while j < len(candidates) and candidates[j] == cur:
                    j += 1

                rec(j, target, list(acc))
                
                acc.append(cur)
                rec(i + 1, target - cur, list(acc))
            
        rec(0, target, [])
        return sols