class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()

        for num in nums:
            hashset.add(num)
        
        sol = 0

        while hashset:
            tmp = 1
            val = hashset.pop()
            left = val - 1

            while left in hashset:
                hashset.remove(left)
                tmp += 1
                left -= 1
            
            right = val + 1
            while right in hashset:
                hashset.remove(right)
                tmp += 1
                right += 1
            
            sol = max(sol, tmp)
        
        return sol
