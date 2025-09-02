def duplicate(nums):
    arr=[]
    for i in nums:
        if i not in arr:
            arr.append(i)
    return arr
        

nums=[2,5,2,5,8,9]
print(duplicate(nums))