class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                return [hash[nums[i]], i]
            hash[target - nums[i]] = i
            
        return [-1, -1]