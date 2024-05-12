def find_duplicates(nums):
    ans = []
    for num in nums:
        n = abs(num)
        if nums[n-1] < 0:
            ans.append(abs(num))
        nums[n-1] *= -1

    return ans


print(find_duplicates([4,3,2,7,8,2,3,1]))
print(find_duplicates([1,1,2]))
print(find_duplicates([1]))