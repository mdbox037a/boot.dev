def sum_nums(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_nums(nums[1:])
