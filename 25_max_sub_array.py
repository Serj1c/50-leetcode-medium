def maxSubArray(nums) -> int:
    cur_sum = nums[0] # it is ok cause by description len is at least 1
    max_sum = nums[0]

    for i in range(1, len(nums)):
        cur_sum = max(cur_sum + nums[i], nums[i])
        max_sum = max(max_sum, cur_sum)

    return max_sum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))