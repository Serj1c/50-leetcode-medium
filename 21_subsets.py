def subsets(nums):
    ans = []

    def helper(i, subset):
        ans.append(subset)

        if i < len(nums):
            for j in range(i, len(nums)):
                helper(j+1, subset+[nums[j]])
    
    helper(0, [])
    return ans


print(subsets([1,2,3]))
print(subsets([0]))
    