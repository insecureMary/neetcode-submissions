class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bigList = []
        seen = {}
        for i, word in enumerate(strs):
            key = "".join(sorted(word))
            if key in seen:
                coolIndex = seen[key]
                bigList[coolIndex].append(word)
            else:
                bigList.append([word])
                seen[key] = len(bigList) - 1
        
        return bigList





        