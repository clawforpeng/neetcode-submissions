class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answers = []
        frequency_dict = defaultdict(int)
        for num in nums:
            frequency_dict[num] += 1
        # key: frequency; value: list of nums that has that frequency
        frequency_map = [[] for _ in range(len(nums) + 1)]
        for num in frequency_dict:
            frequency_map[frequency_dict[num]].append(num)
        
        tmp = k

        for fre in reversed(frequency_map):
            if tmp == 0:
                break
            if len(fre) > 0:
                for num in fre:
                    if tmp > 0:
                        answers.append(num)
                        tmp = tmp - 1
                    else:
                        break
        
        return answers
