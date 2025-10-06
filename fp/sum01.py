def sum_nums(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_nums(nums[1:])


# call from terminal for testing:
# python3 -c "from sum01 import sum_nums; print(sum_nums((1, 2, 3)))"
