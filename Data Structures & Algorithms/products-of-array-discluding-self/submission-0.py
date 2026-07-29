class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            product = 1
            if i == 0:
                excluded_nums = nums[1:]
            elif i == len(nums) - 1:
                excluded_nums = nums[:i]
            else:
                excluded_nums = nums[:i] + nums[i + 1:]
            for number in excluded_nums:
                product *= number
            
            ans.append(product)
        
        return ans
        
