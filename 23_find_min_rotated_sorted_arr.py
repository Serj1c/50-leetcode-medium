def find_min(nums) -> int:
    if len(nums) == 1:
        return nums[0]
    l, r = 0, len(nums)-1
    if nums[l] < nums[r]:
        return nums[0]

    while l <= r:
        mid = (l+r) // 2
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]

        if nums[mid] > nums[r]:
            l = mid
        else:
            r = mid


print(find_min([3,4,5,1,2]))
print(find_min([4,5,6,7,0,1,2]))