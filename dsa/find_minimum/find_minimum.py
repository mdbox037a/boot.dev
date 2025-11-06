def find_minimum(nums):
    minimum = float("inf")
    if not nums:
        return None
    else:
        for num in nums:
            if num < minimum:
                minimum = num
        return minimum
