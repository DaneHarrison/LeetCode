def twoSum(self, nums, target):
    seen = {}

    for idx, num in enumerate(nums):
        diff = target - num
        diffIdx = seen.get(diff)

        if diffIdx is not None:
            return [diffIdx, idx]

        seen[num] = idx

    return []