def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping is True:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                holder = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = holder
                swapping = True
        end -= 1
    return nums
