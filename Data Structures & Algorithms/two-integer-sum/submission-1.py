class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        frequency_dict = defaultdict(list)

        for index, num in enumerate(nums):
            frequency_dict[num].append(index)
        
        for i in range(len(nums)):
            target_index = target - nums[i]
            if len(frequency_dict[target_index]) > 0:
                if nums[i] == target_index:
                    if len(frequency_dict[target_index]) > 1:
                        return [frequency_dict[target_index][0], frequency_dict[target_index][1]]
                else:
                    return [i, frequency_dict[target_index][0]]

        # should not happen in this problem
        return[]