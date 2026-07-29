class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # {1:1, 2:2}
        
        ans = []
        
        for _ in range(len(freq)): # 3 times 
            max_val = max(freq.values()) # 2
            for key in freq.keys(): #1, 2
                if freq[key] == max_val:
                    max_key = key # 2
            ans.append(max_key) # [3, 2, 1]
            freq.pop(max_key)
        
        return ans[:k]
        
            