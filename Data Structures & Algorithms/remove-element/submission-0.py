class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        left = 0 
        right = len(nums) - 1

        while left <= right:
            num = nums[left]
            if num == val:
                if left == right:
                    k += 1
                    break
                if nums[right] == val:
                    k += 1
                    right -= 1
                else:
                    k += 1
                    tmp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = tmp
                    left += 1
                    right -= 1
            else:
                left += 1

        return len(nums) - k