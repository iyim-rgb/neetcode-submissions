class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        order = 0
        duplicate = -1
        c = {}
        max_len = 0
        

        if len(nums) < 2:
            return len(nums)

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i - 1] + 1 == sorted_nums[i]:
                c[order] = c.get(order, [sorted_nums[i - 1]]) + [sorted_nums[i]]
            elif sorted_nums[i - 1] == sorted_nums[i]:
                c[duplicate] = [sorted_nums[i]]
                duplicate -= 1
            else:
                order += 1
                c[order] = [sorted_nums[i]]



        for value in c.values():
            length = len(value)
            if length >= max_len:
                max_len = length

        return max_len

        