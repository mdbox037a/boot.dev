def bad_get_median_font_size(font_sizes):
    sorted_list = sorted(font_sizes)
    if len(sorted_list) == 0:
        return
    elif len(sorted_list) % 2 != 0:
        tuple_median = len(sorted_list) // 2
        return sorted_list[tuple_median]
    else:
        tuple_median = (len(sorted_list) // 2) - 1
        return sorted_list[tuple_median]


# much better:


def better_get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None
    return sorted(font_sizes)[(len(font_sizes) - 1) // 2]
