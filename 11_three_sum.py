def three_sum(nums):
    nums.sort()
    res = set()
    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            potentialSum = nums[i] + nums[l] + nums[r] 
            if potentialSum > 0:
                r -= 1
            elif potentialSum < 0:
                l += 1
            else:
                res.add((nums[i] , nums[l] ,nums[r]))
                l += 1
                r -= 1
    return res


print(three_sum([-1,0,1,2,-1,-4]))