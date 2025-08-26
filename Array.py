# Check if any value appears at least twice
def findNum():
    for i in range(len(arr)):
        for j in range(i+1,(len(arr))):
            if arr[i] == arr[j]:
                return "true",arr[i]
    return "false"

arr = [1,2,3,3,5]
print(findNum())


# Find index of target using Binary Search
def indexFinder(nums,target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [1,2,3,4,5,6,7]
target = 5
print(indexFinder(nums,target))


# Merge two sorted arrays (without sort function)
def sort_array(arr1,arr2):
    arr3 = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    while i < len(arr1):
        arr3.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr3.append(arr2[j])
        j += 1

    return arr3

arr1 = [1,2,3]
arr2 = [4,5,6]
print(sort_array(arr1,arr2))


# Second largest number in array
def second_largest(arr):
    largest = 0
    second = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):  
            if arr[i] > arr[j]:
                if arr[i] > largest:
                    second = largest
                    largest = arr[i]
                elif arr[i] > second and arr[i] != largest:
                    second = arr[i]
            else:
                if arr[j] > largest:
                    second = largest
                    largest = arr[j]
                elif arr[j] > second and arr[j] != largest:
                    second = arr[j]
    return second if second != 0 else None

arr = [1, 4, 2, 6, 7,7]
print(second_largest(arr))  


# Two Sum Problem
def twoNum(nums,target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    return pairs

nums = [2,3,5,4,1]
target = 5
print(twoNum(nums,target))   


# Reverse an array
nums = [2,4,7,3,5,8]
reverse_nums = []
i = len(nums)-1
while i >= 0:
    reverse_nums.append((nums[i]))
    i -= 1
print(reverse_nums)


# Move zeros to end
def zeroes(arr):
    i = 0  
    for j in range(len(arr)): 
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1
    while i < len(arr):
        arr[i] = 0
        i += 1
    return arr

arr = [2, 0, 3, 4, 0, 1, 6, 7, 0]
print(zeroes(arr))


# Missing number in sequence
arr = [1,2,4,5,6,7]
missing = 1
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+1 != arr[j]:
            missing = arr[i]+1
            break
    if missing != 1:
        break

if missing in arr:
    missing = arr[-1]+1



