def findDifferentBinaryString(self, nums: List[str]) -> str:
    diff = ""

    for idx, num in enumerate(nums):
        if num[idx] == "0":
            diff += "1"
        else:
            diff += "0"

    return diff