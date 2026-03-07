def longestConsecutive(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    best = 1
    numSet = set(nums)

    for num in numSet:
        count = 1

        if num - 1 in numSet:
            continue

        while num + count in numSet:
            count += 1

        best = max(count, best)

    return best