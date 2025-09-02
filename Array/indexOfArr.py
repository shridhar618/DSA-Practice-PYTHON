def index(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return "target not found"
        
arr=[5,9,2,9,1,5,3]
target=9
print(index(arr, target))