class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {}
        done = {}
        largest_consecutive = 0
        for num in nums:
            nums_dict[num] = [num]
            done[num] = False
        for key in nums_dict:
            if done[key] == False:
                self.rec(key, nums_dict, done)
            if largest_consecutive < len(nums_dict[key]):
                largest_consecutive = len(nums_dict[key])
        return largest_consecutive


    def rec(self, key: int, nums_dict: {}, done: {}) -> List[int]:
        if done[key] == True:
            return nums_dict[key]
        target = key + 1
        done[key] = True
        if (target not in nums_dict):
            return nums_dict[key]

        nums_dict[key].extend(self.rec(target, nums_dict, done))
        return nums_dict[key]