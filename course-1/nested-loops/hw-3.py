nums = [3, 7, 4]
for i in range(len(nums)):
    for k in range(len(nums)):
        if nums[k] != nums[i]: print(10*nums[i]+nums[k])