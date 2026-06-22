from typing import List

def threeSum(self, nums: list[int]) -> list[list[int]]:
    if len(nums) < 3:
        return []

    nums.sort()
    res = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        l = i + 1
        r = len(nums) - 1
        
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            
            if sum == 0:
                res.append([nums[i], nums[l], nums[r]])
                
                l += 1
                r -= 1
                
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
    return res
            