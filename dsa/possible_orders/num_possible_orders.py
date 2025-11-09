def num_possible_orders(num_posts):
    total = 1
    for i in range(1, num_posts + 1):
        total *= i
    return total


# don't need to make a special case for num_posts == 0, because total is set
# to 1 from the beginning and the for loop just won't run if num_posts == 0
