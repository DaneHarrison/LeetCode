from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    if len(nums) == 0:
        return []
    
    products = [1 for _ in range(len(nums))]
    val = nums[0]
    for i in range(1, nums):
        products[i] *= val
        val *= nums[i]
        
    val = nums[-1]
    for i in range(len(nums) - 2, 0, -1):
        products[i] *= val
        val *= nums[i]
        
    return products