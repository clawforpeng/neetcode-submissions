class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # special case: list with 1 zero, list with 2+ zeros
        num_of_zeros = 0
        total_product = 1
        answer = [0] * len(nums)
        for num in nums:
            if num == 0:
                num_of_zeros += 1
            else:
                total_product *= num
        
        if num_of_zeros > 1:
            return answer
        
        if num_of_zeros == 1:
            answer[nums.index(0)] = total_product
            return answer

        for i in range(len(nums)):
            answer[i] = int(total_product / nums[i])
        
        return answer