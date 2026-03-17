nums = ["a", "b", "c", "d"]
factor = 2

for num in range(len(nums)):
    nums[num] *= factor

print(nums)

# alternate solution
nums2 = [1, 2, 3, 4]

for index, num in enumerate(nums2):
    nums2[index] = num * factor

print(nums2)