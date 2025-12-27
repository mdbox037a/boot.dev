def subset_sum(nums, target):
    return find_subset_sum(nums, target, len(nums) - 1)


def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    elif index < 0:
        return False

    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    else:
        resultA = find_subset_sum(nums, target, index - 1)
        resultB = find_subset_sum(nums, target - nums[index], index - 1)
        if resultA or resultB:
            return True
        else:
            return False
