class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        result = [0, 0]
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                temp = nums[i] + nums[j];
                if (temp == target):
                    result[0] = i
                    result[1] = j
                    break
                temp = 0
        return result
        
