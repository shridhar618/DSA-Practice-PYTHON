def max_num(nums):
    max=nums[0]
    for i in range(len(nums)):
        if nums[i]>max:
            max=nums[i]
    return max

nums=[5,6,1,3,9,7]
result=max_num(nums)
print(result)