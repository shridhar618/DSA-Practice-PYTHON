def min_num(nums):
    min=nums[0]
    for i in range(len(nums)):
        if nums[i]<min:
            min=nums[i]
    return min

nums=[3,6,8,9,1,2]
result=min_num(nums)
print(result)