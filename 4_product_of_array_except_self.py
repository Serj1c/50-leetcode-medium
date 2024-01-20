def product_except_self(nums):
    ans = [1]
    for i in range(1,len(nums)):
        ans.append(ans[-1]*nums[i-1])

    cur = 1
    for i in range(len(nums)-2, -1, -1):
        cur = cur * nums[i+1]
        ans[i] = ans[i] * cur

    return ans