from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i, num in enumerate(nums):
        e = target - num
        for j in range(i+1, len(nums)):
            if nums[j] == e:
                return [i, j]

a = [2, 7, 0, 6, 18, 23, 78]
b = [2,1,1,1,1,1,1]
ii = twoSum(0, a, 84)
print(ii)
a*b
print(a*b)