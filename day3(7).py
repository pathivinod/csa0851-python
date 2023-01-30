from collections import Counter
def permuteUnique(nums):
    def backtrack(first=0):
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            if i > first and nums[i] == nums[first]:
                continue
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]
    n = len(nums)
    output = []
    backtrack()
    return output
print(permuteUnique([1,1,2]))
