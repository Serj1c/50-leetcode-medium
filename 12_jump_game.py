def can_jump(nums) -> bool:
    amount = 0
    for num in nums:
        if amount < 0:
            return False
        if num > amount:
            amount = num
        amount -= 1
            
    return True


print(can_jump([2,3,1,1,4]))
print(can_jump([3,2,1,0,4]))