def productExceptSelf(self, nums):
    answers = [1 for x in nums]

    accum = 1

    for i in range(len(nums) -1):
        accum *= nums[i]
        answers[i + 1] *= accum

    accum = 1
    for i in range(len(nums) - 1, 0, -1):
        accum *= nums[i]
        answers[i - 1] *= accum

    return answers