class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = []
        dicts = []
        for str in strs:
            single_dict = {}
            for char in str:
                if char in single_dict:
                    single_dict[char] = single_dict[char] + 1
                else:
                    single_dict[char] = 1
            if (single_dict in dicts):
                answers[dicts.index(single_dict)].append(str)
            else:
                dicts.append(single_dict)
                answers.append([str])
        return answers
        
