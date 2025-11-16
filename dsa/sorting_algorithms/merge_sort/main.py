def merge_sort(nums):
    if len(nums) < 2:
        return nums
    half = len(nums) // 2
    nums1 = nums[:half]
    nums2 = nums[half:]
    sorted1 = merge_sort(nums1)
    sorted2 = merge_sort(nums2)
    return merge(sorted1, sorted2)


def merge(first, second):
    final = []
    i = 0
    j = 0
    while (i < len(first)) and (j < len(second)):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    if i < len(first):
        while i < len(first):
            final.append(first[i])
            i += 1
    elif j < len(second):
        while j < len(second):
            final.append(second[j])
            j += 1
    return final
