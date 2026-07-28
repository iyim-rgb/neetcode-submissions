class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        strs_sorted = []

        for word in strs:
            strs_sorted.append(sorted(word))
        
        used = []

        for i in range(len(strs_sorted)):
            if strs[i] not in used:
                group = []
                group.append(strs[i])
                used.append(strs[i])
                for j in range(len(strs_sorted)):
                    if strs_sorted[i] == strs_sorted[j] and i != j:
                        group.append(strs[j])
                        used.append(strs[j])
                
                ans.append(group)

        return ans

            
        

            