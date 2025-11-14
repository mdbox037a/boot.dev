def count_names(list_of_lists, target_name):
    count = 0
    for name_list in list_of_lists:
        if target_name in name_list:
            count += 1
    return count
