class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0

        hashMap = {}
        hashMap[0] = 1
        sol = 0

        for num in nums:
            prefixSum += num

            if prefixSum not in hashMap:
                hashMap[prefixSum] = 1
            else:
                hashMap[prefixSum] += 1
            
            if prefixSum - k in hashMap:
                if k == 0:
                    sol += hashMap[prefixSum - k] - 1
                else:
                    sol += hashMap[prefixSum - k]
        
        return sol